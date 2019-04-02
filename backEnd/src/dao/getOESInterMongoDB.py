from src.dao.getMongo import mongoConn
from bson.objectid import ObjectId

class getOESInterMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()
        self.collection = self.db['OESInter']

    def insertOESInter(self, OESInterInfo):
        result = self.collection.insert(OESInterInfo)
        return result

    def getOESInterById(self,OES_ID):
        result = self.collection.find_one({"_id":ObjectId(oesProjectId)})
        result["_id"] = str(result["_id"])
        return result

    def updateOESInterById(self, Inter_ID, OESInterInfo):
        result = self.collection.update({"_id": ObjectId(Inter_ID)}, OESInterInfo)
        return result

    def deleteOESInter(self, Inter_ID):
        result = self.collection.remove({"_id":ObjectId(Inter_ID)})
        return result