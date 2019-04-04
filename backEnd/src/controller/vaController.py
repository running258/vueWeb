from src.controller.controllerIndex import controllerIndex

class vaController(controllerIndex):

    def __init__(self):
        self.vaProject = controllerIndex().getVAProjectMongoDB()
        self.va = controllerIndex().getVAMongoDB()

    #新建VA项目
    def insertVAProject(self,vaProjectInfo):
        res = self.vaProject.insertNewVAProject(vaProjectInfo)
        return  res

    #更新VA项目
    def updateVAProject(self,vaProjectInfo):
        vaProjectId = vaProjectInfo["_id"]
        vaProjectInfo.pop("_id")
        res = self.vaProject.updateVAProjectById(vaProjectId,vaProjectInfo)
        return  res

    #删除VA项目
    def deleteVAProject(self,projectId):
        res = self.vaProject.getVAProjectsByProjectId(projectId)
        VAList = res["vaList"]
        self.vaProject.deleteProjectById(projectId)
        for va in VAList:
            VA_ID = va["VA_ID"]
            self.va.deleteVA(VA_ID)
        return "done"

    #获取所有VA项目/查询
    def getVAProjectList(self,vaProjectName):
        res = self.vaProject.getVAProjectList(vaProjectName)
        return  res

    #根据id查看项目信息
    def getVAProjectsByProjectId(self,_id):
        res = self.vaProject.getVAProjectsByProjectId(_id)
        res["_id"] = str(res["_id"])
        return res

    #项目下新建VA
    def insertVAInProject(self,VAInfo):
        projectId = VAInfo["projectId"]
        VAName = VAInfo["VAName"]
        VAInfo.pop("projectId")
        VA_ID = self.va.insertVA(VAInfo)
        vaJson = {'VA_ID': str(VA_ID), 'VAName': VAName}
        projectRes = self.vaProject.getVAProjectsByProjectId(projectId)
        vaList = projectRes["vaList"]
        vaList.append(vaJson)
        projectRes["vaList"] = vaList
        result = self.vaProject.updateProjectVAList(projectId,projectRes)
        return  result

    #查看项目下所有VA
    def getProjectVAList(self,vaProjectId):
        res = self.vaProject.getVAProjectsByProjectId(vaProjectId)
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

    #查看项目下VA详情
    def getProjectVA(self,VA_ID):
        VAInfo = self.va.getVAId(VA_ID)
        return VAInfo

    #删除项目下va
    def deleteProjectVA(self,projectId,VA_ID):
        projectInfo = self.vaProject.getVAProjectsByProjectId(projectId)
        VAList = projectInfo["vaList"]
        indexI = (i for i in VAList if i["VA_ID"] == VA_ID).__next__()
        VAList.remove(indexI)
        projectInfo["vaList"] = VAList
        updateProject = self.vaProject.updateProjectVAList(projectId,projectInfo)
        VADelRes = self.va.deleteVA(VA_ID)
        return updateProject

    #更新项目下va
    def updateProjectVA(self,VAInfo):
        VA_ID = VAInfo["VA_ID"]
        VAInfo.pop("VA_ID")
        VADelRes = self.va.updateVA(VA_ID,VAInfo)
        return VADelRes
