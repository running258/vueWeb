import requests, json
from entity.tools import jsonLoad,getTime
from src.dao.getLoginEnvMongoDB import getLoginEnvMongoDB

class LoginWithMongo(object):
    
    def __init__(self, sys,env="staging"):
        result = getLoginEnvMongoDB().getLoginEnvCollection(sys,env)
        self.url = result["url"]
        self.path = result["path"]
        self.userName = result["userName"]
        self.passWord = result["passWord"]

    def supplyLogin(self):
        userName = self.userName
        passWord = self.passWord
        loginParams = {"identifier":userName,"password":passWord,"_t":getTime().getTimestamp()}
        res = requests.post(self.url+self.path,data=loginParams)
        authorization = json.loads(res.text)["result"]["token"]
        header = {"authorization":authorization}
        params = {"_t":getTime().getTimestamp()}
        res = requests.get(self.url+"/api1/api/user/base/getUserRes",headers=header,data=params)
        return authorization
