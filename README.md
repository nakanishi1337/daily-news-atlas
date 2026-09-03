# DMM Daily News collector

DMM Daily Newsの一覧ページに含まれるサーバー生成HTMLから、記事タイトル、レベル、公開日時、URLを抽出します。ブラウザやJavaScript実行環境は不要です。

```bash
python3 collect_daily_news.py --pretty
python3 collect_daily_news.py --min-level 5 --max-level 7 --limit 20 --pretty
python3 collect_daily_news.py --all-pages --pretty --output daily_news_articles.json
```

個人学習の範囲で、サイトに負荷をかけない頻度で実行してください。

## レッスン候補

記事本文の難しさよりも、Discussionで自分の経験や身近な日本の状況を話しやすいかを重視しています。Level 4〜8から各5件を選び、上からおすすめ順に並べています。

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

最初に選ぶなら `Japanese Customer Service` → `Foreign Supermarkets` → `Adults Only Restaurants` の順がおすすめです。Level 8に挑戦するなら `Smartphone Use` が第一候補です。

### 選定基準

- Level 4〜8を同数にし、難易度が一部に偏らないようにする
- コンビニ、買い物、スマホ、食事、仕事、旅行、防災など、日常と接点がある題材を優先する
- 専門知識がなくても、自分の経験、日本との比較、賛否と理由で答えられるDiscussionを選ぶ
- 本文が多少難しくても、Discussionの質問を読んだときに具体例を思いつける記事は候補に含める
- 過去に良かった記事は好みを判断する一例として使い、その記事自体を優先する理由にはしない
