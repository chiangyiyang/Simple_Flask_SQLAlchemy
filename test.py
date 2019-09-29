from main import db, Device

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
device_a05 = Device.query.filter(Device.name=='a05').first()
print(type(device_a05))
print(device_a05)
print(device_a05.name, device_a05.longitude, device_a05.latitude)

# 觀察資料庫內容

