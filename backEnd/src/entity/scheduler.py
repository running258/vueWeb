# API    http://pydoc.net/APScheduler/3.3.1/apscheduler.jobstores.mongodb/#sourcecode
# https://www.jianshu.com/p/4f5305e220f0
import time
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from src.dao.getMongo import getConfIni
from src.controller.runController import runController

scheduler = BackgroundScheduler()



host = getConfIni().config.get("mongodb", "host")
port = getConfIni().config.get("mongodb", "port")
dbName = getConfIni().config.get("mongodb", "dbName")
client = MongoClient(host=host, port=int(port))
mongoCollection = MongoDBJobStore(database=dbName, client=client)
scheduler.add_jobstore(mongoCollection)



@scheduler.scheduled_job("interval", seconds=5)
def my_job():

    interBatJson = {
        "projectId": "5cb5634a8591d44ad083a73b",
        "interIdList": ["5cb563568591d44ad083a73d", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        "projectCollectionName": "interProject",
        "interCollectionName": "inter",
        "loginEnvCollectionName": "interLoginEnv"
    }

    res = runController().runInterBat(interBatJson)
    print(str(res))
 
scheduler.start()
