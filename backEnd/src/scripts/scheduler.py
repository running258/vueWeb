# API    http://pydoc.net/APScheduler/3.3.1/apscheduler.jobstores.mongodb/#sourcecode
# https://www.jianshu.com/p/4f5305e220f0
import time
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler 
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from src.dao.getMongo import getConfIni
from src.controller.runController import runController

scheduler = BackgroundScheduler ()

host = getConfIni().config.get("mongodb", "host")
port = getConfIni().config.get("mongodb", "port")
dbName = getConfIni().config.get("mongodb", "dbName")
client = MongoClient(host=host, port=int(port))
mongoCollection = MongoDBJobStore(database=dbName, client=client)
scheduler.add_jobstore(mongoCollection)


def runInter(projectId,interIdList):
    interBatJson = {
        "projectId": projectId,
        "interIdList": interIdList,
        "projectCollectionName": "interProject", 
        "interCollectionName": "inter",
        "loginEnvCollectionName": "interLoginEnv"
    }

    res = runController().runInterBat(interBatJson)
    print(str(res))
 

class jobController(object):

    def addJob(self,projectId,interIdList):
        job = scheduler.add_job(runInter, 'interval',args=[projectId,interIdList], seconds=5, id=projectId,replace_existing=True)
        return job

scheduler.start()
