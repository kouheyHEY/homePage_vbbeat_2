from flask import Blueprint, render_template, request
from hpvbbeat.const import Const

bp = Blueprint("views_work", __name__, template_folder="templates")


@bp.route("/work/<string:_category>/<int:_id>")
def work_detail(_category, _id):
    # 渡すパラメータの定義
    params: dict = {}
    # カテゴリ
    params[Const.CNT_PARAM["CATEGORY"]] = _category
    # id
    params[Const.CNT_PARAM["ID"]] = _id
    # タイトル
    params[Const.CNT_PARAM["TITLE"]] = "作品１"
    # 更新日付
    params[Const.CNT_PARAM["UPDDATE"]] = "2023-08-05 12:15:23"

    return render_template("main/work.html", params=params)
