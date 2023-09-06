# Fibonacci

1.
動作するプログラム一式
zipで固めたものでもgithubのリポジトリでもどちらでも良い＞github
githubで提出いただく場合、リポジトリ名は「fib_api」でお願いします
2.
ソースコードの構成、概要を説明するドキュメント
リポジトリに含めて良い
3.
実際に動いている環境のエンドポイントURL
https://colab.research.google.com/notebooks/intro.ipynb
動いている環境であればどんな環境でも問わない

ただのPythonのままだとHTTPと対話できないからFlaskとかで対話可能な形式にする必要がある

何度もfibonacci関数が呼び出された計算量が多くなってるからキャッシュのリセットが必要
https://qiita.com/simonritchie/items/2ae080691e956e2978aa
