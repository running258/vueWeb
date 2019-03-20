from src.dao.getMongo import mongoConn
from bson.objectid import ObjectId


class getLoginEnvMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getAllLoginEnv(self):
        loginList = []
        results = self.db.loginEnv.find()
        for result in results:
            result["_id"] = str(result["_id"])
            loginList.append(result)
        return loginList

    def getLoginEnvCollection(self,env):
        result = self.db.loginEnv.find_one({"env":env})
        result.pop("_id")
        return result
        
    def insertLoginEnvCollection(self,loginInfo):
        result = self.db.loginEnv.insert(loginInfo)
        return result

    def updateLoginEnv(self, loginId, loginInfo):
        result = self.db.loginEnv.update({"_id":ObjectId(loginId)}, loginInfo)
        return result

