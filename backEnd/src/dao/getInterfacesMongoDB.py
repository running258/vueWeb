import os,sys,json
curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)
from getMongo import mongoConn
from bson.objectid import ObjectId

class getInterfacesMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getInterfacesCollectionWithInterName(interName):
        result = self.db.interfaces.find({"interName":interName})
        result.pop("_id")
        return result

    def getInterfacesCollectionWithInterID(self,interfaceId):
        result = self.db.interfaces.find_one({"_id":ObjectId(interfaceId)})
        result.pop("_id")
        return result
    
    def getInterfacesCollectionWithInterIDAndName(self,interfaceId,interName):
        result = self.db.interfaces.find_one({"_id":ObjectId(interfaceId),"interName":interName})
        result.pop("_id")
        return result

    def insertInterfacesCollection(self,interData):
        interData.pop("projectName")
        result = self.db.interfaces.insert(interData)
        return result

