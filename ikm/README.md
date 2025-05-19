# [IKM] このサイトにアクセスできません

- [ICTSC2024 本戦 問題解説: [IKM] このサイトにアクセスできません](https://blog.icttoracon.net/2025/03/31/ictsc2024final/ikm/)

## 概要

あなたは、自宅で Web サーバと DNS サーバ (権威サーバ・フルリゾルバ) を運用している。  
HTTPS レコードを登録し、client から nginx に立てた Web サイト にアクセスできる環境を作りたいと考えていたがうまくいかない。  
この問題を解決し快適な自宅サーバ環境を手に入れよう。

## 前提条件

- それぞれのサーバに Knot DNS, Knot Resolver, Nginx は構築済み
- nginx は HTTPS でアクセスが可能
- client には nginx にアクセスする Python プログラムがある
  - ３分毎に `/home/user/src/firefox.py` が実行される
  - ログファイルが同一階層に保存される
  - 手動実行は以下のコマンドでできる
    - `/home/user/src/.venv/bin/python /home/user/src/firefox.py`

### 制約

- client は問題ネットワーク上で構築したフルリゾルバ以外の手段で名前解決をしてはいけない
- 追加でソフトウェアをインストールしてはいけない
- 既存ファイルの編集でのみファイル操作を許可する
  - ファイルを編集する際は最低限の修正で問題を解決する必要がある
  - 今後の運用を見据えた修正など、本問題の解決に直接関係しない変更は減点対象となる
- Knot Resolver の設定を変更してはいけない
- nginx には SSH ログインできない
- client の Python プログラムを変更してはいけない

## 初期状態

- client の `/home/user/src/firefox.py` を実行すると nginx にアクセスできない

## 終了状態

- client の `/home/user/src/firefox.py` を実行すると５秒以内に 200 OK で Web ページのソースが取得できる
  - ログファイルの抜粋を報告書に添付すること
- 本トラブルの再発防止のために、原因を詳細に記述すること

## ネットワーク図

![topology](./docs/topology.drawio.svg)
