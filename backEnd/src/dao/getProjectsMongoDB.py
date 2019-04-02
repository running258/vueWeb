from src.dao.getMongo import mongoConn
from bson.objectid import ObjectId

class getProjectsMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getAllProjects(self):
        projectsList = []
        results = self.db.projects.find()
        for result in results:
            result["_id"] = str(result["_id"])
            projectsList.append(result)
        return projectsList

    def insertNewProject(self, newProjectJson):
        result = self.db.projects.insert(newProjectJson)
        return result

    def getProjectsByProjectName(self, projectName):
        result = self.db.projects.find_one({"projectName": projectName})
        result["_id"] = str(result["_id"])
        return result

    def updateProjectInter(self, projectName, interId, interName):
        updateInter = {'interId': str(interId), 'interName': interName}
        projectRes = self.getProjectsByProjectName(projectName)
        interfaces = projectRes["interfaces"]
        interfaces.append(updateInter)
        projectRes["interfaces"] = interfaces
        result = self.db.projects.update({"projectName": projectName}, projectRes)
        return result
