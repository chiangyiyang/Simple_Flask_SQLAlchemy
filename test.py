from main import db, Device

# 建立資料庫
db.create_all()

# 清空資料庫
# db.drop_all()

# 建立Device資料模型
model = Device(name='d01', longitude='121.5', latitude='23.5')

print(type(model))
print(model)
print(model.name, model.longitude, model.latitude)

# 將資料加入到本次資料庫存取的Session中
db.session.add(model)

# 將本次資料庫存取的Session寫入資料庫，寫入前資料庫必須要已經建立
db.session.commit()

# 觀察資料庫內容
# 資料沒有新增，有sqlalchemy.exc.IntegrityError的錯誤發生
# 這是因為資料庫中已經有一筆資料name='d01'，依據Device資料模型
# name必須是"唯一"，因此無法再新增一筆name='d01'的資料