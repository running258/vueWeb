from src.dao.getMongo import mongoConn
from bson.objectid import ObjectId

class getCommonMongoDB(mongoConn):

    def __init__(self, collectionName):
        self.collection = mongoConn().getCollection(collectionName)

    # 获取全部list/根据名称查询
    def getList(self, name):
        result = self.collection.find({'name': {'$regex': '.?'+name+'.?'}})
        return result

    # 根据ID查看
    def getById(self, _id):
        result = self.collection.find_one({"_id":ObjectId(_id)})
        return result
    
    # 数据插入
    def insert(self, insertJson):
        result = self.collection.insert_one(insertJson)
        return result

    # 根据ID更新
    def updateById(self, _id, updateJson):
        result = self.collection.update_one({"_id": ObjectId(_id)}, updateJson)
        return result

    # 根据ID删除
    def deleteById(self, _id):
        result = self.collection.delete_one({"_id":ObjectId(_id)})
        return result

    

