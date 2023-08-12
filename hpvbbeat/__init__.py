from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from hpvbbeat.const import Const

# アプリの生成
app = Flask(__name__)
app.config.from_object("hpvbbeat.config")
# データベース設定
db = SQLAlchemy(app)

from hpvbbeat.views import views
from hpvbbeat.views import views_work

# ルーティングファイルの分割を可能にするための記述
app.register_blueprint(views_work.bp)
# jinjaテンプレートで、pythonで定義した定数を使用できるようにする
app.jinja_env.globals.update(Const.__dict__)
