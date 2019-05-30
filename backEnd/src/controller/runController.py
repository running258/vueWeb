from src.dao.getOESProjectMongoDB import getOESProjectMongoDB
from src.dao.getOESInterMongoDB import getOESInterMongoDB
from src.controller.commonController import commonController

from src.entity.tools import mask
from src.entity.tools import getTime
from src.entity.requestsTemp import oesProjectInter
from src.entity.requestsTemp import requestsTemp
import json

class runController(object):

    def __init__(self):
        self.OESProject = getOESProjectMongoDB()
        self.OESInter = getOESInterMongoDB()

    def runOESInter(self,oesProjectId,oesInterId):
        projectInfo = self.OESProject.getOESProjectById(oesProjectId)
        interInfo = self.OESInter.getOESInterById(oesInterId)
        hospsignature = str(projectInfo["signature"])
        timeStamp = str(getTime().getTimestamp())
        hospId = str(projectInfo["hospId"])
        url = str(projectInfo["url"])
        path = str(interInfo["path"])
        signature = mask().sha256(hospsignature+timeStamp+hospId)
        params = {
            "header": {
                "msgId": "virtualOES",
                "msgVer": "1.0.0.1",
                "thirdPartyMsgVer": "虚拟OES",
                "timestamp": timeStamp,
                "signature": signature
	        },
            "body": {
                "data":interInfo["raw"]
            }

        }
        header = {"content-type": "application/json"}
        params = json.dumps(params)
        path = url+path
        res = oesProjectInter().oesProjectRun(path,header,params)
        return res

    def runInterProjectInter(self,projectId,interId,projectCollectionName,interCollectionName,loginEnvCollectionName):
        projectInfo = commonController(projectCollectionName).getById(projectId)
        interInfo = commonController(interCollectionName).getById(interId)
        loginEnvId = projectInfo["loginEnvId"]
        loginEnvInfo = commonController(loginEnvCollectionName).getById(loginEnvId)
        supplyUsername = projectInfo["supplyUsername"]
        supplyPassword = projectInfo["supplyPassword"]
        hospUsername = projectInfo["hospUsername"]
        hospPassword = projectInfo["hospPassword"]
        env = loginEnvInfo["name"]
        sys = interInfo["sys"]
        supplyUrl = loginEnvInfo["supply"]["url"]
        supplyPath = loginEnvInfo["supply"]["path"]
        hospUrl = loginEnvInfo["hosp"]["url"]
        hospPath = loginEnvInfo["hosp"]["path"]
        runUsername = ''
        runPassword = ''
        if sys == "supply":
            if interInfo["username"] != '':
                runUsername = interInfo["username"]
                runPassword = interInfo["password"]
            else:
                runUsername = supplyUsername
                runPassword = supplyPassword
        elif sys == "hosp":
            if interInfo["username"] != '':
                runUsername = interInfo["username"]
                runPassword = interInfo["password"]
            else:
                runUsername = hospUsername
                runUsername = hospPassword
        interInfo["expectedResult"] = str(interInfo["expectedResult"]).replace('\\"','"')
        expectedResult = interInfo["expectedResult"]
        runJson = {
            "sys": sys,
            "path": interInfo["path"],
            "method": interInfo["method"],
            "header": interInfo["header"],
            "params": interInfo["params"],
            "runUsername": runUsername,
            "runPassword": runPassword
        }
        if sys == "supply":
            res = requestsTemp(loginEnvId,loginEnvCollectionName,runUsername,runPassword).supplyRequests(runJson)
        resDict = {}
        resDict["res"] = res
        resStr = json.dumps(res,ensure_ascii=False)
        if expectedResult!='':
            if expectedResult in resStr:
                isPass = True
            else:
                isPass = False
        else:
            isPass = ''
        resDict["isPass"] = isPass
        return resDict

    def runInterBat(self,interBatJson):
        projectId = interBatJson["projectId"]
        interIdList = interBatJson["interIdList"]
        projectCollectionName = interBatJson["projectCollectionName"]
        interCollectionName = interBatJson["interCollectionName"]
        loginEnvCollectionName = interBatJson["loginEnvCollectionName"]
        resList = []
        for index,interId in enumerate(interIdList):
            resList.append('')
            if interId != '':
                res = self.runInterProjectInter(projectId,interId,projectCollectionName,interCollectionName,loginEnvCollectionName)
                resList[index] = res
        return resList


