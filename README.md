# DMM Daily News collector

DMM Daily Newsの一覧ページに含まれるサーバー生成HTMLから、記事タイトル、レベル、公開日時、URLを抽出します。ブラウザやJavaScript実行環境は不要です。

```bash
python3 collect_daily_news.py --pretty
python3 collect_daily_news.py --min-level 5 --max-level 7 --limit 20 --pretty
python3 collect_daily_news.py --all-pages --pretty --output daily_news_articles.json
```

個人学習の範囲で、サイトに負荷をかけない頻度で実行してください。

## レッスン候補

記事本文の難しさよりも、Discussionで自分の経験や身近な日本の状況を話しやすいかを重視しています。Level 4〜8から各20件、合計100件を選んでいます。特におすすめの25件を上位に置き、26件目以降はLevel順です。

| # | 記事 | Level | ジャンル | Discussionで話しやすいポイント |
|---:|---|:---:|---|---|
| 1 | [What Makes Japanese Customer Service Unique](https://eikaiwa.dmm.com/app/daily-news/article/what-makes-japanese-customer-service-unique/CQOvTIbdEfGeoyMgtWOy6Q) | 4 | 日本文化・サービス | 日本で受けた接客や海外との違いを、身近な例で説明できる |
| 2 | [Why Tourists Love Foreign Supermarkets](https://eikaiwa.dmm.com/app/daily-news/article/why-tourists-love-foreign-supermarkets/OnFdcJgyEfGVtH8zH3DSHQ) | 7 | 旅行・買い物 | 旅行先のスーパー、日本との違い、買いたい商品について答えやすい |
| 3 | [Should Restaurants Have 'Adults Only' Areas?](https://eikaiwa.dmm.com/app/daily-news/article/should-restaurants-have-adults-only-areas/eLHRfltzEfGH3JtuE5Vfeg) | 5 | 食・社会 | レストランで重視することや、大人専用エリアへの賛否を話せる |
| 4 | [Japan's Convenience Stores Ready to Help After Disasters](https://eikaiwa.dmm.com/app/daily-news/article/japans-convenience-stores-ready-to-help-after-disasters/dk4USlCAEfGNjhczHT6-2A) | 7 | 防災・生活 | 防災の備えと普段使うコンビニを、自分の経験から具体的に話せる |
| 5 | [Japanese Workers Tired of Unwritten Office Rules](https://eikaiwa.dmm.com/app/daily-news/article/japanese-workers-tired-of-unwritten-office-rules/s2HpSpvwEfGwqc_l8OMy-g) | 6 | 仕事・日本社会 | 職場の暗黙のルールや、変えたい習慣を自分の経験から話せる |
| 6 | [How Smartphone Use Is Affecting Our Bodies](https://eikaiwa.dmm.com/app/daily-news/article/how-smartphone-use-is-affecting-our-bodies/p8ApennNEfGM5Q-NWesaPg) | 8 | 健康・テクノロジー | 毎日のスマホ利用、姿勢、利用時間を自分の習慣に結びつけられる |
| 7 | [Three 'Rules' to Help You Get a Good Sleep](https://eikaiwa.dmm.com/app/daily-news/article/three-rules-to-help-you-get-a-good-sleep/cnPUAFf_EfGquNuUAbHQpw) | 4 | 健康・生活習慣 | 睡眠時間、寝る前の習慣、よく眠る工夫をそのまま話題にできる |
| 8 | [Osaka Restaurant Adds Sushi Pizza to Its Menu](https://eikaiwa.dmm.com/app/daily-news/article/osaka-restaurant-adds-sushi-pizza-to-its-menu/GnCjwmLrEfGkX7PQPazHOg) | 5 | 食・新商品 | 食べてみたいか、好きな変わり種料理は何かを気軽に話せる |
| 9 | [S. Korean Program Rewards People for Exercise](https://eikaiwa.dmm.com/app/daily-news/article/s-korean-program-rewards-people-for-exercise/OURceJJ4EfGhfo-Z8ZmXUQ) | 6 | 健康・制度 | 運動習慣や、ご褒美があれば続けやすいかを考えられる |
| 10 | [More Clothing Brands Offering Repair Services](https://eikaiwa.dmm.com/app/daily-news/article/more-clothing-brands-offering-repair-services/9XjAopVQEfGpyTNNXjaStA) | 8 | 買い物・環境 | 服を修理するか買い替えるか、価格や環境面から意見を言える |
| 11 | [Top Tips to Reduce Your Smartphone Use](https://eikaiwa.dmm.com/app/daily-news/article/top-tips-to-reduce-your-smartphone-use/CICFOE_bEfGTsx_CvC6R_g) | 4 | 生活習慣・テクノロジー | スマホを使う時間と、実行できそうな対策について話せる |
| 12 | [Clothes Top List of Online Returns — Survey](https://eikaiwa.dmm.com/app/daily-news/article/clothes-top-list-of-online-returns-survey/DdqePmLlEfGNW1dCM5Sabw) | 5 | 買い物・生活 | 通販での失敗や返品経験、店で買う場合との違いを話せる |
| 13 | [Gen Z Adults Are Spending Their Weekends at Home](https://eikaiwa.dmm.com/app/daily-news/article/gen-z-adults-are-spending-their-weekends-at-home/HW8OGpFxEfGuHE_W1tkkiw) | 6 | 生活・世代 | 理想の週末や、外出と家で過ごす時間の好みを答えられる |
| 14 | [New Flip Phone Made to Do 'as Little as Possible'](https://eikaiwa.dmm.com/app/daily-news/article/new-flip-phone-made-to-do-as-little-as-possible/k_io6o0jEfGdQO-6wcDhdw) | 7 | テクノロジー・生活 | 多機能なスマホが本当に必要か、自分の使い方から考えられる |
| 15 | [Why Do We Get Grumpy in Hot Weather?](https://eikaiwa.dmm.com/app/daily-news/article/why-do-we-get-grumpy-in-hot-weather/VWAuanTREfGJuf9eBBU6LQ) | 8 | 健康・季節 | 暑さによる気分や行動の変化、夏の対策を実体験から答えられる |
| 16 | [What Is 'Comfort Food,' and Why Do We Love It?](https://eikaiwa.dmm.com/app/daily-news/article/what-is-comfort-food-and-why-do-we-love-it/bjzf_iR9EfGPjzsMvpCEwQ) | 4 | 食・文化 | 自分にとってのcomfort foodと、それを食べる場面を説明できる |
| 17 | [Fewer than 10,000 Bookstores Remain in Japan](https://eikaiwa.dmm.com/app/daily-news/article/fewer-than-10000-bookstores-remain-in-japan/Gqm5EGplEfGMko8qjCGmig) | 5 | 本・地域社会 | 本をどこで買うか、書店が地域に必要かを自分の習慣から話せる |
| 18 | [74% of US Consumers Have Used AI to Shop](https://eikaiwa.dmm.com/app/daily-news/article/74-of-us-consumers-have-used-ai-to-shop/3_NPoomVEfGg0JPJm6pwAw) | 6 | AI・買い物 | 買い物にAIを使いたいか、店員やレビューとの比較ができる |
| 19 | [Coffee Cup Texture May Change What You Taste](https://eikaiwa.dmm.com/app/daily-news/article/coffee-cup-texture-may-change-what-you-taste/0B6w8nS1EfGSDZfW8vCwHg) | 7 | 食・心理 | 好きな飲み物やカップへのこだわりを、日常の経験から話せる |
| 20 | [Hong Kong Restaurants Now Allow Dogs](https://eikaiwa.dmm.com/app/daily-news/article/hong-kong-restaurants-now-allow-dogs/lAtcGoDGEfGoqevVSt55Lg) | 8 | ペット・食 | ペット同伴の店を利用したいか、衛生や利便性の賛否を話せる |
| 21 | [Hotel, Airbnb, Hostel: Where to Stay on Holiday](https://eikaiwa.dmm.com/app/daily-news/article/hotel-airbnb-hostel-where-to-stay-on-holiday/SmcaCCbqEfGZoL-1li9wuQ) | 4 | 旅行・宿泊 | 宿泊先を選ぶ基準や過去の旅行経験を具体的に話せる |
| 22 | [Japan's Summer Plans Change as Costs Rise](https://eikaiwa.dmm.com/app/daily-news/article/japans-summer-plans-change-as-costs-rise/m2rqAoV2EfGKSEsTg5Wrfg) | 5 | 旅行・家計 | 物価が休日の計画に与える影響や、節約方法を話せる |
| 23 | [England to Reward People for Going for a Walk](https://eikaiwa.dmm.com/app/daily-news/article/england-to-reward-people-for-going-for-a-walk/0kGY2nyBEfGiTG827KIIqw) | 6 | 健康・制度 | よく歩くか、報酬が行動を変えるかを自分の生活から答えられる |
| 24 | [Dogs Can Read Human Emotions, Study Finds](https://eikaiwa.dmm.com/app/daily-news/article/dogs-can-read-human-emotions-study-finds/KhW_hJdREfGxKz_MlXw2Fg) | 7 | ペット・科学 | 動物との体験や、犬が人の気持ちを理解すると思うかを話せる |
| 25 | [Remote Work Making Americans Lonelier — Report](https://eikaiwa.dmm.com/app/daily-news/article/remote-work-making-americans-lonelier-report/eYFummQiEfG0zN9xEcT2HA) | 8 | 仕事・生活 | 在宅勤務の長所・短所や、同僚との交流について意見を言える |
| 26 | [40% in US Say Kids Should Learn More Languages](https://eikaiwa.dmm.com/app/daily-news/article/40-in-us-say-kids-should-learn-more-languages/Ar08SpaFEfGwbesQN0gQ2Q) | 4 | 言語・教育 | 学びたい言語や子どもの語学教育について話せる |
| 27 | [Why Good Posture Is Important](https://eikaiwa.dmm.com/app/daily-news/article/why-good-posture-is-important/eoa9mpG4EfGhQGPZSZ1yoA) | 4 | 健康・生活 | 姿勢の癖や改善方法を自分の生活から話せる |
| 28 | [The Best Ways to Politely Correct Someone](https://eikaiwa.dmm.com/app/daily-news/article/the-best-ways-to-politely-correct-someone/9gnXHIwyEfGlHS9-QbZ03g) | 4 | コミュニケーション | 間違いをどう伝えるか、実体験をもとに答えられる |
| 29 | [Many Americans Judge People by Their Phone Wallpaper](https://eikaiwa.dmm.com/app/daily-news/article/many-americans-judge-people-by-their-phone-wallpaper/h14pJoG_EfGuAD9xBgVk7w) | 4 | 心理・スマホ | 自分の壁紙や第一印象について気軽に話せる |
| 30 | [Work Makes It Hard to Be a Good Parent — Survey](https://eikaiwa.dmm.com/app/daily-news/article/work-makes-it-hard-to-be-a-good-parent-survey/_aHp0nOXEfGVhdf1p8JboQ) | 4 | 仕事・家庭 | 仕事と家庭の両立や支援策について考えられる |
| 31 | [The Best Foods to Eat Before Running](https://eikaiwa.dmm.com/app/daily-news/article/the-best-foods-to-eat-before-running/JIVlNm5AEfGRLbsXg7Jmng) | 4 | 食・運動 | 運動前の食事や普段の運動習慣を話せる |
| 32 | [40% of Older Japanese Adults Want to Work](https://eikaiwa.dmm.com/app/daily-news/article/40-of-older-japanese-adults-want-to-work/D2U6EmhrEfGoMOOFnLqK7Q) | 4 | 仕事・日本社会 | 何歳まで働きたいか、仕事の意味を話せる |
| 33 | [Expert Tips to Keep Your Home Tidy](https://eikaiwa.dmm.com/app/daily-news/article/expert-tips-to-keep-your-home-tidy/nMF6KF3bEfGsRF8N5OJnOA) | 4 | 住まい・生活 | 片付けの習慣や苦手な家事について答えやすい |
| 34 | [Why Walking Is So Good for Our Health](https://eikaiwa.dmm.com/app/daily-news/article/why-walking-is-so-good-for-our-health/QPtDeFZGEfG9vL_96zie6g) | 4 | 健康・運動 | 普段どれくらい歩くか、続ける工夫を話せる |
| 35 | [How to Find Time for Yourself When Life Is Busy](https://eikaiwa.dmm.com/app/daily-news/article/how-to-find-time-for-yourself-when-life-is-busy/YYqffk1WEfG84kfZ_mRpkQ) | 4 | 生活・心理 | 忙しい日の自分時間や優先順位について話せる |
| 36 | [What Is 'Slow Travel' and Why Should We Do It?](https://eikaiwa.dmm.com/app/daily-news/article/what-is-slow-travel-and-why-should-we-do-it/NTPiVPaVEfC3XytKdYD3dw) | 4 | 旅行 | 短い旅行と長期滞在の好みを比較できる |
| 37 | [How to Plan the Perfect Day Trip](https://eikaiwa.dmm.com/app/daily-news/article/how-to-plan-the-perfect-day-trip/AiZ27kNQEfGV2N9fEVqZwQ) | 4 | 旅行 | 理想の日帰り旅行を具体的に組み立てられる |
| 38 | [How to Avoid Stress When You Have a Deadline](https://eikaiwa.dmm.com/app/daily-news/article/how-to-avoid-stress-when-you-have-a-deadline/BSV62j2qEfGytb_3FDH3ew) | 4 | 仕事・心理 | 締切への対処法や自分の仕事の進め方を話せる |
| 39 | [A 'Boring' Routine Could Be Good for Your Health](https://eikaiwa.dmm.com/app/daily-news/article/a-boring-routine-could-be-good-for-your-health/XTQhNDggEfGy0KNjP3B99w) | 4 | 健康・生活習慣 | 毎日のルーティンと退屈の価値を話せる |
| 40 | [How to Start Exercising and Make It a Habit](https://eikaiwa.dmm.com/app/daily-news/article/how-to-start-exercising-and-make-it-a-habit/D4mJsDHbEfGliX9MeXQA6Q) | 4 | 健康・運動 | 始めやすい運動と習慣化の工夫を答えられる |
| 41 | [Driverless Taxis Are Coming to European Cities](https://eikaiwa.dmm.com/app/daily-news/article/driverless-taxis-are-coming-to-european-cities/33kq5pwkEfGS4I-inJGX6A) | 5 | 交通・テクノロジー | 無人タクシーに乗りたいか、安全性も含め話せる |
| 42 | [Ticket Prices Rising at Japan's Amusement Parks](https://eikaiwa.dmm.com/app/daily-news/article/ticket-prices-rising-at-japans-amusement-parks/7m8aYpVMEfGOA5f8OMEm1A) | 5 | 娯楽・家計 | 遊園地に払える金額や値上げへの考えを話せる |
| 43 | [1 in 4 Japanese Think AI Will Replace Friends](https://eikaiwa.dmm.com/app/daily-news/article/1-in-4-japanese-think-ai-will-replace-friends/tuPQ6JBLEfGyX7PO0WcTOg) | 5 | AI・人間関係 | AIが友人になれるか、自分の価値観で答えられる |
| 44 | [Japan's Paternity Leave Rate Topped 50% in 2025](https://eikaiwa.dmm.com/app/daily-news/article/japans-paternity-leave-rate-topped-50-in-2025/-HcesJABEfGAPnNXsZZjXg) | 5 | 仕事・家庭 | 育休の取りやすさや職場の支援について話せる |
| 45 | [Japan's Food Waste Falls to Record Low](https://eikaiwa.dmm.com/app/daily-news/article/japans-food-waste-falls-to-record-low/3ardwHbEEfGrTGebcGpFYw) | 5 | 食・環境 | 家庭で食品を捨てない工夫を具体的に話せる |
| 46 | [The Ideal Movie Length Is 88 Minutes — Survey](https://eikaiwa.dmm.com/app/daily-news/article/the-ideal-movie-length-is-88-minutes-survey/1N3EUnx2EfGN-jMm4Eo_fA) | 5 | 映画・娯楽 | 好きな映画の長さや集中できる時間を話せる |
| 47 | [US Remote Work Increased in 2025](https://eikaiwa.dmm.com/app/daily-news/article/us-remote-work-increased-in-2025/e-kRoHmVEfG_X3em4ZTl4g) | 5 | 仕事・生活 | 在宅勤務と出社のどちらが合うか比較できる |
| 48 | [New Sleeper Train Connects Tokyo to Aomori](https://eikaiwa.dmm.com/app/daily-news/article/new-sleeper-train-connects-tokyo-to-aomori/6OdSqmmPEfGC9usLg9r5qw) | 5 | 旅行・鉄道 | 寝台列車に乗りたいか、移動手段の好みを話せる |
| 49 | [The Mistakes Travelers Make When Visiting Japan](https://eikaiwa.dmm.com/app/daily-news/article/the-mistakes-travelers-make-when-visiting-japan/Whg9WGDbEfGAkT9i9gOiLw) | 5 | 旅行・日本文化 | 外国人旅行者への助言を日本の経験から話せる |
| 50 | [Survey Finds Japan's Most Popular Pet Names](https://eikaiwa.dmm.com/app/daily-news/article/survey-finds-japans-most-popular-pet-names/2LYeGkNeEe--lWu54OZ3tA) | 5 | ペット・文化 | ペットの名前や名付け方について気軽に答えられる |
| 51 | [Many Americans Choose Sleep over Plans with Friends](https://eikaiwa.dmm.com/app/daily-news/article/many-americans-choose-sleep-over-plans-with-friends/X6HU5l6hEfGAUAvF17libg) | 5 | 生活・人間関係 | 睡眠と友人との予定のどちらを優先するか話せる |
| 52 | [Lawson Opens New 'Mini-Supermarkets'](https://eikaiwa.dmm.com/app/daily-news/article/lawson-opens-new-mini-supermarkets/ORA2Cl2eEfGh1Gt0oqDaBw) | 5 | 買い物・生活 | コンビニとスーパーの使い分けを説明できる |
| 53 | [Japan Will Soon Have a Pokemon-Themed Airport](https://eikaiwa.dmm.com/app/daily-news/article/japan-will-soon-have-a-pokemon-themed-airport/I5VAlFOuEfGr7iNfU7WMew) | 5 | 旅行・娯楽 | テーマ空港を利用したいか、好きな作品も話せる |
| 54 | [Japanese Prefecture to Pay People to Use Dating Apps](https://eikaiwa.dmm.com/app/daily-news/article/japanese-prefecture-to-pay-people-to-use-dating-apps/Hq3MHET_EfGkTVdkSE-iUA) | 5 | 恋愛・制度 | 自治体の婚活支援やアプリへの賛否を話せる |
| 55 | [Why MP3 Players Are Making a Comeback](https://eikaiwa.dmm.com/app/daily-news/article/why-mp3-players-are-making-a-comeback/urEjbDrREfGboe_DnO1TTg) | 5 | 音楽・テクノロジー | 音楽を聴く機器やスマホとの違いを話せる |
| 56 | [South Korea, US Are Japan's Top Fashion Influences](https://eikaiwa.dmm.com/app/daily-news/article/south-korea-us-are-japans-top-fashion-influences/nVUclJsZEfG40r-t8yJDYg) | 6 | ファッション・文化 | 服選びや海外から受ける影響について話せる |
| 57 | [Laptops Now More Important for Students than Books](https://eikaiwa.dmm.com/app/daily-news/article/laptops-now-more-important-for-students-than-books/62LRiJseEfG17QNeO8ErFw) | 6 | 教育・テクノロジー | 紙とパソコンのどちらで学びやすいか比較できる |
| 58 | [Japanese People Spend Less Time and Money on Leisure](https://eikaiwa.dmm.com/app/daily-news/article/japanese-people-spend-less-time-and-money-on-leisure/nGRelpqpEfGGf_OWMu3UBg) | 6 | 娯楽・家計 | 余暇の過ごし方や趣味への出費を話せる |
| 59 | [Most US Families Have One Parent in Charge of Dinner](https://eikaiwa.dmm.com/app/daily-news/article/most-us-families-have-one-parent-in-charge-of-dinner/_Pb9WpaiEfG89ueiII8Bhw) | 6 | 食・家庭 | 家庭で誰が料理するか、役割分担を話せる |
| 60 | [Which Workers Feel the Most Stress?](https://eikaiwa.dmm.com/app/daily-news/article/which-workers-feel-the-most-stress/aqqFFJc1EfGqIuOW521luw) | 6 | 仕事・健康 | 仕事のストレス要因と解消法を話せる |
| 61 | [Japanese Choosing 'Coolcations' for Summer Trips](https://eikaiwa.dmm.com/app/daily-news/article/japanese-choosing-coolcations-for-summer-trips/mESeWpYUEfGijadPgGYgHA) | 6 | 旅行・季節 | 暑い時期にどこへ旅行したいか答えられる |
| 62 | [Robot Chef Cooks Noodles in Just 90 Seconds](https://eikaiwa.dmm.com/app/daily-news/article/robot-chef-cooks-noodles-in-just-90-seconds/KJqy1JVQEfGF01cAUoqZeA) | 6 | 食・ロボット | ロボット料理を食べたいか、店での役割を話せる |
| 63 | [Wobbly Beer Glass Forces You to Drink Water](https://eikaiwa.dmm.com/app/daily-news/article/wobbly-beer-glass-forces-you-to-drink-water/ca8y6JX-EfGzxMdwj23Mvw) | 6 | 飲み物・アイデア商品 | 行動を変える商品が有効か楽しく議論できる |
| 64 | [Would You Say 'I Do' to These Unusual Wedding Traditions?](https://eikaiwa.dmm.com/app/daily-news/article/would-you-say-i-do-to-these-unusual-wedding-traditions/ilh0tl7bEe2DGZOuFcnsAw) | 6 | 文化・結婚 | 結婚式の習慣や好みを各国と比較できる |
| 65 | [Many Japanese Workers Consider Quitting Their Jobs](https://eikaiwa.dmm.com/app/daily-news/article/many-japanese-workers-consider-quitting-their-jobs/JBzARI8GEfGU_kPq34g3iA) | 6 | 仕事・日本社会 | 仕事を辞める理由や良い職場の条件を話せる |
| 66 | [Timing of Meals May Affect Brain Health](https://eikaiwa.dmm.com/app/daily-news/article/timing-of-meals-may-affect-brain-health/WKNPlIxfEfG6vdN1CFbl9Q) | 6 | 食・健康 | 食事の時間や生活リズムを振り返って話せる |
| 67 | [City Hall in Japan Lets Staff Wear T-Shirts](https://eikaiwa.dmm.com/app/daily-news/article/city-hall-in-japan-lets-staff-wear-t-shirts/8EzAKIY9EfGgyG_RHvKOSg) | 6 | 仕事・服装 | 職場の服装ルールや快適さについて話せる |
| 68 | [Working from Home May Increase Obesity Risk](https://eikaiwa.dmm.com/app/daily-news/article/working-from-home-may-increase-obesity-risk/gVp-PIPoEfGwVTP9B-YQXw) | 6 | 仕事・健康 | 在宅勤務中の運動や食生活について話せる |
| 69 | [Japanese Workers Pay Services to Ask for Leave](https://eikaiwa.dmm.com/app/daily-news/article/japanese-workers-pay-services-to-ask-for-leave/gW_SBIRhEfGTL5czH0GjzQ) | 6 | 仕事・文化 | 休みを頼みやすい職場とは何かを考えられる |
| 70 | [Read, Don't Talk: What Are Silent Reading Clubs?](https://eikaiwa.dmm.com/app/daily-news/article/read-dont-talk-what-are-silent-reading-clubs/50eetm_IEfGRo1unW0a3pA) | 6 | 本・コミュニティ | 読書会に参加したいか、読書習慣を話せる |
| 71 | ['FIRE' Movement Helps People Retire Early](https://eikaiwa.dmm.com/app/daily-news/article/fire-movement-helps-people-retire-early/ehAqxp0DEfGN33vEy60xtw) | 7 | 仕事・お金 | 節約や理想の退職年齢を価値観に結びつけられる |
| 72 | [Having a Sweet Tooth Linked to Safer Choices](https://eikaiwa.dmm.com/app/daily-news/article/having-a-sweet-tooth-linked-to-safer-choices/jtzwfpg_EfGY4otNip5-Uw) | 7 | 食・心理 | 甘い物の好みと性格が関係するか話せる |
| 73 | [Feeding by Tourists Puts Japan's Rabbit Island at Risk](https://eikaiwa.dmm.com/app/daily-news/article/feeding-by-tourists-puts-japans-rabbit-island-at-risk/Cs_mFpwIEfGWDBPjCJBZEw) | 7 | 観光・動物 | 観光客のルールと動物保護について意見を言える |
| 74 | [Amazon Expands Its Drone Delivery Service](https://eikaiwa.dmm.com/app/daily-news/article/amazon-expands-its-drone-delivery-service/BxsyGJxoEfGdiCMF5ejv7Q) | 7 | 買い物・テクノロジー | ドローン配送を利用したいか、利点と不安を話せる |
| 75 | [Constantly Searching for Meaning Could Cause Burnout](https://eikaiwa.dmm.com/app/daily-news/article/constantly-searching-for-meaning-could-cause-burnout/fA1QWpaIEfGpSYeBCqM8-g) | 7 | 仕事・心理 | 仕事の意味と燃え尽きについて自分の考えを話せる |
| 76 | [Five Things Happy Countries Have in Common](https://eikaiwa.dmm.com/app/daily-news/article/five-things-happy-countries-have-in-common/vNOrupWjEfG5kyu-hDueBg) | 7 | 社会・幸福 | 幸せな国の条件や日本の良い点を考えられる |
| 77 | [Airline to Charge Passengers to Use Overhead Lockers](https://eikaiwa.dmm.com/app/daily-news/article/airline-to-charge-passengers-to-use-overhead-lockers/w__-KJGVEfGuDQuKR7becA) | 7 | 旅行・料金 | 飛行機の追加料金にどこまで払えるか話せる |
| 78 | [How to Make Time for 'Deep Work'](https://eikaiwa.dmm.com/app/daily-news/article/how-to-make-time-for-deep-work/3E1LiLRHEfCW3G8Ni9xBrQ) | 7 | 仕事・集中 | 集中を妨げるものや自分の仕事環境を話せる |
| 79 | [Is Social Media Ruining the Joy of Travel?](https://eikaiwa.dmm.com/app/daily-news/article/is-social-media-ruining-the-joy-of-travel/s0qbFoaBEfGwjKvz0gA7Ag) | 7 | 旅行・SNS | 旅行中の投稿や写真の撮り方について話せる |
| 80 | [Just 10 Minutes of Forest Birdsong May Relieve Stress](https://eikaiwa.dmm.com/app/daily-news/article/just-10-minutes-of-forest-birdsong-may-relieve-stress/Rf_CbItdEfGL1GeF-PY5dw) | 7 | 自然・健康 | 好きな自然の音やストレス解消法を話せる |
| 81 | [Older Tokyo Residents Increasingly Enjoy Time Alone](https://eikaiwa.dmm.com/app/daily-news/article/older-tokyo-residents-increasingly-enjoy-time-alone/3vbiSonpEfGnwK9bSkDzJA) | 7 | 生活・社会 | 一人時間の楽しみ方や孤独との違いを話せる |
| 82 | [Why Forgetting Your Phone Might Help Your Memory](https://eikaiwa.dmm.com/app/daily-news/article/why-forgetting-your-phone-might-help-your-memory/JUz38InxEfG_b69PXi9CQg) | 7 | スマホ・健康 | スマホなしで過ごせるか、記憶への影響を考えられる |
| 83 | [Monitoring Employees Doesn't Improve Performance](https://eikaiwa.dmm.com/app/daily-news/article/monitoring-employees-doesnt-improve-performance/tKLQ8IbvEfG5unMzjAnsew) | 7 | 仕事・管理 | 職場での監視と信頼のどちらが有効か話せる |
| 84 | [From Practical to Fashionable: Casio's 'Cheap Watches'](https://eikaiwa.dmm.com/app/daily-news/article/from-practical-to-fashionable-casios-cheap-watches/yK-MEH6_EfG0Fg_bxs9Plw) | 7 | ファッション・商品 | 腕時計を使うか、安い商品の魅力を話せる |
| 85 | [Saving Money Is Easier with Goals — US Survey](https://eikaiwa.dmm.com/app/daily-news/article/saving-money-is-easier-with-goals-us-survey/wnmPkG_cEfGqX6f0IzXWng) | 7 | お金・生活 | 貯金の目的や続ける工夫を具体的に話せる |
| 86 | [Some US Colleges Now Offer 'Influencer' Degrees](https://eikaiwa.dmm.com/app/daily-news/article/some-us-colleges-now-offer-influencer-degrees/_7zrnJe8EfGCpsvFKz2b0A) | 8 | 教育・SNS | インフルエンサーに大学教育が必要か話せる |
| 87 | [AI Uptake Remains Slow in Japan](https://eikaiwa.dmm.com/app/daily-news/article/ai-uptake-remains-slow-in-japan/MyhazpgsEfGjCWfqbre3qQ) | 8 | AI・仕事 | 日本でAI利用が遅い理由や自分の利用法を話せる |
| 88 | [Kellogg to Remove Artificial Colors from Its Cereals](https://eikaiwa.dmm.com/app/daily-news/article/kellogg-to-remove-artificial-colors-from-its-cereals/3TrHEpJbEfGdNe8mtIXc9w) | 8 | 食・健康 | 食品の色と安全性のどちらを重視するか話せる |
| 89 | [Cage-Free Eggs May Have Worse Environmental Impact](https://eikaiwa.dmm.com/app/daily-news/article/cage-free-eggs-may-have-worse-environmental-impact/EZ9M4JEHEfGjW8PkL2mQZA) | 8 | 食・環境 | 動物福祉と環境負荷の優先順位を考えられる |
| 90 | [Research Finds Risks of Eating Too Much Protein](https://eikaiwa.dmm.com/app/daily-news/article/research-finds-risks-of-eating-too-much-protein/YC2PlJEVEfGIkde5LDymJA) | 8 | 食・健康 | 普段の食事や健康情報との付き合い方を話せる |
| 91 | [Food Tax Cut Approved by Japanese Cabinet](https://eikaiwa.dmm.com/app/daily-news/article/food-tax-cut-approved-by-japanese-cabinet/57jHmpInEfGjSL-MIO2eEg) | 8 | 食・経済 | 食料品の税金や家計への影響について話せる |
| 92 | [Coffee May Protect Your Heart — Energy Drinks Don't](https://eikaiwa.dmm.com/app/daily-news/article/coffee-may-protect-your-heart-energy-drinks-dont/ikLqrIupEfGM2otz6tj-vQ) | 8 | 飲み物・健康 | コーヒーとエナジードリンクの習慣を比較できる |
| 93 | [Your Birth Order May Affect Your Health](https://eikaiwa.dmm.com/app/daily-news/article/your-birth-order-may-affect-your-health/j3B1EpWzEfG5w39X3gK_Jw) | 8 | 家族・健康 | 兄弟姉妹での立場や性格の違いを話せる |
| 94 | [Ultrarare Nintendo Cartridges Found After Years in Storage](https://eikaiwa.dmm.com/app/daily-news/article/ultrarare-nintendo-cartridges-found-after-years-in-storage/p8co0JrSEfGjUY98Ukdi6A) | 8 | ゲーム・収集 | 古いゲームやコレクションの価値について話せる |
| 95 | [United Airlines Announces New Empty Middle Seat Row](https://eikaiwa.dmm.com/app/daily-news/article/united-airlines-announces-new-empty-middle-seat-row/5Pq6FoEcEfG1_kslPNfZqA) | 8 | 旅行・サービス | 快適な座席に追加料金を払うか考えられる |
| 96 | [Algorithms May Be Making Your Media Consumption Boring](https://eikaiwa.dmm.com/app/daily-news/article/algorithms-may-be-making-your-media-consumption-boring/WhO3bGA0EfGQNAsu98pCvA) | 8 | メディア・AI | おすすめ機能で選択肢が狭まるか話せる |
| 97 | [Mexico Passes Bill to Cut Workweek to 40 Hours](https://eikaiwa.dmm.com/app/daily-news/article/mexico-passes-bill-to-cut-workweek-to-40-hours/VSNrFGTsEfGV9MftrLIubQ) | 8 | 仕事・制度 | 理想の労働時間と生産性について話せる |
| 98 | [Money Influencers' Advice Is Poor, But Users Still Listen](https://eikaiwa.dmm.com/app/daily-news/article/money-influencers-advice-is-poor-but-users-still-listen/BJq-flh5EfGIOFNfiNulgQ) | 8 | お金・SNS | ネットの金融情報をどこまで信用するか話せる |
| 99 | [Could 'Ikigai' Help You Find Happiness?](https://eikaiwa.dmm.com/app/daily-news/article/could-ikigai-help-you-find-happiness/qqEcnn-zEeyDyy_GFWhtVg) | 8 | 日本文化・幸福 | 生きがいや日々の満足について自分の言葉で話せる |
| 100 | [How Notifications Hurt Your Concentration](https://eikaiwa.dmm.com/app/daily-news/article/how-notifications-hurt-your-concentration/2gBv9Ce6EfG7QQ_dbT_vxw) | 8 | スマホ・集中 | 通知を切るか、集中を守る方法を話せる |

最初に選ぶなら `Japanese Customer Service` → `Foreign Supermarkets` → `Adults Only Restaurants` の順がおすすめです。Level 8に挑戦するなら `Smartphone Use` が第一候補です。

### 選定基準

- Level 4〜8を各20件にし、難易度が一部に偏らないようにする
- コンビニ、買い物、スマホ、食事、仕事、旅行、防災など、日常と接点がある題材を優先する
- 専門知識がなくても、自分の経験、日本との比較、賛否と理由で答えられるDiscussionを選ぶ
- 本文が多少難しくても、Discussionの質問を読んだときに具体例を思いつける記事は候補に含める
- 過去に良かった記事は好みを判断する一例として使い、その記事自体を優先する理由にはしない
