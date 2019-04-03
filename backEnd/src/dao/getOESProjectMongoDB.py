from src.dao.getMongo import mongoConn
from bson.objectid import ObjectId
class getOESProjectMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()
        self.collection = self.db['OESProject']

    def getOESProjectList(self,projectName):
        projectList = []
        results = self.collection.find({'projectName': {'$regex': '.?'+projectName+'.?'}})
        for result in results:
            result["_id"] = str(result["_id"])
            projectList.append(result)
        return projectList

    def insertOESProject(self, oesProjectInfo):
        result = self.collection.insert(oesProjectInfo)
        return result

    def getOESProjectById(self, oesProjectId):
        result = self.collection.find_one({"_id":ObjectId(oesProjectId)})
        result["_id"] = str(result["_id"])
        return result

    def updateOESProjectById(self, oesProjectId,oesProjectInfo):
        result = self.collection.update({"_id": ObjectId(oesProjectId)}, oesProjectInfo)
        return result

    def deleteOESProjectById(self, oesProjectId):
        result = self.collection.remove({"_id":ObjectId(oesProjectId)})
        return result