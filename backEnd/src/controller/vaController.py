from src.controller.controllerIndex import controllerIndex

class vaController(controllerIndex):

    def __init__(self):
        self.vaProject = controllerIndex().getVAProjectMongoDB()
        self.va = controllerIndex().getVAMongoDB()

    def insertVAProject(self,vaProjectInfo):
        res = self.vaProject.insertNewVAProject(vaProjectInfo)
        return  res

    def getVAProjectList(self,vaProjectName):
        res = self.vaProject.getVAProjectList(vaProjectName)
        return  res

    def getVAProjectsByProjectName(self,vaProjectName):
        res = self.vaProject.getVAProjectsByProjectName(vaProjectName)
        res["_id"] = str(res["_id"])
        return  res

    def insertVAInProject(self,VAInfo):
        vaProjectName = VAInfo["vaProjectName"]
        VAName = VAInfo["VAName"]
        VAInfo.pop("vaProjectName")
        VA_ID = self.va.insertVA(VAInfo)
        vaJson = {'VA_ID': str(VA_ID), 'VAName': VAName}
        projectRes = self.vaProject.getVAProjectsByProjectName(vaProjectName)
        vaList = projectRes["vaList"]
        vaList.append(vaJson)
        projectRes["vaList"] = vaList
        result = self.vaProject.updateProjectVAList(vaProjectName,projectRes)
        return  result

    #查看项目下所有VA
    def getProjectVAList(self,vaProjectName):
        res = self.vaProject.getVAProjectsByProjectName(vaProjectName)
        VAList = res["vaList"]
        VAListInfo = []
        for vaInfo in VAList:
            VA_ID = vaInfo["VA_ID"]
            VAListInfo.append(self.va.getVAId(VA_ID))
        return VAListInfo

    #访问 VA response
    def getVAResponse(self,vaProjectName,vaName):
        res = self.vaProject.getVAProjectsByProjectName(vaProjectName)
        VAList = res["vaList"]
        VA_ID = (i["VA_ID"] for i in VAList if i["VAName"] == vaName).__next__()
        res = self.va.getVAId(VA_ID)
        return res["response"]



