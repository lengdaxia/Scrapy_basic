import pymongo

mongo_url = '127.0.0.1:27017'
connection = pymongo.MongoClient(mongo_url)
# tdb = connection["movies"]
tdb = connection["Test2"]
# douban = tdb["douban"]
douban = tdb["Novel"]


data1 = {'name':"肖申克的救赎",'age':6}
data2 = {'name':"美丽心灵",'age':19,'topic':""}
data3 = {'name':"西西里的美丽传说",'age':6,'dirctor':"unknow"}


# douban.insert(data2)
# douban.remove({'name':"肖申克的救赎"})
# douban.insert(data1)
# douban.insert_many([data2,data3])


r = douban.find({},{"BookChaptersUrl":1})
for url in r:
    print(url["BookChaptersUrl"])

print("数据库操作完成")


