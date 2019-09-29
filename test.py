from main import db, Device
from sqlalchemy import exc


# 建立資料庫
# db.create_all()


# 清空資料庫
# db.drop_all()


# 建立Device資料模型
# model = Device(name='d01', longitude='121.5', latitude='23.5')

# print(type(model))
# print(model)
# print(model.name, model.longitude, model.latitude)

# 將資料加入到本次資料庫存取的Session中
# db.session.add(model)

# 將本次資料庫存取的Session寫入資料庫，寫入前資料庫必須要已經建立
# db.session.commit()


# 一次新增多筆資料
# for i in range(2,10):
#     db.session.add(
#         Device(name='a0%d' % i,
#             longitude=121 + (i/10),
#             latitude=23 + (i/20))
#     )
# db.session.commit()


# 查詢所有Device的資料
# all_devices = Device.query.all()

# print(type(all_devices))
# print(all_devices)
# print(type(all_devices[0]))
# print(all_devices[0])
# print(all_devices[0].name, all_devices[0].longitude, all_devices[0].latitude)


# 查詢第3比Device的資料
# device_3 = Device.query.get(3)
# print(type(device_3))
# print(device_3)
# print(device_3.name, device_3.longitude, device_3.latitude)


# 查詢name='a05'的Device資料
# device_a05 = Device.query.filter_by(name='a05').first()
# 另一種查法
# device_a05 = Device.query.filter(Device.name=='a05').first()
# print(type(device_a05))
# print(device_a05)
# print(device_a05.name, device_a05.longitude, device_a05.latitude)


# 修改一筆資料
# 將Device.name='d01'的資料，改成name='a01'
# 首先找Device.name='d01'的資料
# model = Device.query.filter_by(name='d01').first()
# if model is not None:       # 查詢結果檢查
#     print("\t找到Device.name='d01'的資料==>", model)

#     # 修改內容
#     model.name = 'a01'

#     # 加入Session
#     db.session.add(model)

#     # 寫回資料庫
#     db.session.commit()


# 再修改一筆資料
# 將Device.name='a02'的資料，也改成name='a01'
# 首先找Device.name='a02'的資料
# model = Device.query.filter_by(name='a02').first()
# if model is not None:       # 查詢結果檢查
#     print("\t找到Device.name='a02'的資料==>", model)

#     # 修改內容
#     model.name = 'a01'

#     # 加入Session
#     db.session.add(model)

#     # 寫回資料庫
#     try:
#         db.session.commit()
#     except exc.IntegrityError as error:
#         print(error)
#         print("資料庫中已經有一筆資料name='a01'")


# 刪除一筆資料
# 將Device.name='a01'的資料刪除
# 首先找Device.name='a02'的資料
# model = Device.query.filter_by(name='a01').first()
# if model is not None:       # 查詢結果檢查
#     print("\t找到Device.name='a01'的資料==>", model)
    
#     # 將刪除資訊加入Session中
#     db.session.delete(model)

#     # 寫回資料庫
#     db.session.commit()


# 再新增一筆Device.name='a01'的資料
model = Device(name='a01')

db.session.add(model)

print('commit前')
print(model)
print('name:', model.name)
print('id:', model.id)

# 寫回資料庫
try:
    db.session.commit()
except exc.IntegrityError as error:
    print(error)
    print("資料庫中已經有一筆資料name='a01'")

print('commit後')
print(model)
print('name:', model.name)
print('id:', model.id)


# 觀察資料庫內容，資料已經新增
# 觀察commit前，id=None
# 觀察commit後，id=10
# 這id是SQLAlchemy規定每個資料模型都要有的，其值由資料庫產生
# 在commit前，尚未存取資料庫，所以id=None
# 在commit後，資料庫給一個目前最大的id值10，而不是1