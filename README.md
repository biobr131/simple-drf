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


## Djangoのセットアップ方法

`.env.example`を参考に，`.env`（開発環境を使用する場合は`.env.dev`）を作成してください。

### Dockerを用いる場合

`collectstatic`によりCSSファイル等が`static`ディレクトリ下に集められます。
`makemigrations`および`migrate`により，`models.py`で定義されたモデル群がデータベースに反映されます。
その後，`createsuperuser`により，管理者権限を持つユーザーを作成します。
開発環境を用いる場合は上記と同様に，`-f compose.dev.yaml`のオプションを追加してください。

```
docker compose up -d
docker compose exec drf python manage.py makemigrations accounts
docker compose exec drf python manage.py migrate accounts
docker compose exec drf python manage.py migrate
docker compose exec drf python manage.py createsuperuser
docker compose down
```


### ローカル環境（Windows）を用いる場合

仮想環境を起動した上で，上記のDockerと同様に以下を実行します。

```
.venv¥Scripts¥activate
python manage.py collectstatic
python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py migrate
python manage.py createsuperuser
```
