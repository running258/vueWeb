import configparser, os
from pymongo import MongoClient

class getConfIni(object):

    def __init__(self):
        curPath = os.path.dirname(os.path.realpath(__file__))
        confPath = os.path.join(curPath, "..\..\conf.ini")
        self.config = configparser.ConfigParser()
        self.config.read(confPath,encoding="utf-8")

class mongoConn(getConfIni):

    def getConnection(self,dbName=None):
        host = self.config.get("mongodb","host")
        port = self.config.get("mongodb","port")
        if dbName == None:
            dbName = self.config.get("mongodb","dbName")
        else:
            dbName = dbName
        client = MongoClient(host=host, port=int(port))
        db = client[dbName]
        return db
    
    def getCollection(self,collectionName,dbName=None):
        db = self.getConnection(dbName)
        collection = self.config.get("CollectionName",collectionName)
        dbCollection = db[collection]
        return dbCollection