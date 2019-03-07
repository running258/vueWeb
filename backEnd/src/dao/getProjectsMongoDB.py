import os,sys
curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)
from getMongo import mongoConn

class getProjectsMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getAllProjects(self):
        projectsList = []
        results = self.db.projects.find()
        for result in results:
            projectsList.append(result)
        print(projectsList)

    def getProjectsByProjectName(self,projectName):
        result = self.db.projects.find_one({"projectName":projectName})
        return result


