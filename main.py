import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 取得目前檔案的存放目錄
basedir = os.path.abspath(os.path.dirname(__file__))
# 設定SQLite資料庫儲存路徑，注意:儲存路徑需要有存取權限
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "sqlite:///" + os.path.join(basedir, "data.sqlite")
# 關閉"追蹤修改功能"，以節省資源
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False       
# 建立資料庫物件
db = SQLAlchemy(app)

# 宣告Device資料模型
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    def __repr__(self):
        return '<User %r>' % self.username
