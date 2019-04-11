import requests, json
from src.entity.tools import jsonLoad,getTime
from src.controller.commonController import commonController

class LoginWithMongo(object):
    
    def __init__(self,loginEnvId,loginEnvCollectionName,username,password):
        result = commonController(loginEnvCollectionName).getById(loginEnvId)
        self.supplyUrl = result["supply"]["url"]
        self.supplyPath = result["supply"]["path"]
        self.hospUrl = result["hosp"]["url"]
        self.hospPath = result["hosp"]["path"]
        self.userName = username
        self.passWord = password

    def supplyLogin(self):
        userName = self.userName
        passWord = self.passWord
        loginParams = {"identifier":userName,"password":passWord,"_t":getTime().getTimestamp()}
        res = requests.post(self.supplyUrl+self.supplyPath,data=loginParams)
        authorization = json.loads(res.text)["result"]["token"]
        header = {"authorization":authorization}
        params = {"_t":getTime().getTimestamp()}
        res = requests.get(self.supplyUrl+"/api1/api/user/base/getUserRes",headers=header,data=params)
        return authorization
