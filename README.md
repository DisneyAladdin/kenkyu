# 修論タイトル
トピックモデルにより話題集約されたノウハウサイト群の閲覧インタフェース

# Keywords
Web，情報検索，検索エンジン，トピックモデル，word2vec，話題集約

# 所属
筑波大学 システム情報工学研究科 知能機能システム専攻

# 大まかな流れ
・クエリ入力<br>
・検索エンジン・サジェスト収集<br>
・検索結果上位20位ずつ，ウェブページを収集<br>
・形態素解析（Mecab）<br>
・LDAトピックモデル（教師なし学習）<br>
・word2vec訓練（wikipedia+ウェブページ文書）<br>
・ウェブページにタグ付く検索エンジン・サジェスト同士のCos類似度からサブトピック生成<br>
・デモインタフェース（HTML）作成<br>
・トピックモデルの結果に対し，SVM（Support Vector Machine）を適用，ノウハウサイトの自動同定<br>
・同定されたノウハウサイト候補群およびデモインタフェースを入力に，「ノウハウちゃんねる」作成<br>

# Licence
CopyRight (c) 2018 Shuto Kawabata

Released under the MIT licence

https://opensource.org/licenses/MIT

# Author
川畑修人

Shuto Kawabata
