# DMM Daily News collector

DMM Daily Newsの一覧ページに含まれるサーバー生成HTMLから、記事タイトル、レベル、公開日時、URLを抽出します。ブラウザやJavaScript実行環境は不要です。

```bash
python3 collect_daily_news.py --pretty
python3 collect_daily_news.py --min-level 5 --max-level 7 --limit 20 --pretty
python3 collect_daily_news.py --all-pages --pretty --output daily_news_articles.json
```

個人学習の範囲で、サイトに負荷をかけない頻度で実行してください。

## レッスン候補

食事・飲み物・運動などの身近な話題、海外との違い、少し意外な商品や制度を中心にした候補です。上から順におすすめです。

| # | 記事 | Level | 選定理由 |
|---:|---|:---:|---|
| 1 | [Breakfast: A World of Choices](https://eikaiwa.dmm.com/app/daily-news/article/breakfast-a-world-of-choices/kHuhFLXfEeijR-febh7u2g) | 6 | 国ごとの朝食を、自分の習慣や旅行経験と比較しやすい |
| 2 | [Milk Comics: A Fun Way to Get Kids Drinking Milk](https://eikaiwa.dmm.com/app/daily-news/article/milk-comics-a-fun-way-to-get-kids-drinking-milk/PIyeOHdTEe6o2D_H24l9QQ) | 6 | 行動を促すユニークな仕組みについて話せる |
| 3 | [Coke and Pickles? Star Reveals Unusual Drink Choice](https://eikaiwa.dmm.com/app/daily-news/article/coke-and-pickles-star-reveals-unusual-drink-choice/NFeYqoxjEe-S8ocO5ijmVQ) | 6 | 変わった組み合わせを試したいか、気軽に意見を言える |
| 4 | [Out and About: US vs. UK Shopping Language](https://eikaiwa.dmm.com/app/daily-news/article/out-and-about-us-vs-uk-shopping-language/NVBgsITLEe-aw2uJaE17mg) | 5 | 米英の身近な言葉の違いを学べる |
| 5 | [Italian Named the World's Most Attractive Accent](https://eikaiwa.dmm.com/app/daily-news/article/italian-named-the-worlds-most-attractive-accent/2EDJQtSxEe6Vskt6iJKogg) | 5 | 好きな言語の音や聞き取りやすい英語について話せる |
| 6 | [No-Buy List — A Money-Saving Trend for 2025](https://eikaiwa.dmm.com/app/daily-news/article/no-buy-list-a-money-saving-trend-for-2025/YjeJGNmuEe-k8X8msTx7Vg) | 5 | 買い物や節約を自分の生活に結びつけやすい |
| 7 | [All Aboard: The Origins of the Sushi Train](https://eikaiwa.dmm.com/app/daily-news/article/all-aboard-the-origins-of-the-sushi-train/SlRkoHUKEe-NLLPyxdA4Fg) | 6 | 身近な日本文化を講師へ説明しやすい |
| 8 | [Palau to Reward Tourists Who Respect the Environment](https://eikaiwa.dmm.com/app/daily-news/article/palau-to-reward-tourists-who-respect-the-environment/PRNf1NyDEeyH8mfM5CE61w) | 6 | ユニークな報奨制度と旅行の話を組み合わせられる |

最初に選ぶなら `Breakfast` → `Milk Comics` → `US vs. UK Shopping Language` の順がおすすめです。

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

### 選びやすい記事の傾向

- Level 5〜6
- Food & Drink、Culture、Health & Lifestyle
- 新商品、生活習慣、海外のユニークな制度
- 専門知識がなくても、自分の経験や日本との比較で答えられるもの
