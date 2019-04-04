from src.dao.getMongo import mongoConn
from bson.objectid import ObjectId

class getVAProjectMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()
        self.collection = self.db['vaProject']

    def insertNewVAProject(self, vaProjectJson):
        result = self.collection.insert_one(vaProjectJson)
        insertId = result.inserted_id
        return str(insertId)

    def getVAProjectList(self,vaProjectName):
        vaProjectsList = []
        results = self.collection.find({'vaProjectName': {'$regex': '.?'+vaProjectName+'.?'}})
        for result in results:
            result["_id"] = str(result["_id"])
            vaProjectsList.append(result)
        return vaProjectsList

    def updateProjectVAList(self, projectId,newRes):
        result = self.collection.update({"_id": ObjectId(projectId)}, newRes)
        return result

    #根据ID更新项目
    def updateVAProjectById(self, vaProjectId,vaProjectInfo):
        result = self.collection.update({"_id":ObjectId(vaProjectId)}, vaProjectInfo)
        return result

    #根据ID删除项目
    def deleteProjectById(self, vaProjectId):
        result = self.collection.remove({"_id":ObjectId(vaProjectId)})
        return result
        
    def getVAProjectsByProjectName(self, vaProjectName):
        result = self.collection.find_one({"vaProjectName": vaProjectName})
        return result

    def getVAProjectsByProjectId(self, _id):
        result = self.collection.find_one({"_id":ObjectId(_id)})
        return result

