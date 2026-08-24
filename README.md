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

### 選びやすい記事の傾向

- Level 5〜6
- Food & Drink、Culture、Health & Lifestyle
- 新商品、生活習慣、海外のユニークな制度
- 専門知識がなくても、自分の経験や日本との比較で答えられるもの
