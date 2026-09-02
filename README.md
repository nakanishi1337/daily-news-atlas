# DMM Daily News collector

DMM Daily Newsの一覧ページに含まれるサーバー生成HTMLから、記事タイトル、レベル、公開日時、URLを抽出します。ブラウザやJavaScript実行環境は不要です。

```bash
python3 collect_daily_news.py --pretty
python3 collect_daily_news.py --min-level 5 --max-level 7 --limit 20 --pretty
python3 collect_daily_news.py --all-pages --pretty --output daily_news_articles.json
```

個人学習の範囲で、サイトに負荷をかけない頻度で実行してください。

## レッスン候補

記事本文の難しさよりも、Discussionで自分の経験や身近な日本の状況を話しやすいかを重視した候補です。Level 8も含みます。上から順におすすめです。

| # | 記事 | Level | 選定理由 |
|---:|---|:---:|---|
| 1 | [Japan's Convenience Stores Ready to Help After Disasters](https://eikaiwa.dmm.com/app/daily-news/article/japans-convenience-stores-ready-to-help-after-disasters/dk4USlCAEfGNjhczHT6-2A) | 7 | 防災の備えと普段使うコンビニの両方を、自分の経験から具体的に話せる（利用して特に良かった記事） |
| 2 | [Why Tourists Love Foreign Supermarkets](https://eikaiwa.dmm.com/app/daily-news/article/why-tourists-love-foreign-supermarkets/OnFdcJgyEfGVtH8zH3DSHQ) | 7 | 旅行先のスーパー、日本との違い、買いたい商品について答えやすい |
| 3 | [FamilyMart Uses Cute Stickers to Fight Food Waste](https://eikaiwa.dmm.com/app/daily-news/article/familymart-uses-cute-stickers-to-fight-food-waste/gr0MEMjBEe-hbDu_rqAE4A) | 7 | コンビニでの買い物経験から、値引きや食品ロス対策の効果を話せる |
| 4 | [How Smartphone Use Is Affecting Our Bodies](https://eikaiwa.dmm.com/app/daily-news/article/how-smartphone-use-is-affecting-our-bodies/p8ApennNEfGM5Q-NWesaPg) | 8 | 毎日のスマホ利用、姿勢、利用時間など、自分の習慣をそのまま話題にできる |
| 5 | [More Clothing Brands Offering Repair Services](https://eikaiwa.dmm.com/app/daily-news/article/more-clothing-brands-offering-repair-services/9XjAopVQEfGpyTNNXjaStA) | 8 | 服を修理するか買い替えるか、価格や環境面から身近な意見を言える |
| 6 | [Airline to Charge Passengers to Use Overhead Lockers](https://eikaiwa.dmm.com/app/daily-news/article/airline-to-charge-passengers-to-use-overhead-lockers/w__-KJGVEfGuDQuKR7becA) | 7 | 飛行機で何に追加料金を払えるか、旅行経験をもとに賛否を話せる |
| 7 | [Why Do We Get Grumpy in Hot Weather?](https://eikaiwa.dmm.com/app/daily-news/article/why-do-we-get-grumpy-in-hot-weather/VWAuanTREfGJuf9eBBU6LQ) | 8 | 暑さによる気分や行動の変化、夏の対策を実体験から答えられる |
| 8 | [Some US Colleges Now Offer 'Influencer' Degrees](https://eikaiwa.dmm.com/app/daily-news/article/some-us-colleges-now-offer-influencer-degrees/_7zrnJe8EfGCpsvFKz2b0A) | 8 | インフルエンサーに大学教育が必要か、SNSや仕事の観点から話しやすい |
| 9 | ['FIRE' Movement Helps People Retire Early](https://eikaiwa.dmm.com/app/daily-news/article/fire-movement-helps-people-retire-early/ehAqxp0DEfGN33vEy60xtw) | 7 | 節約、仕事、理想の退職年齢を自分の価値観に結びつけられる |
| 10 | [Japan's Convenience Stores Report Record Profits](https://eikaiwa.dmm.com/app/daily-news/article/japans-convenience-stores-report-record-profits/GwZ-cj57EfGzSQ_CB2iZWA) | 7 | よく使うサービスや価格、コンビニが好調な理由を日本の生活から説明できる |

最初に選ぶなら `Disasters and Convenience Stores` → `Foreign Supermarkets` → `FamilyMart Food Waste` の順がおすすめです。Level 8にも挑戦するなら `Smartphone Use` が第一候補です。

### 追加候補

収集済みの全13,379記事から選んだ追加候補です。

#### 特におすすめ

| # | 記事 | Level | 選定理由 |
|---:|---|:---:|---|
| 1 | [Wobbly Beer Glass Forces You to Drink Water](https://eikaiwa.dmm.com/app/daily-news/article/wobbly-beer-glass-forces-you-to-drink-water/ca8y6JX-EfGzxMdwj23Mvw) | 6 | 水を飲ませる変わった商品で、行動を変える仕組みについて話しやすい |
| 2 | [Robot Chef Cooks Noodles in Just 90 Seconds](https://eikaiwa.dmm.com/app/daily-news/article/robot-chef-cooks-noodles-in-just-90-seconds/KJqy1JVQEfGF01cAUoqZeA) | 6 | 新しい食の技術やロボット料理について話せる |
| 3 | [England to Reward People for Going for a Walk](https://eikaiwa.dmm.com/app/daily-news/article/england-to-reward-people-for-going-for-a-walk/0kGY2nyBEfGiTG827KIIqw) | 6 | 運動への報奨制度を韓国の記事と比較できる |
| 4 | [Osaka Restaurant Adds Sushi Pizza to Its Menu](https://eikaiwa.dmm.com/app/daily-news/article/osaka-restaurant-adds-sushi-pizza-to-its-menu/GnCjwmLrEfGkX7PQPazHOg) | 5 | 変わった料理を食べたいか、気軽に意見を言える |
| 5 | [How the World's Greatest Cities Got Their Nicknames](https://eikaiwa.dmm.com/app/daily-news/article/how-the-worlds-greatest-cities-got-their-nicknames/kvwAGM1gEeyal6spyz0dBw) | 6 | 国の愛称記事の都市版で、好みとの一致度が高い |

#### 食べ物・飲み物

| 記事 | Level | 選定理由 |
|---|:---:|---|
| [Kamakura Store Sells Kanji Ice Cream That Doesn't Melt](https://eikaiwa.dmm.com/app/daily-news/article/kamakura-store-sells-kanji-ice-cream-that-doesnt-melt/aVU-hFX5EfGQ9CeISDyp1w) | 5 | 溶けない漢字アイスという、説明しやすく意外性のある商品 |
| [Fries Taste Better When Stolen, Study Finds](https://eikaiwa.dmm.com/app/daily-news/article/fries-taste-better-when-stolen-study-finds/Uo5KhEj7EfGOrft6IRWOJw) | 6 | 自分の経験や食事のマナーに話を広げやすい |
| [Why Some Dishes Taste Better the Next Day](https://eikaiwa.dmm.com/app/daily-news/article/why-some-dishes-taste-better-the-next-day/tauowPe-EfC6zUtLUQy0aQ) | 6 | カレーなど身近な例を使って説明できる |
| [People Like Insect Protein Bars if They Try Them — Study](https://eikaiwa.dmm.com/app/daily-news/article/people-like-insect-protein-bars-if-they-try-them-study/V6ONaHuvEfGrKbP1nrIRPw) | 6 | 昆虫食を試せるか、軽い賛否を話せる |
| [Special Meals Help People Get Through the Week](https://eikaiwa.dmm.com/app/daily-news/article/special-meals-help-people-get-through-the-week/GSj7LHOeEfG6XRMGbNWqDA) | 5 | ご褒美や好きな食事を自分の生活から答えられる |
| [Cool Off with These Cold Summer Coffee Recipes](https://eikaiwa.dmm.com/app/daily-news/article/cool-off-with-these-cold-summer-coffee-recipes/ax49RGjfEfGtdU_XtHz4IA) | 6 | 好きな飲み方や海外のコーヒー文化について話せる |

#### 海外文化・ユニークな仕組み

| 記事 | Level | 選定理由 |
|---|:---:|---|
| [Indonesian Parents Name Kids After Anime Characters](https://eikaiwa.dmm.com/app/daily-news/article/indonesian-parents-name-kids-after-anime-characters/NyemJpW6EfGMUte5PBT1MQ) | 6 | 名前、アニメ、海外での日本文化を組み合わせた話題 |
| [Swiss Bus Has No Destination, Just Conversation](https://eikaiwa.dmm.com/app/daily-news/article/swiss-bus-has-no-destination-just-conversation/5y80el9qEfGp-4-qd0DAWw) | 6 | 会話だけを目的にしたバスへ参加したいかを話せる |
| [Taiwan to Pay Tourists to Visit Again](https://eikaiwa.dmm.com/app/daily-news/article/taiwan-to-pay-tourists-to-visit-again/FcmBeHqREfGSLNtlTBDhNA) | 6 | 報奨制度と旅行経験を組み合わせて話せる |
| [Why Do Countries Drive on Different Sides of the Road?](https://eikaiwa.dmm.com/app/daily-news/article/why-do-countries-drive-on-different-sides-of-the-road/1uY-LLACEey0iL94DWsC5Q) | 6 | 国による身近な違いを比較できる |

追加候補から選ぶなら `Wobbly Beer Glass` → `Robot Chef` → `England to Reward People for Going for a Walk` → `Sushi Pizza` → `City Nicknames` の順がおすすめです。

### アーカイブからのおすすめ

全期間の記事を収集した後、これまで候補に入っていなかった2020〜2024年の記事から追加で選びました。

| 記事 | 公開年 | Level | 選定理由 |
|---|:---:|:---:|---|
| [Japanese Brewery Releases Special Slow-Drink Glass](https://eikaiwa.dmm.com/app/daily-news/article/japanese-brewery-releases-special-slow-drink-glass/vEUGNkjiEe-7F6_9GZ2lmw) | 2024 | 6 | 飲む速さを変えるグラスで、商品の工夫について話しやすい |
| [Japanese Pizza Chain Delivers Pizza for Dogs](https://eikaiwa.dmm.com/app/daily-news/article/japanese-pizza-chain-delivers-pizza-for-dogs/vWvv-nT5Ee-ozPsNdD79zw) | 2024 | 5 | 犬用ピザという分かりやすい意外性があり、ペットの話にも広げられる |
| [Scone: The Word That Divides the UK](https://eikaiwa.dmm.com/app/daily-news/article/scone-the-word-that-divides-the-uk/TDvX6Go-Ee-dGN8NwN0O1w) | 2024 | 6 | 同じ英単語の発音の違いから、地域や言葉の話ができる |
| [Lost Parakeet Rides Bullet Train, Travels to Tokyo](https://eikaiwa.dmm.com/app/daily-news/article/lost-parakeet-rides-bullet-train-travels-to-tokyo/oN4rZmCdEe-kRE8HGZUXdQ) | 2024 | 6 | インコが新幹線で東京へ行く軽いニュースで、内容を説明しやすい |
| [Japanese People Are Taking Smiling Lessons](https://eikaiwa.dmm.com/app/daily-news/article/japanese-people-are-taking-smiling-lessons/ET2GDPOCEe255vsc3nP0Ug) | 2023 | 6 | 笑顔の練習という珍しい習慣を、文化や自分の経験と比較できる |
| [Bluetooth: The Unusual History of a Name](https://eikaiwa.dmm.com/app/daily-news/article/bluetooth-the-unusual-history-of-a-name/iakgzrbJEe2L9UucDZi9_g) | 2023 | 6 | 身近な技術の名前の由来で、国や都市の愛称記事に近い |
| [Tea Bag, Hot Water, Milk: How 70% of Britons Make Tea](https://eikaiwa.dmm.com/app/daily-news/article/tea-bag-hot-water-milk-how-70-of-britons-make-tea/qbcyCqC-Ee2ZenP8negxag) | 2023 | 6 | 飲み物の作り方を通して、英国と日本の習慣を比較できる |
| [Japan's Momofuku Ando and the History of Instant Noodles](https://eikaiwa.dmm.com/app/daily-news/article/japans-momofuku-ando-and-the-history-of-instant-noodles/5tgSYnDLEe2mpt-_PxNA7Q) | 2023 | 6 | 好きだった冷水カップ麺記事につながる、身近な食品の歴史 |
| [This Mattress Company Is Paying People to Sleep in Public](https://eikaiwa.dmm.com/app/daily-news/article/this-mattress-company-is-paying-people-to-sleep-in-public/ETX0zhpbEe2ph0v-Ptr7UQ) | 2022 | 6 | 寝ると報酬がもらえる仕事で、ユニークな制度の話に近い |
| [These Electric Chopsticks Make Food Taste Saltier](https://eikaiwa.dmm.com/app/daily-news/article/these-electric-chopsticks-make-food-taste-saltier/6kMAZMWHEeyWehcg72DigQ) | 2022 | 6 | 食事と新技術を組み合わせた、試してみたいか答えやすい商品 |
| [Would You Add Hot Sauce to Your Coffee?](https://eikaiwa.dmm.com/app/daily-news/article/would-you-add-hot-sauce-to-your-coffee/-eKRkKw_Eeu9noNnn9nlWQ) | 2021 | 6 | 変わった味の組み合わせについて気軽に賛否を話せる |
| [People in Taiwan Change Names to 'Salmon' for Free Sushi](https://eikaiwa.dmm.com/app/daily-news/article/people-in-taiwan-change-names-to-salmon-for-free-sushi/x8m7XItlEeusDgfBzib6Qw) | 2021 | 5 | 無料寿司のための改名という、食・名前・海外制度が揃った題材 |
| [Robot Wolves Protect Japanese City from Bears](https://eikaiwa.dmm.com/app/daily-news/article/robot-wolves-protect-japanese-city-from-bears/DEJGRi9PEeuz-4_mIcDz5g) | 2020 | 6 | ロボットのオオカミという意外性があり、日本の事情も説明しやすい |

この中では `Slow-Drink Glass` → `Salmon Name` → `Electric Chopsticks` → `Bluetooth` → `Instant Noodles` の順がおすすめです。

### 分野を広げるおすすめ

これまでの食べ物・旅行・海外習慣中心の傾向から意図的に離れ、技術・科学・心理・仕事・歴史・環境から選んだ候補です。Level 7も含め、少し難しい意見説明にも挑戦できます。

#### 技術・未来

| 記事 | Level | 選定理由 |
|---|:---:|---|
| [Japan Builds Its First 3D-Printed Two-Story Home](https://eikaiwa.dmm.com/app/daily-news/article/japan-builds-its-first-3d-printed-two-story-home/CSCkQk4iEfG7Z_88xAO8tQ) | 7 | 3Dプリンター住宅の利点、安全性、住宅不足への効果を考えられる |
| [New Battery Powers EV for 1,000 Kilometers](https://eikaiwa.dmm.com/app/daily-news/article/new-battery-powers-ev-for-1000-kilometers/AcYxWKTxEe6bgg8Ar_2G-A) | 7 | EV普及の条件や、航続距離と充電時間の重要性を比較できる |
| [Japan to Launch Wooden Satellite This Year](https://eikaiwa.dmm.com/app/daily-news/article/japan-to-launch-wooden-satellite-this-year/16iW2uFaEe614xu2-7H4fA) | 7 | 木製人工衛星を入口に、宇宙ごみや新素材について話せる |
| [Short-Distance Electric Flights Coming to Europe](https://eikaiwa.dmm.com/app/daily-news/article/short-distance-electric-flights-coming-to-europe/Uiiu2pScEfGFwn-e8AmgKQ) | 7 | 電動航空機の実現性や鉄道との使い分けを議論できる |
| [How to Tell if a Face Was Made by AI](https://eikaiwa.dmm.com/app/daily-news/article/how-to-tell-if-a-face-was-made-by-ai/yIjmFHu9EfGs8V9j8zLcOw) | 7 | AI画像、偽情報、ネット上の信頼性を考えられる |

#### 脳・心理

| 記事 | Level | 選定理由 |
|---|:---:|---|
| [Writing by Hand May Improve Brain Connectivity](https://eikaiwa.dmm.com/app/daily-news/article/writing-by-hand-may-improve-brain-connectivity/qgoSANSDEe65mu__o8EQ0g) | 6 | 手書きとタイピングを自分の勉強方法と結びつけられる |
| [Reading Aloud Helps Memory, But Not Comprehension](https://eikaiwa.dmm.com/app/daily-news/article/reading-aloud-helps-memory-but-not-comprehension/misF7t_fEe6tYz89ClN_mw) | 6 | 音読を使った英語学習について講師と直接話せる |
| [Thinking Longer Can Lead to Worse Decisions — Study](https://eikaiwa.dmm.com/app/daily-news/article/thinking-longer-can-lead-to-worse-decisions-study/JmexuFYKEfGdqwcU5IFbKg) | 6 | 考える時間と判断の質について、自分の経験から意見を言える |
| [Why Forgetting Your Phone Might Help Your Memory](https://eikaiwa.dmm.com/app/daily-news/article/why-forgetting-your-phone-might-help-your-memory/JUz38InxEfG_b69PXi9CQg) | 7 | スマートフォンへの依存と記憶の関係を考えられる |

#### 仕事・社会

| 記事 | Level | 選定理由 |
|---|:---:|---|
| [How to Make Time for 'Deep Work'](https://eikaiwa.dmm.com/app/daily-news/article/how-to-make-time-for-deep-work/3E1LiLRHEfCW3G8Ni9xBrQ) | 7 | 集中を妨げるものや、自分の仕事環境について話せる |
| [Can a Four-Day Week Work for Everyone?](https://eikaiwa.dmm.com/app/daily-news/article/can-a-four-day-week-work-for-everyone/InaxGA2nEfGbAo_15D7fIA) | 6 | 週休3日の利点と問題点を整理して議論できる |
| [Gaming Helps with Career Skills, Workers Say](https://eikaiwa.dmm.com/app/daily-news/article/gaming-helps-with-career-skills-workers-say/YzE5QEisEfGTux-bgf-GXw) | 7 | ゲームで得る能力が仕事に役立つかを話せる |

#### 歴史・文化・環境

| 記事 | Level | 選定理由 |
|---|:---:|---|
| [Museum of Failure Celebrates Inventors' Mistakes](https://eikaiwa.dmm.com/app/daily-news/article/museum-of-failure-celebrates-inventors-mistakes/5Gk4UlfGEe6Lr0cuKXA3zA) | 7 | 失敗した製品から、挑戦や失敗の価値について考えられる |
| [Heating Up History: The Story of the Microwave Oven](https://eikaiwa.dmm.com/app/daily-news/article/heating-up-history-the-story-of-the-microwave-oven/XLOYii-yEe61Dl8zPdtUag) | 6 | 身近な技術が生まれた歴史を専門知識なしで楽しめる |
| [Do Plastic Bag Bans Actually Work? Researchers Say Yes](https://eikaiwa.dmm.com/app/daily-news/article/do-plastic-bag-bans-actually-work-researchers-say-yes/xEvYEMH1Ee6lVS8za-Zqdg) | 7 | 環境政策が実際に効果を出すか議論できる |

この中では `3D-Printed Home` → `Writing by Hand` → `Museum of Failure` → `Four-Day Week` → `Wooden Satellite` の順がおすすめです。

### 選びやすい記事の傾向

- Levelは原則として制限しない（Level 7〜8でもDiscussionが身近なら優先）
- コンビニ、買い物、スマホ、食事、仕事、旅行、防災など日常と接点がある題材
- 新商品、生活習慣、海外との違い、生活に関わる制度
- 専門知識がなくても、自分の経験、日本との比較、賛否と理由で答えられるDiscussion
- 本文が多少難しくても、Discussionの質問を読んだ瞬間に具体例を思いつけるもの
