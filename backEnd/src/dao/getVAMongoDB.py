import os,sys
curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)
from getMongo import mongoConn

class getVAMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getVAByName(self,VAName):
        result = self.db.virtualAssert.find_one({"VAName":VAName})
        result.pop("_id")
        return result

    def insertVA(self,VAName,res):
        result = self.db.virtualAssert.insert({"VAName":VAName,"response":res})
        return result
