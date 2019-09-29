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
        return '<Device %r>' % self.name

# 宣告DhtLog資料模型
class DhtLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)

    # 設定device_id欄位為與"Device資料模型"的"id欄位"關聯
    # 也就是device_id欄位內的值，"必須"是在"Device資料模型"的"id欄位"有的值之一
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'),
        nullable=False)

    # 建立關聯至"Device資料模型"的屬性"device"，並
    # 使"Device資料模型"有反向參考的屬性"dht_logs"，
    # 且採用lazy-loading方式載入相關資料
    device = db.relationship('Device',
        backref=db.backref('dht_logs', lazy=True))

    def __repr__(self):
        return '<DhtLog id:%r timestamp:%s temperature:%r humidity:%r>' % (
            self.id, self.timestamp, self.temperature, self.humidity)
