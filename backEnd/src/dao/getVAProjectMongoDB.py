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

    def updateProjectVAList(self, vaProjectName,newRes):
        result = self.collection.update({"vaProjectName": vaProjectName}, newRes)
        return result
        
    def getVAProjectsByProjectName(self, vaProjectName):
        result = self.collection.find_one({"vaProjectName": vaProjectName})
        return result

    # def updateProjectInter(self, projectName, interId, interName):
    #     updateInter = {'interId': str(interId), 'interName': interName}
    #     projectRes = self.getProjectsByProjectName(projectName)
    #     interfaces = projectRes["interfaces"]
    #     interfaces.append(updateInter)
    #     projectRes["interfaces"] = interfaces
    #     result = self.db.vaProject.update({"projectName": projectName}, projectRes)
    #     return result
