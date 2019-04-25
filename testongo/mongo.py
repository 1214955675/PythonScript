import pymongo
import pandas as pd

from pymongo import MongoClient
client = MongoClient('52.15.219.168',28018)
#client = MongoClient('mongodb://localhost:27017')
fans=client.imapi.u_fans;
# data = pd.DataFrame(list(fans.find({"userId":10000})))
data = list(fans.find({"userId":10000}))
listdata=[]
a=0
for dataitem in data:
    # dataitem.pop('_id')
    # dataitem['userId']=10015
    if a%2==0:
        print(dataitem)
        fans.delete_one(dataitem)
    a=a+1
    # listdata.append(dataitem)
# fans.insert_many(listdata)
# 选择需要显示的字段
# data = data[['_id', 'toUserId','userId']]
# data=data[['time','toUserId','userId']]
# data[['userId']]=10015
# print(data)
# print("2222222222222222222222222")
# fans.insert_many(data)
# 打印输出
print("suc")
# print(one)
