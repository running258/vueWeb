from src.dao.getMongo import mongoConn
from bson.objectid import ObjectId


class getLoginEnvMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()
        self.collection = self.db['loginEnv']

    def getAllLoginEnv(self):
        loginList = []
        results = self.collection.find()
        for result in results:
            result["_id"] = str(result["_id"])
            loginList.append(result)
        return loginList

    def getLoginEnvCollection(self,env):
        result = self.collection.find_one({"env":env})
        result["_id"] = str(result["_id"])
        return result
        
    def insertLoginEnvCollection(self,loginInfo):
        result = self.collection.insert(loginInfo)
        return result

    def updateLoginEnv(self, loginId, loginInfo):
        result = self.collection.update({"_id":ObjectId(loginId)}, loginInfo)
        return result

    def removeLoginEnv(self,loginEnvId):
        result = self.collection.remove({"_id":ObjectId(loginEnvId)})
        return result

