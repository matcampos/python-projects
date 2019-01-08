from mongo_connection import MongoConnection
from bson.objectid import ObjectId

con = MongoConnection.connect(MongoConnection)

users = con["users"]

for u in users.find():
    print(u)

user = users.find_one({"email": "matheus.campos@fcamara.com.br"})

print(user)

def findById(id):
    idToFind = ObjectId(id)
    return users.find_one({"_id": idToFind})

userByObjId = findById("5c1943d64d9ff90f93ce46c3")

print("user by objId", userByObjId)



def returnArr():
    return [users.find(), users.count()]

[ result, count ] = returnArr()

for r in result:
    print(r)

print(count)