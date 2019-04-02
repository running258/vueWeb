from src.controller.controllerIndex import controllerIndex

class envController(controllerIndex):

    def __init__(self):
        self.loginEnv = controllerIndex().getLoginEnvMongoDB()

    #获取所有环境地址
    def getAllLoginEnv(self):
        res = self.loginEnv.getAllLoginEnv()
        return  res

    #更新环境地址
    def updateLoginEnv(self,loginEnvJson):
        if loginEnvJson["_id"]!='':
            _id = loginEnvJson["_id"]
            loginEnvJson.pop("_id")
            updateResult = self.loginEnv.updateLoginEnv(_id,loginEnvJson)
        else:
            loginEnvJson.pop("_id")
            insertResult = self.loginEnv.insertLoginEnvCollection(loginEnvJson)
        return  "done"

    #删除环境地址
    def deleteLoginEnv(self,loginEnvId):
        res = self.loginEnv.removeLoginEnv(loginEnvId)
        return  res