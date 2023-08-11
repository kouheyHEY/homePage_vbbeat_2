from flask import Flask, Blueprint
from hpvbbeat.const import Const

app = Flask(__name__)
app.config.from_object("hpvbbeat.config")

from hpvbbeat.views import views
from hpvbbeat.views import views_work

app.register_blueprint(views_work.bp)
app.jinja_env.globals.update(Const.__dict__)
