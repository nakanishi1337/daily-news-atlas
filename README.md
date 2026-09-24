# DMM Daily News collector

DMM Daily Newsの一覧ページに含まれるサーバー生成HTMLから、記事タイトル、レベル、公開日時、URLを抽出します。ブラウザやJavaScript実行環境は不要です。

```bash
python3 collect_daily_news.py --pretty
python3 collect_daily_news.py --min-level 5 --max-level 7 --limit 20 --pretty
python3 collect_daily_news.py --all-pages --pretty --output daily_news_articles.json
```

個人学習の範囲で、サイトに負荷をかけない頻度で実行してください。

## レッスン候補

**今の生活・習慣・身の回りの事実を、そのまま説明して会話が成り立つこと**を最優先にしています。「何を・いつ・どこで・どのくらい・どうやって」に答えられる題材を選び、思い出や特別なエピソードを探す質問、理由や賛否を組み立てる質問の優先度を下げています。

部活動、高級みかん、睡眠、iPhone、ソウル観光、シーツ交換、キムチ、職場の服装、二日酔い、夕食の分担という既読10記事は、話題の幅の参考にしています。その10記事自体は候補から外しています。

Level 4〜8から各20件、合計100件。最初の25件は、普段の事実だけで答え始めやすい題材をジャンルが偏らないように配置し、26件目以降はLevel順です。

2026年9月24日更新。新着一覧の先頭8ページを取得して保存済みの [記事一覧](daily_news_articles.json) に統合し、候補24件を入れ替えました（保存データの最新公開日時：2026年9月23日 UTC）。以下はタイトルをもとに作った会話案で、**実際のDiscussionにこうした質問が多いことを確認した一覧ではありません**。記事を選ぶ際は実際の設問も確認してください。金額・頻度はおおよそでよく、「使わない」「特にない」も答えになります。

| # | 記事 | Level | ジャンル | 事実だけで答え始められる質問例（独自の会話案） |
|---:|---|:---:|---|---|
| 1 | [Japan's Vending Machines to Sell Canned Hot Pot](https://eikaiwa.dmm.com/app/daily-news/article/japans-vending-machines-to-sell-canned-hot-pot/fS6aCLKsEfGwi_unK9nc2g) | 5 | 食・自動販売機 | 自動販売機では何を買う？／家や職場の近くにはどんな自販機がある？ |
| 2 | [Japan's Favorite Rice Dish Is Chahan — Survey](https://eikaiwa.dmm.com/app/daily-news/article/japans-favorite-rice-dish-is-chahan-survey/k000equfEfGD94v_xkd6eQ) | 4 | 食事・料理 | チャーハンは家で作る？／普段はどんな具を入れる？ |
| 3 | [Average American Rates Their Home 7.5 Out of 10](https://eikaiwa.dmm.com/app/daily-news/article/average-american-rates-their-home-75-out-of-10/9Oms8Kh5EfGossdUvX6YgQ) | 4 | 住まい・生活 | 今の家には何部屋ある？／普段どの部屋で過ごす？ |
| 4 | [Save Time with These Meal-Prepping Tips](https://eikaiwa.dmm.com/app/daily-news/article/save-time-with-these-meal-prepping-tips/DpUyPjq9Ee2OZGsIAi1KoA) | 6 | 料理・家事 | 作り置きはする？／何日分を作る？／冷蔵と冷凍のどちらで保存する？ |
| 5 | [FamilyMart Introduces New Dress Code for Workers](https://eikaiwa.dmm.com/app/daily-news/article/familymart-introduces-new-dress-code-for-workers/Rl1l7KMPEfGHM7MtT-tpVQ) | 6 | 仕事・服装 | 仕事中はどんな服を着る？／制服はある？／靴に決まりはある？ |
| 6 | [Americans' Top Priority When Buying Clothes? Price!](https://eikaiwa.dmm.com/app/daily-news/article/americans-top-priority-when-buying-clothes-price/ecpiLrETEfGOr-Poab5dSg) | 5 | 買い物・衣服 | 服はどこで買う？／一着にいくらくらい使う？／セールを利用する？ |
| 7 | [Lego Creates Sony PlayStation Set](https://eikaiwa.dmm.com/app/daily-news/article/lego-creates-sony-playstation-set/TagxCKhJEfGi4reZXjEQEw) | 5 | ゲーム・趣味 | 家にゲーム機や組み立てる玩具はある？／普段どこに置いている？ |
| 8 | [53% of Americans Spend Too Much Time on Phones](https://eikaiwa.dmm.com/app/daily-news/article/53-of-americans-spend-too-much-time-on-phones/MSgnWqytEfGsXhOF9sJVWg) | 6 | スマホ・生活習慣 | スマホは一日何時間くらい使う？／よく開くアプリは？ |
| 9 | [Singapore Pays People to Read](https://eikaiwa.dmm.com/app/daily-news/article/singapore-pays-people-to-read/OeRljLG5EfGcZ48bzr337g) | 7 | 本・学習 | 本は週にどのくらい読む？／図書館は使う？／普段どこで読む？ |
| 10 | [Japan's Amazake Becoming Popular as a Health Drink](https://eikaiwa.dmm.com/app/daily-news/article/japans-amazake-becoming-popular-as-a-health-drink/09oZzLBeEfGb3k_8mH-MwQ) | 8 | 飲み物・日本文化 | 甘酒は飲む？／普段飲むものは？／どこで買う？ |
| 11 | [Driverless Taxi Service Planned for Tokyo in 2027](https://eikaiwa.dmm.com/app/daily-news/article/driverless-taxi-service-planned-for-tokyo-in-2027/zBAG1LGtEfGkbR_NyUk9rA) | 7 | 交通・テクノロジー | タクシーはどのくらい使う？／アプリと乗り場のどちらで手配する？ |
| 12 | [Remote Workers Lose 58 Minutes of Movement a Day](https://eikaiwa.dmm.com/app/daily-news/article/remote-workers-lose-58-minutes-of-movement-a-day/5zT_qLIiEfGM3rNaROjYNQ) | 5 | 仕事・運動 | 仕事中はどのくらい座っている？／休憩中は歩く？／通勤手段は？ |
| 13 | [Time Out Ranks the World's Best Cities for Cycling](https://eikaiwa.dmm.com/app/daily-news/article/time-out-ranks-the-worlds-best-cities-for-cycling/tLXbQq4IEfG1G-OqqHs4Gg) | 6 | 移動・街 | 自転車は使う？／どこへ行くときに乗る？／近所に駐輪場はある？ |
| 14 | [Japan's Tatami Mats Could Help Mood and Focus](https://eikaiwa.dmm.com/app/daily-news/article/japans-tatami-mats-could-help-mood-and-focus/WUKIVq4gEfGluofmZXnH5A) | 7 | 住まい・日本文化 | 家に畳の部屋はある？／床には何を敷いている？／どこで勉強する？ |
| 15 | [Osaka Metro Tests AI Robot Station Worker](https://eikaiwa.dmm.com/app/daily-news/article/osaka-metro-tests-ai-robot-station-worker/9xLxcqruEfGcujdddIVZCg) | 5 | 鉄道・生活 | 普段使う駅は？／切符とICカードのどちらを使う？／経路は何で調べる？ |
| 16 | [Americans Use Less Cash, but Still Carry It](https://eikaiwa.dmm.com/app/daily-news/article/americans-use-less-cash-but-still-carry-it/V3rjdqIgEfGKev8Z42cYjw) | 4 | 買い物・支払い | 普段は何で支払う？／現金はいくらくらい持ち歩く？ |
| 17 | [Three Key Decorating Tips for Renters](https://eikaiwa.dmm.com/app/daily-news/article/three-key-decorating-tips-for-renters/z4rOIKr1EfGeJJchj3wO1w) | 6 | 住まい・家具 | 部屋にはどんな家具を置いている？／壁に飾っているものはある？ |
| 18 | [How South Korea Solved the Problem of Food Waste](https://eikaiwa.dmm.com/app/daily-news/article/how-south-korea-solved-the-problem-of-food-waste/73RdTLWjEfG7Jq94kU8bJw) | 8 | 家事・環境 | 生ごみはどう分別する？／収集日は週に何回？／余った食材はどう保存する？ |
| 19 | [The Best Foods to Try at 7-Eleven Japan](https://eikaiwa.dmm.com/app/daily-news/article/the-best-foods-to-try-at-7-eleven-japan/NUFgwM_iEfC14ifDstv8Kg) | 4 | 食・コンビニ | コンビニには週に何回行く？／よく買う食べ物は？ |
| 20 | [Mobile Gaming May Hurt Your Neck and Elbows](https://eikaiwa.dmm.com/app/daily-news/article/mobile-gaming-may-hurt-your-neck-and-elbows/mgdn6KiGEfGD0GvdKa9ieQ) | 7 | ゲーム・スマホ | スマホでゲームをする？／一回何分くらい？／どんな姿勢で遊ぶ？ |
| 21 | [Screenshots Are Bad for Your Memory — Here's Why](https://eikaiwa.dmm.com/app/daily-news/article/screenshots-are-bad-for-your-memory-heres-why/Rj3FoJwdEfG9C0vj74qIYQ) | 8 | スマホ・記録 | スクリーンショットは撮る？／何を保存する？／後でどこから探す？ |
| 22 | [Paper Coffee Cups Release Millions of Nanoplastics](https://eikaiwa.dmm.com/app/daily-news/article/paper-coffee-cups-release-millions-of-nanoplastics/VohvqKVrEfGPxF9EYxbNNg) | 8 | 飲み物・日用品 | 飲み物は持ち帰りで買う？／家ではどんなカップを使う？／マイボトルは持ち歩く？ |
| 23 | [Tsukimi: Japan's Moon-Viewing Tradition](https://eikaiwa.dmm.com/app/daily-news/article/tsukimi-japans-moon-viewing-tradition/_1Co4MPoEfC-0b8k_26BLA) | 7 | 日本文化・季節 | 近所で月見の飾りや商品を見かける？／この時期に店に並ぶ食べ物は？ |
| 24 | [Sleep Trackers May Make You Feel More Tired](https://eikaiwa.dmm.com/app/daily-news/article/sleep-trackers-may-make-you-feel-more-tired/8tRuyKu3EfGklw9hmyh4DQ) | 8 | 睡眠・機器 | 睡眠時間は記録している？／使うアプリや機器は？／何時に起きる？ |
| 25 | [Research Confirms Tai Chi Health Benefits](https://eikaiwa.dmm.com/app/daily-news/article/research-confirms-tai-chi-health-benefits/6R_uwqHsEfG-Z-tnwjQAEQ) | 8 | 運動・生活習慣 | 普段どんな運動をする？／週に何回？／家と屋外のどちらでする？ |
| 26 | [Sweet, Bitter, Tart: Four Special Fruits from Japan](https://eikaiwa.dmm.com/app/daily-news/article/sweet-bitter-tart-four-special-fruits-from-japan/_m8xoverEfCNHePgAq8xMQ) | 4 | 食・買い物 | 普段買う果物は？／どこで買う？／だいたいいくら？ |
| 27 | [How to Make Your Home Feel Brand New](https://eikaiwa.dmm.com/app/daily-news/article/how-to-make-your-home-feel-brand-new/vw5EVA5_EfGnP7PpRQiL0A) | 4 | 住まい・家事 | 部屋にどんな家具がある？／掃除に何を使う？ |
| 28 | [What Makes Japanese Customer Service Unique](https://eikaiwa.dmm.com/app/daily-news/article/what-makes-japanese-customer-service-unique/CQOvTIbdEfGeoyMgtWOy6Q) | 4 | 日本文化・サービス | 普段行く店はセルフレジ？／袋詰めは誰がする？ |
| 29 | [Top Tips to Reduce Your Smartphone Use](https://eikaiwa.dmm.com/app/daily-news/article/top-tips-to-reduce-your-smartphone-use/CICFOE_bEfGTsx_CvC6R_g) | 4 | 生活習慣・テクノロジー | スマホをよく使う時間帯は？／利用時間の制限を設定している？ |
| 30 | [What Is 'Comfort Food,' and Why Do We Love It?](https://eikaiwa.dmm.com/app/daily-news/article/what-is-comfort-food-and-why-do-we-love-it/bjzf_iR9EfGPjzsMvpCEwQ) | 4 | 食・文化 | よく食べる料理は？／家で作るか買うか？ |
| 31 | [40% in US Say Kids Should Learn More Languages](https://eikaiwa.dmm.com/app/daily-news/article/40-in-us-say-kids-should-learn-more-languages/Ar08SpaFEfGwbesQN0gQ2Q) | 4 | 言語・教育 | 普段使う言語は？／英語のレッスンを週に何回受ける？ |
| 32 | [The Best Ways to Politely Correct Someone](https://eikaiwa.dmm.com/app/daily-news/article/the-best-ways-to-politely-correct-someone/9gnXHIwyEfGlHS9-QbZ03g) | 4 | コミュニケーション | 仕事の連絡はチャットか口頭か？／文章の修正にはどんな機能を使う？ |
| 33 | [Many Americans Judge People by Their Phone Wallpaper](https://eikaiwa.dmm.com/app/daily-news/article/many-americans-judge-people-by-their-phone-wallpaper/h14pJoG_EfGuAD9xBgVk7w) | 4 | 心理・スマホ | スマホの壁紙は何？／どのくらいの頻度で変える？ |
| 34 | [Work Makes It Hard to Be a Good Parent — Survey](https://eikaiwa.dmm.com/app/daily-news/article/work-makes-it-hard-to-be-a-good-parent-survey/_aHp0nOXEfGVhdf1p8JboQ) | 4 | 仕事・家庭 | 普段の勤務時間は？／職場に時短勤務の制度はある？ |
| 35 | [The Best Foods to Eat Before Running](https://eikaiwa.dmm.com/app/daily-news/article/the-best-foods-to-eat-before-running/JIVlNm5AEfGRLbsXg7Jmng) | 4 | 食・運動 | 普段運動する？／運動する時間帯は？／その前に食事を取る？ |
| 36 | [40% of Older Japanese Adults Want to Work](https://eikaiwa.dmm.com/app/daily-news/article/40-of-older-japanese-adults-want-to-work/D2U6EmhrEfGoMOOFnLqK7Q) | 4 | 仕事・日本社会 | 職場に定年制度はある？／何歳と決まっている？ |
| 37 | [The Best Places to Go Shopping in Tokyo](https://eikaiwa.dmm.com/app/daily-news/article/the-best-places-to-go-shopping-in-tokyo/xKUFNBmHEfG3brPEb06m8w) | 4 | 街・買い物 | 買い物はどの街でする？／そこまで何で行く？ |
| 38 | [How to Find Time for Yourself When Life Is Busy](https://eikaiwa.dmm.com/app/daily-news/article/how-to-find-time-for-yourself-when-life-is-busy/YYqffk1WEfG84kfZ_mRpkQ) | 4 | 生活・心理 | 平日に自由な時間は何時間くらいある？／何をして過ごす？ |
| 39 | [What Is 'Slow Travel' and Why Should We Do It?](https://eikaiwa.dmm.com/app/daily-news/article/what-is-slow-travel-and-why-should-we-do-it/NTPiVPaVEfC3XytKdYD3dw) | 4 | 旅行 | 旅行は普段何泊くらい？／一か所に泊まるか移動するか？ |
| 40 | [How to Plan the Perfect Day Trip](https://eikaiwa.dmm.com/app/daily-news/article/how-to-plan-the-perfect-day-trip/AiZ27kNQEfGV2N9fEVqZwQ) | 4 | 旅行 | 近場への外出には何を使う？／時刻や経路は何で調べる？ |
| 41 | [A 'Boring' Routine Could Be Good for Your Health](https://eikaiwa.dmm.com/app/daily-news/article/a-boring-routine-could-be-good-for-your-health/XTQhNDggEfGy0KNjP3B99w) | 4 | 健康・生活習慣 | 朝起きてから出かけるまで、普段何をする？ |
| 42 | [More than Half of Young Koreans Skip Breakfast](https://eikaiwa.dmm.com/app/daily-news/article/more-than-half-of-young-koreans-skip-breakfast/H3vhHrbDEe6xH3vFndujNQ) | 5 | 食事・生活習慣 | 朝食は食べる？／何時に、何を食べる？ |
| 43 | [Make Food from Ponyo with This Studio Ghibli Cookbook](https://eikaiwa.dmm.com/app/daily-news/article/make-food-from-ponyo-with-this-studio-ghibli-cookbook/nN-ggmAXEfGQoU89dxxpdA) | 5 | アニメ・食 | 家に料理本はある？／レシピは本・動画・サイトのどれで見る？ |
| 44 | [Should Restaurants Have 'Adults Only' Areas?](https://eikaiwa.dmm.com/app/daily-news/article/should-restaurants-have-adults-only-areas/eLHRfltzEfGH3JtuE5Vfeg) | 5 | 食・社会 | 普段行くレストランにはどんな席がある？／予約して行く？ |
| 45 | [Osaka Restaurant Adds Sushi Pizza to Its Menu](https://eikaiwa.dmm.com/app/daily-news/article/osaka-restaurant-adds-sushi-pizza-to-its-menu/GnCjwmLrEfGkX7PQPazHOg) | 5 | 食・新商品 | 寿司やピザはどのくらい食べる？／持ち帰りと店内のどちらが多い？ |
| 46 | [Clothes Top List of Online Returns — Survey](https://eikaiwa.dmm.com/app/daily-news/article/clothes-top-list-of-online-returns-survey/DdqePmLlEfGNW1dCM5Sabw) | 5 | 買い物・生活 | 服はネットで買う？／サイズ表を見る？／普段使うサイトは？ |
| 47 | [Japan's Summer Plans Change as Costs Rise](https://eikaiwa.dmm.com/app/daily-news/article/japans-summer-plans-change-as-costs-rise/m2rqAoV2EfGKSEsTg5Wrfg) | 5 | 旅行・家計 | 休日の外出には月にいくらくらい使う？／宿や交通は何で予約する？ |
| 48 | [Driverless Taxis Are Coming to European Cities](https://eikaiwa.dmm.com/app/daily-news/article/driverless-taxis-are-coming-to-european-cities/33kq5pwkEfGS4I-inJGX6A) | 5 | 交通・テクノロジー | 普段の移動手段は？／タクシーはアプリで呼ぶ？ |
| 49 | [Ticket Prices Rising at Japan's Amusement Parks](https://eikaiwa.dmm.com/app/daily-news/article/ticket-prices-rising-at-japans-amusement-parks/7m8aYpVMEfGOA5f8OMEm1A) | 5 | 娯楽・家計 | 遊園地に行く頻度は？／チケットはどこで買う？ |
| 50 | [Japan's Paternity Leave Rate Topped 50% in 2025](https://eikaiwa.dmm.com/app/daily-news/article/japans-paternity-leave-rate-topped-50-in-2025/-HcesJABEfGAPnNXsZZjXg) | 5 | 仕事・家庭 | 職場に育休制度はある？／制度の案内はどこで確認できる？ |
| 51 | [Japan's Food Waste Falls to Record Low](https://eikaiwa.dmm.com/app/daily-news/article/japans-food-waste-falls-to-record-low/3ardwHbEEfGrTGebcGpFYw) | 5 | 食・環境 | 余った料理は冷凍する？／買い物前に冷蔵庫を確認する？ |
| 52 | [US Remote Work Increased in 2025](https://eikaiwa.dmm.com/app/daily-news/article/us-remote-work-increased-in-2025/e-kRoHmVEfG_X3em4ZTl4g) | 5 | 仕事・生活 | 週に何日出社する？／通勤には何分かかる？ |
| 53 | [New Sleeper Train Connects Tokyo to Aomori](https://eikaiwa.dmm.com/app/daily-news/article/new-sleeper-train-connects-tokyo-to-aomori/6OdSqmmPEfGC9usLg9r5qw) | 5 | 旅行・鉄道 | 長距離の移動には何を使う？／電車の切符はどこで買う？ |
| 54 | [The Mistakes Travelers Make When Visiting Japan](https://eikaiwa.dmm.com/app/daily-news/article/the-mistakes-travelers-make-when-visiting-japan/Whg9WGDbEfGAkT9i9gOiLw) | 5 | 旅行・日本文化 | 電車やバスの支払い方法は？／近所に英語の案内はある？ |
| 55 | [Many Americans Choose Sleep over Plans with Friends](https://eikaiwa.dmm.com/app/daily-news/article/many-americans-choose-sleep-over-plans-with-friends/X6HU5l6hEfGAUAvF17libg) | 5 | 生活・人間関係 | 平日は何時間寝る？／友人とは普段どの時間帯に会う？ |
| 56 | [Japan Will Soon Have a Pokemon-Themed Airport](https://eikaiwa.dmm.com/app/daily-news/article/japan-will-soon-have-a-pokemon-themed-airport/I5VAlFOuEfGr7iNfU7WMew) | 5 | 旅行・娯楽 | 普段使う空港は？／空港までは何で行く？ |
| 57 | [Wobbly Beer Glass Forces You to Drink Water](https://eikaiwa.dmm.com/app/daily-news/article/wobbly-beer-glass-forces-you-to-drink-water/ca8y6JX-EfGzxMdwj23Mvw) | 6 | 飲み物・アイデア商品 | お酒は飲む？／普段飲む種類と量は？／水も一緒に飲む？ |
| 58 | [New Museum Celebrates the World of Jellyfish](https://eikaiwa.dmm.com/app/daily-news/article/new-museum-celebrates-the-world-of-jellyfish/rfXkuJujEfGcT-OaCPrsqQ) | 6 | お出かけ・自然 | 近くに水族館や博物館はある？／休みの日はどんな施設を利用する？ |
| 59 | [S. Korean Program Rewards People for Exercise](https://eikaiwa.dmm.com/app/daily-news/article/s-korean-program-rewards-people-for-exercise/OURceJJ4EfGhfo-Z8ZmXUQ) | 6 | 健康・制度 | 週に何回運動する？／歩数をアプリで記録している？ |
| 60 | [74% of US Consumers Have Used AI to Shop](https://eikaiwa.dmm.com/app/daily-news/article/74-of-us-consumers-have-used-ai-to-shop/3_NPoomVEfGg0JPJm6pwAw) | 6 | AI・買い物 | 商品を探すときは何を使う？／レビューやAIを使う？ |
| 61 | [Seoul, Tokyo Named Best Cities for Digital Nomads](https://eikaiwa.dmm.com/app/daily-news/article/seoul-tokyo-named-best-cities-for-digital-nomads/SEB5jpssEfGmrPPysZoj5A) | 6 | 街・働き方 | 普段どこで仕事や勉強をする？／ネットや電源はある？ |
| 62 | [South Korea, US Are Japan's Top Fashion Influences](https://eikaiwa.dmm.com/app/daily-news/article/south-korea-us-are-japans-top-fashion-influences/nVUclJsZEfG40r-t8yJDYg) | 6 | ファッション・文化 | 普段着る服のブランドは？／服の情報はどこで見る？ |
| 63 | [Japanese People Spend Less Time and Money on Leisure](https://eikaiwa.dmm.com/app/daily-news/article/japanese-people-spend-less-time-and-money-on-leisure/nGRelpqpEfGGf_OWMu3UBg) | 6 | 娯楽・家計 | 普段の趣味は？／週に何時間、月にいくらくらい使う？ |
| 64 | [Four Easy Tricks to Help You Eat Better](https://eikaiwa.dmm.com/app/daily-news/article/four-easy-tricks-to-help-you-eat-better/KxQsAoIYEfGb9h9je8GHXA) | 6 | 食事・家事 | 平日の夕食は何時？／自炊・外食・弁当のどれが多い？ |
| 65 | [Japanese Choosing 'Coolcations' for Summer Trips](https://eikaiwa.dmm.com/app/daily-news/article/japanese-choosing-coolcations-for-summer-trips/mESeWpYUEfGijadPgGYgHA) | 6 | 旅行・季節 | 夏の外出は何時ごろ？／暑い日はどんな場所で過ごす？ |
| 66 | [Robot Chef Cooks Noodles in Just 90 Seconds](https://eikaiwa.dmm.com/app/daily-news/article/robot-chef-cooks-noodles-in-just-90-seconds/KJqy1JVQEfGF01cAUoqZeA) | 6 | 食・ロボット | 麺料理はどのくらい食べる？／普段行く店では注文や配膳はどうする？ |
| 67 | [Would You Say 'I Do' to These Unusual Wedding Traditions?](https://eikaiwa.dmm.com/app/daily-news/article/would-you-say-i-do-to-these-unusual-wedding-traditions/ilh0tl7bEe2DGZOuFcnsAw) | 6 | 文化・結婚 | 日本の結婚式ではどんな服を着る？／お祝いは何を渡す？ |
| 68 | [Many Japanese Workers Consider Quitting Their Jobs](https://eikaiwa.dmm.com/app/daily-news/article/many-japanese-workers-consider-quitting-their-jobs/JBzARI8GEfGU_kPq34g3iA) | 6 | 仕事・日本社会 | 今の仕事はどんな仕事内容？／勤務日数や勤務場所は？ |
| 69 | [New Ghibli Anime Released — But Only at Ghibli Park](https://eikaiwa.dmm.com/app/daily-news/article/new-ghibli-anime-released-but-only-at-ghibli-park/7n4eKIHrEfGGFZsaA3RBMA) | 6 | アニメ・観光 | アニメは普段どこで見る？／利用している配信サービスは？ |
| 70 | [Japanese Workers Pay Services to Ask for Leave](https://eikaiwa.dmm.com/app/daily-news/article/japanese-workers-pay-services-to-ask-for-leave/gW_SBIRhEfGTL5czH0GjzQ) | 6 | 仕事・文化 | 職場で休みを申請する方法は？／誰に、何日前までに伝える？ |
| 71 | [Read, Don't Talk: What Are Silent Reading Clubs?](https://eikaiwa.dmm.com/app/daily-news/article/read-dont-talk-what-are-silent-reading-clubs/50eetm_IEfGRo1unW0a3pA) | 6 | 本・コミュニティ | 普段どこで本を読む？／紙と電子書籍のどちらを使う？ |
| 72 | [New Flip Phone Made to Do 'as Little as Possible'](https://eikaiwa.dmm.com/app/daily-news/article/new-flip-phone-made-to-do-as-little-as-possible/k_io6o0jEfGdQO-6wcDhdw) | 7 | テクノロジー・生活 | スマホで毎日使う機能は？／通話はどのくらいする？ |
| 73 | [Why Tourists Love Foreign Supermarkets](https://eikaiwa.dmm.com/app/daily-news/article/why-tourists-love-foreign-supermarkets/OnFdcJgyEfGVtH8zH3DSHQ) | 7 | 旅行・買い物 | 普段使うスーパーは？／どんな売り場がある？／営業時間は？ |
| 74 | [The 'Gen Alpha Melody': Why New Songs Sound the Same](https://eikaiwa.dmm.com/app/daily-news/article/the-gen-alpha-melody-why-new-songs-sound-the-same/W_JlnpZvEfGo1wuf9mkbMA) | 7 | 音楽・ネット文化 | 音楽はどのアプリで聴く？／普段聴くジャンルは？ |
| 75 | [Coffee Cup Texture May Change What You Taste](https://eikaiwa.dmm.com/app/daily-news/article/coffee-cup-texture-may-change-what-you-taste/0B6w8nS1EfGSDZfW8vCwHg) | 7 | 食・心理 | コーヒーやお茶は毎日飲む？／家ではどんなカップを使う？ |
| 76 | [Japan's Convenience Stores Ready to Help After Disasters](https://eikaiwa.dmm.com/app/daily-news/article/japans-convenience-stores-ready-to-help-after-disasters/dk4USlCAEfGNjhczHT6-2A) | 7 | 防災・生活 | 家に水や非常食は置いている？／近所にコンビニはある？ |
| 77 | ['FIRE' Movement Helps People Retire Early](https://eikaiwa.dmm.com/app/daily-news/article/fire-movement-helps-people-retire-early/ehAqxp0DEfGN33vEy60xtw) | 7 | 仕事・お金 | 家計簿はつける？／毎月決まった額を貯金している？ |
| 78 | [Feeding by Tourists Puts Japan's Rabbit Island at Risk](https://eikaiwa.dmm.com/app/daily-news/article/feeding-by-tourists-puts-japans-rabbit-island-at-risk/Cs_mFpwIEfGWDBPjCJBZEw) | 7 | 観光・動物 | 近所の公園には動物への餌やりの注意書きがある？／どんなルール？ |
| 79 | [Amazon Expands Its Drone Delivery Service](https://eikaiwa.dmm.com/app/daily-news/article/amazon-expands-its-drone-delivery-service/BxsyGJxoEfGdiCMF5ejv7Q) | 7 | 買い物・テクノロジー | ネット通販は月に何回使う？／荷物は対面・置き配・ロッカーのどれで受け取る？ |
| 80 | [Airline to Charge Passengers to Use Overhead Lockers](https://eikaiwa.dmm.com/app/daily-news/article/airline-to-charge-passengers-to-use-overhead-lockers/w__-KJGVEfGuDQuKR7becA) | 7 | 旅行・料金 | 飛行機に乗るときはどんなかばんを使う？／荷物を預ける？ |
| 81 | [How to Make Time for 'Deep Work'](https://eikaiwa.dmm.com/app/daily-news/article/how-to-make-time-for-deep-work/3E1LiLRHEfCW3G8Ni9xBrQ) | 7 | 仕事・集中 | 作業中は通知を切っている？／集中する時間帯は？ |
| 82 | [Is Social Media Ruining the Joy of Travel?](https://eikaiwa.dmm.com/app/daily-news/article/is-social-media-ruining-the-joy-of-travel/s0qbFoaBEfGwjKvz0gA7Ag) | 7 | 旅行・SNS | SNSに写真を載せる？／撮影と投稿にはどのアプリを使う？ |
| 83 | [Just 10 Minutes of Forest Birdsong May Relieve Stress](https://eikaiwa.dmm.com/app/daily-news/article/just-10-minutes-of-forest-birdsong-may-relieve-stress/Rf_CbItdEfGL1GeF-PY5dw) | 7 | 自然・健康 | 家の周りに公園や木はある？／普段どんな鳥の声が聞こえる？ |
| 84 | [Older Tokyo Residents Increasingly Enjoy Time Alone](https://eikaiwa.dmm.com/app/daily-news/article/older-tokyo-residents-increasingly-enjoy-time-alone/3vbiSonpEfGnwK9bSkDzJA) | 7 | 生活・社会 | 一人で過ごす時間は一日どのくらい？／その時間に何をする？ |
| 85 | [Monitoring Employees Doesn't Improve Performance](https://eikaiwa.dmm.com/app/daily-news/article/monitoring-employees-doesnt-improve-performance/tKLQ8IbvEfG5unMzjAnsew) | 7 | 仕事・管理 | 職場では勤怠をどう記録する？／作業報告はどのくらいの頻度？ |
| 86 | [Saving Money Is Easier with Goals — US Survey](https://eikaiwa.dmm.com/app/daily-news/article/saving-money-is-easier-with-goals-us-survey/wnmPkG_cEfGqX6f0IzXWng) | 7 | お金・生活 | 貯金は自動積立か手動か？／残高は何で確認する？ |
| 87 | [More Clothing Brands Offering Repair Services](https://eikaiwa.dmm.com/app/daily-news/article/more-clothing-brands-offering-repair-services/9XjAopVQEfGpyTNNXjaStA) | 8 | 買い物・環境 | 服はどこで買う？／修理に出す？／何年くらい着る？ |
| 88 | [United Airlines Announces New Empty Middle Seat Row](https://eikaiwa.dmm.com/app/daily-news/article/united-airlines-announces-new-empty-middle-seat-row/5Pq6FoEcEfG1_kslPNfZqA) | 8 | 旅行・サービス | 飛行機ではどの席を選ぶ？／予約時に座席指定をする？ |
| 89 | [Why Do We Get Grumpy in Hot Weather?](https://eikaiwa.dmm.com/app/daily-news/article/why-do-we-get-grumpy-in-hot-weather/VWAuanTREfGJuf9eBBU6LQ) | 8 | 健康・季節 | 夏は冷房を何度に設定する？／外出時に何を持ち歩く？ |
| 90 | [New Pixel Phones Betting on AI to Tempt Buyers](https://eikaiwa.dmm.com/app/daily-news/article/new-pixel-phones-betting-on-ai-to-tempt-buyers/VIBC5JboEfGRlKv74RAPtA) | 8 | スマホ・AI | 今のスマホは何年使っている？／AI機能を使っている？ |
| 91 | [Remote Work Making Americans Lonelier — Report](https://eikaiwa.dmm.com/app/daily-news/article/remote-work-making-americans-lonelier-report/eYFummQiEfG0zN9xEcT2HA) | 8 | 仕事・生活 | 同僚との連絡には何を使う？／雑談する機会は一日にどのくらいある？ |
| 92 | [Some US Colleges Now Offer 'Influencer' Degrees](https://eikaiwa.dmm.com/app/daily-news/article/some-us-colleges-now-offer-influencer-degrees/_7zrnJe8EfGCpsvFKz2b0A) | 8 | 教育・SNS | 普段見るSNSは？／どんな分野のアカウントをフォローしている？ |
| 93 | [AI Uptake Remains Slow in Japan](https://eikaiwa.dmm.com/app/daily-news/article/ai-uptake-remains-slow-in-japan/MyhazpgsEfGjCWfqbre3qQ) | 8 | AI・仕事 | AIを仕事や日常で使う？／どんな作業に使う？ |
| 94 | [Kellogg to Remove Artificial Colors from Its Cereals](https://eikaiwa.dmm.com/app/daily-news/article/kellogg-to-remove-artificial-colors-from-its-cereals/3TrHEpJbEfGdNe8mtIXc9w) | 8 | 食・健康 | 朝食にシリアルを食べる？／買い物で原材料表示を見る？ |
| 95 | [The Story of How the Days of the Week Got Their Names](https://eikaiwa.dmm.com/app/daily-news/article/the-story-of-how-the-days-of-the-week-got-their-names/To7V0n3_EeySu1_Dd8K7hA) | 8 | 言語・日常 | 仕事やレッスンは何曜日？／ごみ収集は何曜日？ |
| 96 | [Your Birth Order May Affect Your Health](https://eikaiwa.dmm.com/app/daily-news/article/your-birth-order-may-affect-your-health/j3B1EpWzEfG5w39X3gK_Jw) | 8 | 家族・健康 | 兄弟姉妹はいる？／何人？／普段家族とはどのくらい連絡を取る？ |
| 97 | [Algorithms May Be Making Your Media Consumption Boring](https://eikaiwa.dmm.com/app/daily-news/article/algorithms-may-be-making-your-media-consumption-boring/WhO3bGA0EfGQNAsu98pCvA) | 8 | メディア・AI | 動画は検索とおすすめ欄のどちらから選ぶ？／使っているサービスは？ |
| 98 | [Mexico Passes Bill to Cut Workweek to 40 Hours](https://eikaiwa.dmm.com/app/daily-news/article/mexico-passes-bill-to-cut-workweek-to-40-hours/VSNrFGTsEfGV9MftrLIubQ) | 8 | 仕事・制度 | 週に何日、何時間働く？／休憩は何分？ |
| 99 | [Hiking Affects Animal Behavior More than We Think](https://eikaiwa.dmm.com/app/daily-news/article/hiking-affects-animal-behavior-more-than-we-think/uMxfFl7REfGazcfcdlUQrg) | 8 | アウトドア・自然 | 普段歩く場所は街中か自然の中か？／近くの散策路にどんな標識がある？ |
| 100 | [How Notifications Hurt Your Concentration](https://eikaiwa.dmm.com/app/daily-news/article/how-notifications-hurt-your-concentration/2gBv9Ce6EfG7QQ_dbT_vxw) | 8 | スマホ・集中 | どのアプリの通知をオンにしている？／寝るときは音を消す？ |

最初は **Japan's Favorite Rice Dish Is Chahan — Survey**（チャーハンの具・作る頻度）、**Average American Rates Their Home 7.5 Out of 10**（部屋数・過ごす場所）、**Save Time with These Meal-Prepping Tips**（作り置き・保存方法）がおすすめです。買い物なら **Americans Use Less Cash, but Still Carry It**（支払い方法）、Level 8なら **How South Korea Solved the Problem of Food Waste**（ごみの分別・収集日）から話し始められます。

### 選定基準

- 現在の習慣、頻度、使っている物、店、場所、手順、身近なルールなど、すでに知っている事実を答えるだけで会話が成り立つことを優先する
- 「そんな思い出はある？」「印象的な出来事は？」「子どもの頃は？」など、記憶を探してエピソードを組み立てる必要がある質問は避ける
- 「なぜそう思う？」「賛成か反対か？」「理想は？」「社会にどんな影響がある？」など、意見や分析が中心になる記事は優先度を下げる
- 食事、家事、健康、製品、学校・学習、仕事、買い物、旅行、娯楽、文化、自然・環境に題材を広げる
- Level 4〜8を各20件とし、英文の難しさとは別に、回答内容を考える負担が小さいかを判断する
- ペットの飼育、育児、海外旅行など特定の経験を前提にせず、現在の生活や知っている範囲の事実から答えられる入口を用意する
- 専門知識や調べ直しが必要な説明を求めず、健康・技術の記事も普段の習慣や使い方を話す入口として選ぶ
- 実際のDiscussionでは事実・習慣を聞く質問の数と答えやすさを確認する。会話案だけで記事の設問まで話しやすいとは判断しない
