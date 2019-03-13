import requests, json,os,sys

curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)


# from login import Login
from login import LoginWithMongo
from entity.tools import jsonLoad,getTime
from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB

class requestsTemp(LoginWithMongo):

    def supplyRequests(self, jsonData, returnType = "json", extraParams={},  extraPath=""):
        authorization = LoginWithMongo("supply").supplyLogin()
        # authorization = Login().supplyLogin()
        data = jsonData
        method = data["method"]
        path = data["path"]+extraPath
        header = data["header"]
        header["authorization"] = authorization
        params = data["params"]
        params["_t"] = getTime().getTimestamp()
        params = {**params, **extraParams}  # merge and update params with extraParams 

        if method.lower() == "post":
            params = json.dumps(params)
            res = requests.post(self.url+path, data=params,headers=header)
        elif method.lower() == "get":
            res = requests.get(self.url+path, params=params,headers=header)
        elif method.lower() == "put":
            params = json.dumps(params)
            res = requests.put(self.url+path, data=params,headers=header)
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
            res = requests.post(self.url+path, data=params,headers=header)
        elif method.lower() == "get":
            res = requests.get(self.url+path, params=params,headers=header)
        elif method.lower() == "put":
            params = json.dumps(params)
            res = requests.put(self.url+path, data=params,headers=header)
        else:
            raise Exception("no requests named %s"% (method))
        # return different type of response with returnType
        if returnType.lower() == "json":
            return res.json()
        elif returnType.lower() == "string" or returnType.lower() == "text":
            return res.text

