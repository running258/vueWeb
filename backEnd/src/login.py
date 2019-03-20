import requests, json
from entity.tools import jsonLoad,getTime
from src.dao.getLoginEnvMongoDB import getLoginEnvMongoDB

class LoginWithMongo(object):
    
    def __init__(self,env,username,password):
        result = getLoginEnvMongoDB().getLoginEnvCollection(env)
        self.supplyUrl = result["supply"]["url"]
        self.supplyPath = result["supply"]["path"]
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
