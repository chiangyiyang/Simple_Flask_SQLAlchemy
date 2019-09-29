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

# 觀察資料庫內容
# 目前尚未有新增資料