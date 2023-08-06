from flask import Flask, Blueprint

app = Flask(__name__)
app.config.from_object("hpvbbeat.config")

from hpvbbeat.views import views
from hpvbbeat.views import views_work

app.register_blueprint(views_work.bp)
