from main import db, Device

# 建立資料庫
# db.create_all()

# 清空資料庫
# db.drop_all()

# 建立Device資料模型
model = Device(name='d01', longitude='121.5', latitude='23.5')

print(type(model))
print(model)
print(model.name, model.longitude, model.latitude)

# 將資料加入到本次資料庫存取的Session中
db.session.add(model)

# 觀察資料庫內容
# 目前尚未有新增資料