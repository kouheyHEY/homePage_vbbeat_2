from flask import Blueprint, render_template, request

bp = Blueprint("views_work", __name__, template_folder="templates")


@bp.route("/work/<string:category>/<int:id>")
def work_detail(category, id):
    return render_template("main/index.html")
