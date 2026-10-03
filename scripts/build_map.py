#!/usr/bin/env python3
"""Build a static semantic index from titles. No article bodies or remote APIs."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import re

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("NUMBA_NUM_THREADS", "4")

# Top-level categories group the topics below; map points are colored by category.
CATEGORIES = {
    "Health & Body": ("健康・からだ", "#cf7f72"),
    "Food & Drink": ("食・飲み物", "#d6a04d"),
    "Travel & Transport": ("旅行・交通", "#3f93a3"),
    "Tech & AI": ("テクノロジー・AI", "#8170c2"),
    "Work & Money": ("仕事・お金", "#5d83b8"),
    "Life & People": ("暮らし・人間関係", "#c48a9c"),
    "Entertainment & Culture": ("エンタメ・文化", "#b07cb8"),
    "Nature & Environment": ("自然・動物・環境", "#6f9f5f"),
    "Science & Space": ("科学・宇宙", "#5fa59c"),
    "Society & History": ("社会・政治・歴史", "#8f8a9f"),
    "Learning & Language": ("教育・言語", "#9a9a4c"),
    "Sports & Outdoors": ("スポーツ", "#c27a5a"),
}
# Broad topics are assigned by embedding similarity: name -> (description, label, category).
TOPICS = {
    "Travel": ("Travel, tourism, vacation destinations, hotels, tourists and sightseeing.", "旅行", "Travel & Transport"),
    "Transportation": ("Transportation, commuting, traffic, trains, cars, aviation, airlines and public transport.", "交通", "Travel & Transport"),
    "Technology": ("Technology, computers, smartphones, software, digital products, gadgets and the internet.", "テクノロジー", "Tech & AI"),
    "AI": ("Artificial intelligence, generative AI, ChatGPT, chatbots, machine learning and AI applications.", "AI", "Tech & AI"),
    "Health": ("Health, medicine, diseases, medical treatments, nutrition, sleep and physical fitness.", "健康・医療", "Health & Body"),
    "Psychology": ("Psychology, emotions, happiness, personality, mental health, stress and human behavior.", "心理", "Health & Body"),
    "Food": ("Food, cooking, restaurants, drinks, meals and eating habits.", "食・料理", "Food & Drink"),
    "Environment": ("Environment, climate change, pollution, recycling, energy, sustainability and conservation.", "環境", "Nature & Environment"),
    "Animals": ("Animals, wildlife, pets, birds, insects, animal behavior and endangered species.", "動物", "Nature & Environment"),
    "Work": ("Work, jobs, careers, employees, working hours, salaries and workplace conditions.", "仕事", "Work & Money"),
    "Business": ("Business, companies, startups, entrepreneurs, corporate management, brands and industries.", "企業・ビジネス", "Work & Money"),
    "Economy": ("Economy, money, finance, inflation, prices, taxes, trade, banking and personal savings.", "経済・お金", "Work & Money"),
    "Culture": ("Culture, customs, traditions, festivals, cultural heritage and cultural differences.", "文化", "Entertainment & Culture"),
    "Entertainment": ("Entertainment, movies, television, music, celebrities, art, video games and books.", "エンタメ・芸術", "Entertainment & Culture"),
    "History": ("History, historical events, archaeology, ancient civilizations, historical figures and artifacts.", "歴史", "Society & History"),
    "Society": ("Society, communities, population, inequality, social issues, crime, laws and public services.", "社会", "Society & History"),
    "Politics": ("Politics, elections, governments, diplomacy, international relations, conflicts and world leaders.", "政治・国際", "Society & History"),
    "Science": ("Science, scientific experiments, discoveries, physics, chemistry, biology and scientific research.", "科学", "Science & Space"),
    "Space": ("Space, astronomy, planets, stars, the universe, astronauts, rockets and space exploration.", "宇宙", "Science & Space"),
    "Lifestyle": ("Daily life, homes, housing, housework, routines, leisure and personal habits.", "生活・住まい", "Life & People"),
    "Relationships": ("Family, friendship, dating, marriage, parenting, children and personal relationships.", "家族・人間関係", "Life & People"),
    "Shopping": ("Shopping, consumer spending, retail stores, fashion, clothing, purchasing products and customer preferences.", "買い物・消費", "Life & People"),
    "Education": ("Education, schools, universities, students, teaching, studying, exams and learning.", "教育", "Learning & Language"),
    "Language": ("Languages, words, vocabulary, pronunciation, translation, linguistics and language learning.", "言語", "Learning & Language"),
    "Sports": ("Sports, athletes, competitions, football, tennis and Olympic games.", "スポーツ", "Sports & Outdoors"),
}
# Specific topics come from title keywords: name -> (pattern, label, category).
# They are added alongside the broad topics, so an article can belong to several categories.
SPECIFIC_TOPICS = {
    # Health & Body
    "Sleep": (r"sleep(?:ing|s|ers?|walking)?|asleep|insomnia|naps?|napping|bedtime|snor(?:e|es|ing)", "睡眠", "Health & Body"),
    "Smoking": (r"smoking|smokers?|tobacco|cigarettes?|vaping|vapes?|e-cigarettes?", "煙草", "Health & Body"),
    "Exercise": (r"exercis(?:e|es|ing)|fitness|workouts?|physical activity|jogging|stretching|yoga|gyms?|walking|steps a day", "運動", "Health & Body"),
    "Nutrition": (r"nutrition|nutritious|diets?|dieting|calories|calorie|obesity|obese|weight loss|healthy eating", "食生活・栄養", "Health & Body"),
    "Mental Health": (r"mental health|anxiety|anxious|depression|depressed|loneliness|lonely|stress(?:ed|ful)?|burnout", "メンタルヘルス", "Health & Body"),
    "Aging": (r"aging|ageing|longevity|live longer|living longer|lifespans?|life expectancy|centenarians?|oldest (?:man|woman|person|people)|elderly|older (?:adults|people)", "長寿・老化", "Health & Body"),
    "Diseases": (r"cancers?|diabetes|dementia|alzheimer'?s|heart (?:disease|attacks?)|strokes?|blood pressure|cholesterol", "病気", "Health & Body"),
    "Infectious Diseases": (r"covid(?:-19)?|coronavirus|pandemics?|virus(?:es)?|flu|influenza|vaccines?|vaccinat\w+|measles|infections?", "感染症", "Health & Body"),
    "Brain": (r"brains?|cognitive|intelligence quotient|iq", "脳", "Health & Body"),
    # Food & Drink
    "Coffee": (r"coffee|caffeine|espresso|cappuccino", "コーヒー", "Food & Drink"),
    "Alcohol": (r"alcohol(?:ic)?|beers?|wines?|drunk|drunken|binge drinking|hangovers?|drinking rates|drinking habits|sake|whisk(?:e)?y", "飲酒", "Food & Drink"),
    "Tea": (r"tea|teas|matcha|bubble tea|tapioca", "お茶", "Food & Drink"),
    "Japanese Food": (r"sushi|ramen|wagyu|bento|onigiri|rice balls?|udon|soba|tempura|wasabi|natto|miso|japanese (?:food|cuisine|dishes)|washoku", "和食", "Food & Drink"),
    "Restaurants": (r"restaurants?|caf[eé]s?|chefs?|michelin|diners?|eating out", "外食・レストラン", "Food & Drink"),
    "Sweets": (r"chocolates?|sweets|cand(?:y|ies)|desserts?|ice cream|cakes?|cookies|donuts?|doughnuts?|sugar|sugary", "スイーツ", "Food & Drink"),
    "Fast Food": (r"fast food|fast-food|mcdonald'?s|burgers?|hamburgers?|pizzas?|kfc|fried chicken|french fries", "ファストフード", "Food & Drink"),
    "Meat & Vegan": (r"meat|beef|pork|steaks?|vegan(?:s|ism)?|vegetarian(?:s|ism)?|plant-based|lab-grown|insects? as food|edible insects", "肉・菜食", "Food & Drink"),
    # Travel & Transport
    "Hotels": (r"hotels?|airbnb|hostels?|resorts?|inns?|ryokan|capsule hotels?", "宿泊", "Travel & Transport"),
    "Overtourism": (r"overtourism|over-tourism|tourist tax(?:es)?|too many tourists|tourists? behaving badly|bans? tourists|tourism tax", "観光公害", "Travel & Transport"),
    "Islands & Beaches": (r"islands?|beach(?:es)?|seaside", "島・ビーチ", "Travel & Transport"),
    "Landmarks": (r"landmarks?|unesco|world heritage|heritage sites?|castles?|temples?|shrines?|most beautiful|best places|eiffel tower|mount fuji|mt\.? fuji", "名所・世界遺産", "Travel & Transport"),
    "Air Travel": (r"airports?|airlines?|airplanes?|planes?|flights?|aviation|aircraft|jets?|pilots?|flight attendants?|air travel", "空の旅", "Travel & Transport"),
    "Trains": (r"trains|train (?:rides?|stations?|lines?|travel|tickets?|journeys?)|railways?|railroads?|rail|shinkansen|bullet trains?|subways?|metro|derail\w*", "鉄道", "Travel & Transport"),
    "Cars": (r"cars?|electric vehicles?|evs?|tesla|toyota|vehicles?|drivers?|driving|car owners?|traffic jams?|speed limits?", "車・EV", "Travel & Transport"),
    "Self-Driving": (r"self-driving|driverless|autonomous (?:cars?|vehicles?|buses|taxis?)|robotaxis?|robo-taxis?", "自動運転", "Travel & Transport"),
    "Bicycles": (r"bicycles?|bikes?|cycling|cyclists?|e-scooters?|scooters?", "自転車・スクーター", "Travel & Transport"),
    "Taxis & Rideshare": (r"taxis?|uber|lyft|ride-hailing|ride-sharing|rideshare", "タクシー・ライドシェア", "Travel & Transport"),
    # Tech & AI
    "Smartphones": (r"smartphones?|mobile phones?|cell phones?|iphones?|screen time|phone use|phone addiction", "スマホ", "Tech & AI"),
    "Social Media": (r"social media|tiktok|instagram|facebook|influencers?|twitter|snapchat|threads app", "SNS", "Tech & AI"),
    "Cybersecurity": (r"hack(?:ers?|ed|ing)?|cyber\w*|passwords?|data breach(?:es)?|privacy|scams?|scammers?|phishing|personal data", "ネット・セキュリティ", "Tech & AI"),
    "Robots & Drones": (r"robots?|robotic|robotics|drones?|humanoids?", "ロボット・ドローン", "Tech & AI"),
    "Big Tech": (r"apple|google|amazon|microsoft|meta|samsung|sony|nvidia|openai|elon musk", "IT企業", "Tech & AI"),
    # Work & Money
    "Remote Work": (r"remote work(?:ing|ers?)?|work(?:ing)? from home|telecommut(?:e|ing|ers?)|hybrid work(?:ing)?", "リモートワーク", "Work & Money"),
    "Pay": (r"salar(?:y|ies)|wages?|pay raises?|pay rises?|minimum wage|bonus(?:es)?|paid more|pay gap|gets? paid|earn(?:s|ings)?", "給料", "Work & Money"),
    "Work Style": (r"four-day|4-day|work-life|overtime|working hours|work hours|paid leave|days off|sick leave|vacation days|quiet quitting|side jobs?|workweek|work week", "働き方", "Work & Money"),
    "Startups": (r"startups?|start-ups?|entrepreneurs?|founders?", "起業", "Work & Money"),
    "Prices": (r"inflation|price (?:hikes?|rises?|increases?)|prices|cost of living|more expensive|cheaper|price of", "物価", "Work & Money"),
    "Wealth": (r"billionaires?|millionaires?|richest|wealthiest|wealth|rich people|lottery|bitcoin|crypto\w*|stocks?|stock market|invest(?:ing|ors?|ments?)", "富裕層・投資", "Work & Money"),
    "Taxes": (r"tax|taxes|taxed", "税金", "Work & Money"),
    # Life & People
    "Parenting": (r"parenting|parents?|children|child|kids|babies|childcare|child care|raising kids", "育児", "Life & People"),
    "Dating & Marriage": (r"dating|marriage|married|marry|divorc(?:e|ed)|weddings?|dating apps?", "恋愛・結婚", "Life & People"),
    "Fashion": (r"fashion|clothes|clothing|dress code|wardrobe|sneakers|uniforms?", "ファッション", "Life & People"),
    "Housing": (r"homes|houses?|housing|apartments?|rent|rents|akiya|tiny homes?|homeowners?|home prices|dream home", "住まい", "Life & People"),
    "Happiness": (r"happiness|happiest|happier|well-being|wellbeing|life satisfaction", "幸福", "Life & People"),
    "Stores & Online Shopping": (r"convenience stores?|supermarkets?|stores?|shops?|shopping|shoppers|online shopping|e-commerce|vending machines?|konbini", "お店・通販", "Life & People"),
    "Housework": (r"housework|household chores|chores|cleaning|laundry|tidying|declutter\w*", "家事・片付け", "Life & People"),
    "Friendship": (r"friends?|friendships?|neighbors?|neighbours?", "友人・近所", "Life & People"),
    # Entertainment & Culture
    "Movies": (r"movies?|cinema|films?|filmmakers?|hollywood|oscars", "映画", "Entertainment & Culture"),
    "Music": (r"music|songs?|singers?|concerts?|orchestras?|musicians?|k-pop|bts", "音楽", "Entertainment & Culture"),
    "Books": (r"books?|reading|libraries|library|novels?|bookstores?", "読書", "Entertainment & Culture"),
    "Gaming": (r"video games?|gaming|gamers?|nintendo|playstation|xbox|esports|e-sports", "ゲーム", "Entertainment & Culture"),
    "Anime & Manga": (r"anime|manga|ghibli|pok[eé]mon|cartoons?|animated|animation", "アニメ・漫画", "Entertainment & Culture"),
    "Art & Museums": (r"art|artists?|artworks?|museums?|paintings?|painter|exhibitions?|galler(?:y|ies)|sculptures?|banksy|picasso|van gogh", "アート・美術館", "Entertainment & Culture"),
    "Celebrities": (r"celebrit(?:y|ies)|taylor swift|beyonc[eé]|kardashians?|famous people", "有名人", "Entertainment & Culture"),
    "Streaming & TV": (r"netflix|youtube|youtubers?|streaming|tv shows?|television|tv series|dramas?|disney\+", "動画配信・テレビ", "Entertainment & Culture"),
    "Festivals & Holidays": (r"festivals?|christmas|halloween|new year'?s?|valentine'?s|easter|thanksgiving|golden week|holiday season|fireworks|cherry blossoms?|hanami", "祭り・年中行事", "Entertainment & Culture"),
    "Theme Parks": (r"disneyland|disney world|disneysea|theme parks?|amusement parks?|universal studios|roller coasters?", "テーマパーク", "Entertainment & Culture"),
    # Nature & Environment
    "Pets": (r"pets?|dogs?|cats?|kittens?|pupp(?:y|ies)", "ペット", "Nature & Environment"),
    "Climate": (r"climate|global warming|greenhouse gas(?:es)?|carbon emissions|net zero", "気候変動", "Nature & Environment"),
    "Recycling": (r"recycl(?:e|es|ed|ing)|food waste|plastic waste|zero waste|reuse|reusable|plastics?", "リサイクル・プラスチック", "Nature & Environment"),
    "Wildlife": (r"wildlife|endangered|extinct(?:ion)?|species|elephants?|pandas?|rhinos?|rhinoceros|bears?|lions?|tigers?|gorillas?|monkeys?|giraffes?|koalas?|wolves|deer|kangaroos?", "野生動物", "Nature & Environment"),
    "Sea Life": (r"whales?|sharks?|dolphins?|fish|octopus(?:es)?|turtles?|coral reefs?|seals?|jellyfish|penguins?|oceans?", "海の生き物", "Nature & Environment"),
    "Birds & Insects": (r"birds?|owls?|crows?|parrots?|eagles?|insects?|bees?|butterfl(?:y|ies)|ants|mosquito(?:es)?|spiders?", "鳥・虫", "Nature & Environment"),
    "Zoos & Aquariums": (r"zoos?|aquariums?|safari", "動物園・水族館", "Nature & Environment"),
    "Weather & Disasters": (r"heat ?waves?|heatwaves?|earthquakes?|typhoons?|floods?|flooding|wildfires?|hurricanes?|tsunamis?|droughts?|snowfall|snowstorms?|weather|temperatures?|hottest (?:year|summer|month|day)s?|volcano(?:es)?|disasters?", "天気・災害", "Nature & Environment"),
    "Energy": (r"solar|renewable|wind (?:power|farms?|turbines?)|nuclear|energy|electricity|power plants?|oil prices|oil spills?|fossil fuels?|batteries", "エネルギー", "Nature & Environment"),
    # Science & Space
    "Nobel Prize": (r"nobel", "ノーベル賞", "Science & Space"),
    "Genetics": (r"dna|genes?|genetic(?:s|ally)?|genome|cloning|cloned|stem cells?", "遺伝子", "Science & Space"),
    "Dinosaurs & Fossils": (r"dinosaurs?|fossils?|t\. rex|mammoths?|prehistoric", "恐竜・化石", "Science & Space"),
    "Moon & Planets": (r"moon|lunar|mars|martian|jupiter|saturn|venus|planets?|asteroids?|comets?|eclipses?|meteors?", "月・惑星", "Science & Space"),
    "Spaceflight": (r"astronauts?|rockets?|nasa|jaxa|spacex|space station|iss|spacecraft|space tourism|space travel|satellites?", "宇宙飛行・ロケット", "Science & Space"),
    # Society & History
    "Crime": (r"crimes?|criminals?|police|arrested|arrests?|prisons?|jail(?:ed)?|thie(?:f|ves)|theft|stolen|steals?|robber(?:y|ies)|murders?|guns?|shootings?|fraud", "犯罪・治安", "Society & History"),
    "Population": (r"population|birth ?rates?|births|fertility rates?|declining births|aging society|ageing society|shrinking", "人口・少子化", "Society & History"),
    "Gender": (r"gender|women'?s rights|equality|feminis\w+|lgbt\w*|same-sex|sexism|female (?:leaders?|workers?)", "ジェンダー", "Society & History"),
    "Elections": (r"elections?|elected|voters?|voting|votes?|presidential|campaigns?|prime ministers?", "選挙・リーダー", "Society & History"),
    "War & Conflict": (r"wars?|warfare|conflicts?|military|soldiers?|troops|invasion|missiles?|nuclear weapons?|ukraine|gaza|refugees?", "戦争・紛争・難民", "Society & History"),
    "Archaeology": (r"archaeolog\w+|ancient|ruins|mumm(?:y|ies)|tombs?|pyramids?|shipwrecks?|treasures?|roman|vikings?|samurai", "考古学・古代", "Society & History"),
    "Royals": (r"royals?|royal family|kings?|queens?|princes?|princess(?:es)?|emperors?|empress|monarch(?:s|y)?|coronation", "王室・皇室", "Society & History"),
    # Learning & Language
    "Universities": (r"universit(?:y|ies)|colleges?|degrees?|graduates?|tuition|campus(?:es)?", "大学", "Learning & Language"),
    "Exams": (r"exams?|examinations?|entrance tests?|test scores?|grades|pisa|homework|cheating", "試験・勉強", "Learning & Language"),
    "Study Abroad": (r"study(?:ing)? abroad|international students|foreign students|exchange students?", "留学", "Learning & Language"),
    "English": (r"english", "英語", "Learning & Language"),
    "Words & Slang": (r"words?|slang|dictionar(?:y|ies)|emojis?|phrases?|vocabulary|word of the year|accents?|dialects?", "言葉・新語", "Learning & Language"),
    "School Life": (r"schools?|teachers?|classrooms?|pupils|school lunch(?:es)?|school uniforms?|kindergartens?|bullying", "学校生活", "Learning & Language"),
    # Sports
    "Soccer": (r"soccer|fifa|premier league|messi|ronaldo|football clubs?|footballers?", "サッカー", "Sports & Outdoors"),
    "Olympics": (r"olympics?|olympic|olympians?|paralympics?|paralympic", "オリンピック", "Sports & Outdoors"),
    "Baseball": (r"baseball|ohtani|mlb|koshien|home runs?", "野球", "Sports & Outdoors"),
    "Tennis": (r"tennis|wimbledon|osaka naomi|naomi osaka|djokovic|nadal|federer", "テニス", "Sports & Outdoors"),
    "Marathons": (r"marathons?|runners?|ultramarathons?|half marathons?|triathlons?", "マラソン・ランニング", "Sports & Outdoors"),
    "Rugby": (r"rugby", "ラグビー", "Sports & Outdoors"),
    "Chess & Board Games": (r"chess|shogi|board games?|grandmasters?", "チェス・将棋", "Sports & Outdoors"),
    "Outdoors": (r"everest|climbers?|climbing|mountaineer\w*|skydiv\w+|surf(?:ing|ers?)|skateboard\w*|swim(?:s|mers?|ming)?", "登山・水泳・アウトドア", "Sports & Outdoors"),
}
# Titles that match a topic keyword but are about something else.
EXCLUSIONS = {
    "Pets": r"hot dogs?|dog days|cat scans?|robot dogs?",
    "Mental Health": r"lonely planet",
    "Moon & Planets": r"lonely planet",
    "Dinosaurs & Fossils": r"fossil fuels?",
    "Royals": r"burger king|queen bee|(?:king|queen) of \w+|stephen king|king kazu|princess mononoke",
    "Housing": r"(?:upper|lower|white|opera|full|haunted) house|house of|house music",
    "Trains": r"trains (?:dogs?|ai|staff|workers|people)",
    "Birds & Insects": r"spider-man|queen bee|bee'?s knees",
    "Art & Museums": r"state-of-the-art|art of",
}
REGIONS = {
    "Japan": r"japan(?:ese)?|tokyo|osaka|kyoto|hokkaido|okinawa",
    "South Korea": r"(?:south )?korea(?:n)?s?|seoul",
    "China": r"china|chinese|beijing|shanghai",
    "Asia": r"asia(?:n)?|india(?:n)?|thailand|thai|singapore|vietnam|indonesia|taiwan|philippines",
    "North America": r"america(?:n)?s?|us|usa|canada|canadian|mexico|mexican|new york|california",
    "Europe": r"europe(?:an)?|uk|britain|british|england|london|france|french|germany|german|italy|italian|spain|spanish|sweden|norway|finland",
    "Oceania": r"australia(?:n)?|new zealand",
    "Africa": r"africa(?:n)?|kenya|egypt|nigeria|morocco",
    "South America": r"brazil(?:ian)?|argentina|chile|peru|south america",
    "Middle East": r"middle east|saudi|dubai|israel|iran|turkey|turkish",
}
# Every topic, broad or specific: name -> (label, category).
ALL_TOPICS = {name: (v[1], v[2]) for name, v in {**TOPICS, **SPECIFIC_TOPICS}.items()}
AI_PATTERN = r"ai|artificial intelligence|chatgpt|chatbot|machine learning"


def matches(pattern: str, title: str) -> bool:
    return bool(re.search(r"\b(?:" + pattern + r")\b", title, re.I))


def specific_topics(title: str) -> list[str]:
    topics = [name for name, (pattern, _, _) in SPECIFIC_TOPICS.items() if matches(pattern, title)]
    for name, pattern in EXCLUSIONS.items():
        if name in topics and matches(pattern, title):
            topics.remove(name)
    return topics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("daily_news_articles.json"))
    parser.add_argument("--output", type=Path, default=Path("site/data/articles.json"))
    parser.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    parser.add_argument("--limit", type=int, help="Use a subset for development")
    parser.add_argument("--retag-only", action="store_true", help="Reuse coordinates and similar articles from the output; requires unchanged titles and model")
    args = parser.parse_args()
    import numpy as np
    import torch
    from sentence_transformers import SentenceTransformer
    from sklearn.neighbors import NearestNeighbors
    from umap import UMAP

    torch.set_num_threads(min(4, os.cpu_count() or 1))
    source = json.loads(args.input.read_text())
    source = sorted({a["url"]: a for a in source if a.get("title") and a.get("url", "").startswith("https://eikaiwa.dmm.com/app/daily-news/article/")}.values(), key=lambda a: (a.get("published_at") or "", a["url"]), reverse=True)
    if args.limit is not None:
        if args.limit < 4:
            parser.error("--limit must be at least 4")
        source = source[:args.limit]
    if len(source) < 4:
        parser.error("at least 4 valid articles are required")
    titles = [a["title"] for a in source]
    ids = [hashlib.sha256(a["url"].encode()).hexdigest()[:16] for a in source]
    existing = None
    if args.retag_only:
        if not args.output.exists():
            parser.error("--retag-only requires an existing output file")
        previous = json.loads(args.output.read_text())
        existing = {a["id"]: a for a in previous["articles"]}
        if (previous["meta"]["model"] != args.model or previous["meta"].get("embeddingInput") != "title"
                or set(existing) != set(ids) or any(existing[id]["title"] != title for id, title in zip(ids, titles))):
            parser.error("--retag-only requires the same article IDs, titles and embedding model; run a full build instead")
    cache = Path(".cache")
    cache.mkdir(exist_ok=True)
    fingerprint = hashlib.sha256(json.dumps([args.model, titles]).encode()).hexdigest()
    embeddings_path = cache / f"embeddings-{fingerprint}.npy"
    model = SentenceTransformer(args.model)
    if embeddings_path.exists():
        embeddings = np.load(embeddings_path)
    else:
        print(f"Embedding {len(titles):,} article titles", flush=True)
        embeddings = model.encode(titles, batch_size=128, normalize_embeddings=True, show_progress_bar=True)
        np.save(embeddings_path, embeddings)
    topic_names = list(TOPICS)
    topic_vectors = model.encode([v[0] for v in TOPICS.values()], normalize_embeddings=True)
    scores = embeddings @ topic_vectors.T
    if existing is not None:
        print("Preserving existing coordinates and similar articles", flush=True)
        points = np.array([[existing[id]["x"], existing[id]["y"]] for id in ids])
        similar = [existing[id]["similar"] for id in ids]
    else:
        print("Computing UMAP coordinates", flush=True)
        points = UMAP(n_components=2, n_neighbors=min(30, len(source) - 1), min_dist=0.16, metric="cosine", random_state=42).fit_transform(embeddings)
        points = (points - points.min(axis=0)) / np.maximum(np.ptp(points, axis=0), 1e-8)
        print("Finding similar articles in embedding space", flush=True)
        _, neighbors = NearestNeighbors(n_neighbors=min(7, len(source)), metric="cosine", n_jobs=4).fit(embeddings).kneighbors(embeddings)
        similar = [[ids[j] for j in row if j != i][:6] for i, row in enumerate(neighbors)]
    articles = []
    for i, article in enumerate(source):
        ranked = np.argsort(scores[i])[::-1]
        topics = [topic_names[ranked[0]]]
        if scores[i, ranked[1]] >= 0.25 and scores[i, ranked[0]] - scores[i, ranked[1]] <= 0.045:
            topics.append(topic_names[ranked[1]])
        # Preserve explicit AI tagging even when another subject dominates the title.
        if matches(AI_PATTERN, titles[i]) and "AI" not in topics:
            topics.append("AI")
        topics.extend(specific_topics(titles[i]))
        regions = [name for name, pattern in REGIONS.items() if matches(pattern, titles[i])]
        if any(region in regions for region in ("Japan", "South Korea", "China")) and "Asia" not in regions:
            regions.append("Asia")
        categories = list(dict.fromkeys(ALL_TOPICS[topic][1] for topic in topics))
        articles.append({"id": ids[i], "title": titles[i], "url": article["url"], "date": (article.get("published_at") or "")[:10], "level": article.get("level"), "categories": categories, "topics": topics, "regions": regions, "tags": list(dict.fromkeys(topics + regions)), "x": round(float(points[i, 0]), 6), "y": round(float(points[i, 1]), 6), "similar": similar[i]})
    labels = []
    # Earlier labels win when labels overlap: categories, then specific topics, then broad topics.
    for kind, name in [*(("category", n) for n in CATEGORIES), *(("topic", n) for n in [*SPECIFIC_TOPICS, *topic_names])]:
        if kind == "category":
            indices = [i for i, a in enumerate(articles) if a["categories"][0] == name]
        else:
            indices = [i for i, a in enumerate(articles) if (name in a["topics"] if name in SPECIFIC_TOPICS else a["topics"][0] == name)]
        if not indices:
            continue
        # Use a real point near the topic median, so labels remain in the cloud.
        center = np.median(points[indices], axis=0)
        index = min(indices, key=lambda i: float(np.sum((points[i] - center) ** 2)))
        labels.append({"name": name, "kind": kind, "x": articles[index]["x"], "y": articles[index]["y"], "minZoom": 0 if kind == "category" else 1.6})
    facet_topics = [{"name": n, "label": label, "category": category, "color": CATEGORIES[category][1]} for category in CATEGORIES for n, (label, parent) in ALL_TOPICS.items() if parent == category]
    payload = {"meta": {"generatedAt": datetime.now(timezone.utc).isoformat(), "model": args.model, "projection": "UMAP", "embeddingInput": "title", "tagMethod": "broad topic embedding similarity; AI/specific topic and region title rules; categories from topic parents", "count": len(articles)}, "facets": {"categories": [{"name": n, "label": label, "color": color} for n, (label, color) in CATEGORIES.items()], "topics": facet_topics, "regions": list(REGIONS)}, "labels": labels, "articles": articles}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
    temporary.replace(args.output)
    print(f"Saved {len(articles):,} articles to {args.output}")


if __name__ == "__main__":
    main()
