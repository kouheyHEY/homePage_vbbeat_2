from hpvbbeat import db
from datetime import datetime

# workテーブル
# カラム一覧
# work_id     作品id
# work_name   作品名
# work_detail 作品の説明
# thumbneil   サムネイル
# upddate     更新日時
# createdate  作成日時
# upduser     更新ユーザ
# createuser  作成ユーザ


class Work(db.Model):
    # テーブル名
    __tablename__ = "work"
    # カラムの定義
    work_id = db.Column(db.Integer, primary_key=True)
    work_name = db.Column(db.String(64))
    work_detail = db.Column(db.String(256))
    thumbneil = db.Column(db.String(64))

    upddate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    createdate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    upduser = db.Column(db.String(64))
    createuser = db.Column(db.String(64))
