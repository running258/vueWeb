import requests, json,os,sys

curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)

from login import Login
from login import LoginWithMongo
from entity.tools import jsonLoad,getTime
from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB

class requestsTemp(Login):

    def supplyRequestsMongo(self,projectName,interName,returnType = "json", extraParams={},  extraPath=""):
        authorization = LoginWithMongo("supply").supplyLogin()
        projectsInterfaces = getProjectsMongoDB().getProjectsCollection(projectName)["interfaces"]
        interId = (pi["_id"] for pi in projectsInterfaces if pi["interName"]==interName).__next__()
        interInfo = getInterfacesMongoDB().getInterfacesCollection(interId,interName)
        method = interInfo["method"]
        path = interInfo["path"]+extraPath
        header = interInfo["header"]
        header["authorization"] = authorization
        params = interInfo["params"]
        params["_t"] = getTime().getTimestamp()
        params = {**params, **extraParams}  # merge the params and update params by extraParams 
        if method.lower() == "post":
            params = json.dumps(params)
            res = requests.post(self._supplyUrl+path, data=params,headers=header)
        elif method.lower() == "get":
            res = requests.get(self._supplyUrl+path, params=params,headers=header)
        elif method.lower() == "put":
            params = json.dumps(params)
            res = requests.put(self._supplyUrl+path, data=params,headers=header)
        else:
            raise Exception("no requests named %s"% (method))
        # return different type of response with returnType
        if returnType.lower() == "json":
            return res.json()
        elif returnType.lower() == "string" or returnType.lower() == "text":
            return res.text
res = requestsTemp().supplyRequestsMongo("demoTest","addRole")
print(res)
