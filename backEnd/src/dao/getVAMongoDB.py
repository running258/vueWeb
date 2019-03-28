import os,sys
curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)
from getMongo import mongoConn
from bson.objectid import ObjectId

class getVAMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getVAByName(self,VAName):
        result = self.db.virtualAssert.find_one({"VAName":VAName})
        result.pop("_id")
        return result

    def getVAList(self):
        VAList = []
        results = self.db.virtualAssert.find()
        for result in results:
            result["_id"] = str(result["_id"])
            VAList.append(result)
        return VAList

    def insertVA(self,VAInfo):
        result = self.db.virtualAssert.insert(VAInfo)
        return result

    def updateVA(self, VA_ID, VAInfo):
        result = self.db.virtualAssert.update({"_id":ObjectId(VA_ID)}, VAInfo)
        return result

    def deleteVA(self,VA_ID):
        result = self.db.virtualAssert.remove({"_id":ObjectId(VA_ID)})
        return result

