import requests, json,os,sys

# from login import Login
from src.entity.tools import jsonLoad,getTime
from src.entity.login import LoginWithMongo
from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB

class requestsTemp(LoginWithMongo):

    def supplyRequests(self, jsonData, returnType = "json", extraParams={},  extraPath=""):
        data = jsonData
        env = jsonData["env"]
        authorization = LoginWithMongo(env,jsonData["runUsername"],jsonData["runPassword"]).supplyLogin()
        method = data["method"]
        path = data["path"]+extraPath
        header = data["header"]
        header["authorization"] = authorization
        params = data["params"]
        params["_t"] = getTime().getTimestamp()
        params = {**params, **extraParams}  # merge and update params with extraParams 

        if method.lower() == "post":
            params = json.dumps(params)
            res = requests.post(self.supplyUrl+path, data=params,headers=header)
        elif method.lower() == "get":
            res = requests.get(self.supplyUrl+path, params=params,headers=header)
        elif method.lower() == "put":
            params = json.dumps(params)
            res = requests.put(self.supplyUrl+path, data=params,headers=header)
        else:
            raise Exception("no requests named %s"% (method))

        # return different type of response with returnType
        if returnType.lower() == "json":
            return res.json()
        elif returnType.lower() == "string" or returnType.lower() == "text":
            return res.text

    def supplyRequestsMongo(self,projectName,interName,returnType = "json", extraParams={},  extraPath=""):
        authorization = LoginWithMongo("supply").supplyLogin()
        projectsInterfaces = getProjectsMongoDB().getProjectsByProjectName(projectName)["interfaces"]
        interId = (pi["interId"] for pi in projectsInterfaces if pi["interName"]==interName).__next__()
        interInfo = getInterfacesMongoDB().getInterfacesCollectionWithInterIDAndName(interId,interName)
        method = interInfo["method"]
        path = interInfo["path"]+extraPath
        header = interInfo["header"]
        header["authorization"] = authorization
        params = interInfo["params"]
        params["_t"] = getTime().getTimestamp()
        params = {**params, **extraParams}  # merge and update params with extraParams 
        if method.lower() == "post":
            params = json.dumps(params)
            res = requests.post(self.supplyUrl+path, data=params,headers=header)
        elif method.lower() == "get":
            res = requests.get(self.supplyUrl+path, params=params,headers=header)
        elif method.lower() == "put":
            params = json.dumps(params)
            res = requests.put(self.supplyUrl+path, data=params,headers=header)
        else:
            raise Exception("no requests named %s"% (method))
        # return different type of response with returnType
        if returnType.lower() == "json":
            return res.json()
        elif returnType.lower() == "string" or returnType.lower() == "text":
            return res.text

class oesProjectInter(object):

    def oesProjectRun(self,path,header,params):
        res = requests.post(path,headers=header,data=params,verify=False)
        return res.json()