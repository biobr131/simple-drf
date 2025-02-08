# Simple DRF

Django REST Frameworkのテンプレートレポジトリです。
主にDjango Adminの管理画面とSwagger UIを用いたデータベース管理を目的としたシンプルなリポジトリです。


## 環境構築方法

このリポジトリをクローンし，以下の手順を実行してください。

### Dockerを使用する場合

以下のコマンドで本番環境用のイメージがビルドされます。

```
docker compose build
```

開発環境用のイメージをビルドするには，

```
docker compose -f compose.dev.yaml build
```

### ローカル環境（Windows）を使用する場合

Python組み込みの`venv`モジュールを用い，仮想環境を構築します。
`Python 3.12`を推奨します。

```
python -m venv .venv
.venv¥Scripts¥activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
