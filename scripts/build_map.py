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

TOPICS = {
    "Travel": ("Travel, tourism, vacation destinations, hotels, tourists and sightseeing.", "旅行", "#328e9c"),
    "Transportation": ("Transportation, commuting, traffic, trains, cars, aviation, airlines and public transport.", "交通", "#5393ac"),
    "Technology": ("Technology, computers, smartphones, software, digital products, gadgets and the internet.", "テクノロジー", "#787bc5"),
    "AI": ("Artificial intelligence, generative AI, ChatGPT, chatbots, machine learning and AI applications.", "AI", "#9068b2"),
    "Health": ("Health, medicine, diseases, medical treatments, nutrition, sleep and physical fitness.", "健康・医療", "#cf8275"),
    "Psychology": ("Psychology, emotions, happiness, personality, mental health, stress and human behavior.", "心理", "#bd87a5"),
    "Food": ("Food, cooking, restaurants, drinks, meals and eating habits.", "食・料理", "#d6a04d"),
    "Environment": ("Environment, climate change, pollution, recycling, energy, sustainability and conservation.", "環境", "#6c9b70"),
    "Animals": ("Animals, wildlife, pets, birds, insects, animal behavior and endangered species.", "動物", "#91a95d"),
    "Work": ("Work, jobs, careers, employees, working hours, salaries and workplace conditions.", "仕事", "#648bbd"),
    "Business": ("Business, companies, startups, entrepreneurs, corporate management, brands and industries.", "企業・ビジネス", "#647a9b"),
    "Economy": ("Economy, money, finance, inflation, prices, taxes, trade, banking and personal savings.", "経済・お金", "#b59c55"),
    "Culture": ("Culture, customs, traditions, festivals, cultural heritage and cultural differences.", "文化", "#b789b2"),
    "Entertainment": ("Entertainment, movies, television, music, celebrities, art, video games and books.", "エンタメ・芸術", "#a17fc0"),
    "History": ("History, historical events, archaeology, ancient civilizations, historical figures and artifacts.", "歴史", "#aa8a68"),
    "Society": ("Society, communities, population, inequality, social issues, crime, laws and public services.", "社会", "#859aab"),
    "Politics": ("Politics, elections, governments, diplomacy, international relations, conflicts and world leaders.", "政治・国際", "#8a849f"),
    "Science": ("Science, scientific experiments, discoveries, physics, chemistry, biology and scientific research.", "科学", "#79aaa3"),
    "Space": ("Space, astronomy, planets, stars, the universe, astronauts, rockets and space exploration.", "宇宙", "#767ba6"),
    "Lifestyle": ("Daily life, homes, housing, housework, routines, leisure and personal habits.", "生活・住まい", "#b79973"),
    "Relationships": ("Family, friendship, dating, marriage, parenting, children and personal relationships.", "家族・人間関係", "#c68f99"),
    "Shopping": ("Shopping, consumer spending, retail stores, fashion, clothing, purchasing products and customer preferences.", "買い物・消費", "#c19b78"),
    "Education": ("Education, schools, universities, students, teaching, studying, exams and learning.", "教育", "#8c9c56"),
    "Language": ("Languages, words, vocabulary, pronunciation, translation, linguistics and language learning.", "言語", "#6f9d89"),
    "Sports": ("Sports, athletes, competitions, football, tennis and Olympic games.", "スポーツ", "#ba8474"),
}
# These are independent labels, not children of the broader topics above.
SPECIFIC_TOPICS = {
    "Sleep": (r"sleep(?:ing|s|ers?|walking)?|asleep|insomnia|naps?|napping|bedtime|snor(?:e|es|ing)", "睡眠", "#cf8275"),
    "Smoking": (r"smoking|smokers?|tobacco|cigarettes?|vaping|vapes?|e-cigarettes?", "煙草", "#b58a76"),
    "Alcohol": (r"alcohol(?:ic)?|beers?|wines?|drunk|drunken|binge drinking|hangovers?|drinking rates|drinking habits", "飲酒", "#bc956b"),
    "Coffee": (r"coffee|caffeine|espresso|cappuccino", "コーヒー", "#a48a68"),
    "Exercise": (r"exercis(?:e|es|ing)|fitness|workouts?|physical activity|jogging|stretching", "運動", "#c28e79"),
    "Nutrition": (r"nutrition|nutritious|diets?|dieting|calories|calorie|obesity|obese|weight loss|healthy eating", "食生活・栄養", "#c8a168"),
    "Mental Health": (r"mental health|anxiety|anxious|depression|depressed|loneliness|lonely|stress(?:ed|ful)?|burnout", "メンタルヘルス", "#bd87a5"),
    "Pets": (r"pets?|dogs?|cats?|kittens?|pupp(?:y|ies)", "ペット", "#91a95d"),
    "Parenting": (r"parenting|parents?|children|child|kids|babies|childcare|child care|raising kids", "育児", "#c68f99"),
    "Dating & Marriage": (r"dating|marriage|married|marry|divorc(?:e|ed)|weddings?|dating apps?", "恋愛・結婚", "#bf869e"),
    "Social Media": (r"social media|tiktok|instagram|facebook|influencers?|twitter", "SNS", "#9390be"),
    "Smartphones": (r"smartphones?|mobile phones?|cell phones?|iphones?|screen time|phone use|phone addiction", "スマホ", "#858cc0"),
    "Gaming": (r"video games?|gaming|gamers?|nintendo|playstation|xbox", "ゲーム", "#a17fc0"),
    "Movies": (r"movies?|cinema|films?|filmmakers?|hollywood|oscars", "映画", "#b18cab"),
    "Music": (r"music|songs?|singers?|concerts?|orchestras?|musicians?", "音楽", "#b789b2"),
    "Books": (r"books?|reading|libraries|library|novels?", "読書", "#8c9c56"),
    "Fashion": (r"fashion|clothes|clothing|dress code|wardrobe", "ファッション", "#c19b78"),
    "Climate": (r"climate|global warming|greenhouse gas(?:es)?|carbon emissions|net zero", "気候変動", "#6c9b70"),
    "Recycling": (r"recycl(?:e|es|ed|ing)|food waste|plastic waste|zero waste|reuse|reusable", "リサイクル", "#7e9d74"),
    "Remote Work": (r"remote work(?:ing|ers?)?|work(?:ing)? from home|telecommut(?:e|ing|ers?)|hybrid work(?:ing)?", "リモートワーク", "#648bbd"),
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
AI_PATTERN = r"ai|artificial intelligence|chatgpt|chatbot|machine learning"


def matches(pattern: str, title: str) -> bool:
    return bool(re.search(r"\b(?:" + pattern + r")\b", title, re.I))


def specific_topics(title: str) -> list[str]:
    topics = [name for name, (pattern, _, _) in SPECIFIC_TOPICS.items() if matches(pattern, title)]
    if "Pets" in topics and matches(r"hot dogs?|dog days|cat scans?", title):
        topics.remove("Pets")
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
        articles.append({"id": ids[i], "title": titles[i], "url": article["url"], "date": (article.get("published_at") or "")[:10], "level": article.get("level"), "topics": topics, "regions": regions, "tags": list(dict.fromkeys(topics + regions)), "x": round(float(points[i, 0]), 6), "y": round(float(points[i, 1]), 6), "similar": similar[i]})
    labels = []
    for name in [*SPECIFIC_TOPICS, *topic_names]:
        specific = name in SPECIFIC_TOPICS
        indices = [i for i, a in enumerate(articles) if (name in a["topics"] if specific else a["topics"][0] == name)]
        if not indices:
            continue
        # Use a real point near the topic median, so labels remain in the cloud.
        center = np.median(points[indices], axis=0)
        index = min(indices, key=lambda i: float(np.sum((points[i] - center) ** 2)))
        labels.append({"topic": name, "x": articles[index]["x"], "y": articles[index]["y"], "minZoom": 1.6 if specific else 0})
    all_topics = {**SPECIFIC_TOPICS, **TOPICS}
    payload = {"meta": {"generatedAt": datetime.now(timezone.utc).isoformat(), "model": args.model, "projection": "UMAP", "embeddingInput": "title", "tagMethod": "broad topic embedding similarity; AI/specific topic and region title rules", "count": len(articles)}, "facets": {"topics": [{"name": n, "label": v[1], "color": v[2]} for n, v in all_topics.items()], "regions": list(REGIONS)}, "labels": labels, "articles": articles}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
    temporary.replace(args.output)
    print(f"Saved {len(articles):,} articles to {args.output}")


if __name__ == "__main__":
    main()
