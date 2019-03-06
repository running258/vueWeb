from interfaceFrameWork.dao.getMongo import mongoConn

class getProjectsMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getProjectsCollection(self,projectName):
        result = self.db.projects.find_one({"projectName":projectName})
        return result
