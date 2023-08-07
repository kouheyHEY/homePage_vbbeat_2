from flask import Blueprint, render_template, request

bp = Blueprint("views_work", __name__, template_folder="templates")


@bp.route("/work/<string:_category>/<int:_id>")
def work_detail(_category, _id):
    return render_template("main/work.html", category=_category, id=_id)
