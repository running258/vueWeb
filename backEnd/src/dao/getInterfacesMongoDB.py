import os,sys,json
curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)
from getMongo import mongoConn
from bson.objectid import ObjectId

class getInterfacesMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getInterfacesCollection(self,interfaceId,interName):
        result = self.db.interfaces.find_one({"_id":ObjectId(interfaceId),"interName":interName})
        result.pop("_id")

        # print(result)
        # print(type(result))

        return result

# getInterfacesMongoDB().getInterfacesCollection("5c7e21b2a76ccc33d0dde741","addRole")