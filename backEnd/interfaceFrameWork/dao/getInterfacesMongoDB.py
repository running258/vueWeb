from interfaceFrameWork.dao.getMongo import mongoConn
from bson.objectid import ObjectId

class getInterfacesMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getInterfacesCollection(self,interfaceId,interName):
        result = self.db.interfaces.find_one({"_id":ObjectId(interfaceId),"interName":interName})
        return result
