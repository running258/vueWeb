from src.controller.controllerIndex import controllerIndex

class oesController(controllerIndex):

    def __init__(self):
        self.OESProject = controllerIndex().getOESProjectMongoDB()
        self.OESInter = controllerIndex().getOESInterMongoDB()

    #保存OES项目
    def saveOESProject(self,oesProjectInfo):
        OES_ID = oesProjectInfo["OES_ID"]
        oesProjectInfo.pop("OES_ID")
        if oesProjectInfo["OES_ID"] != '':
            updateRes = self.OESProject.updateOESProjectById(OES_ID,oesProjectInfo)
        else :
            OES_ID = self.OESProject.insertOESProject(oesProjectInfo)
        return  "done"

    #查看OES项目
    def getOESProjectList(self):
        resList = self.OESProject.getOESProjectList()
        for res in resList:
            res["_id"] = str(res["_id"])
        return  resList

    #根据ID查看OES项目详情
    def getOESProjectById(self,oesProjectId):
        res = self.OESProject.getOESProjectById(oesProjectId)
        res["_id"] = str(res["_id"])
        return res

    #删除OES项目
    def deleteOESProjectById(self,oesProjectId):
        res = self.OESProject.getOESProjectById(oesProjectId)
        OESInterList = res["OESInterList"]
        self.OESProject.deleteOESProjectById(oesProjectId)
        for OESInter in OESInterList:
            Inter_ID = va["Inter_ID"]
            self.OESInter.deleteOESInter(Inter_ID)
        return "done"

    #项目下新建OES接口
    def saveOESInter(self,OESInterInfo):
        oesProjectId = OESInterInfo["oesProjectId"]
        Inter_ID = OESInterInfo["Inter_ID"]
        InterName = OESInterInfo["InterName"]
        OESInterInfo.pop("oesProjectId")
        OESInterInfo.pop("Inter_ID")
        if Inter_ID != '':
            updateRes = self.OESInter.updateOESInterById(Inter_ID,OESInterInfo)
        else :
            newInter_ID = self.OESInter.insertOESInter(OESInterInfo)
            res = self.OESProject.getOESProjectById(self,oesProjectId)
            interJson = {'Inter_ID': str(newInter_ID), 'InterName': InterName}
            OESInterList = res["OESInterList"]
            OESInterList.append(interJson)
            res["OESInterList"] = OESInterList
            result = self.OESProject.updateOESProjectById(OES_ID,res)
        return  "done"

    #查看项目下所有OES接口
    def getOESProjectInterList(self,oesProjectId):
        res = self.OESProject.getOESProjectById(oesProjectId)
        OESInterList = res["OESInterList"]
        OESInterListInfo = []
        for OESInter in OESInterList:
            OES_ID = OESInter["OES_ID"]
            OESInterRes = self.OESInter.getOESInterById(OES_ID)
            OESInterRes["_id"] = str(OESInterRes["_id"])
            OESInterListInfo.append(OESInterRes)
        return OESInterListInfo

    #查看项目下OES接口详情
    def getOESInterById(self,oesInterId):
        OESinterInfo = self.OESInter.getOESInterById(oesInterId)
        return OESinterInfo

    #删除项目下va
    def deleteOESProjectInter(self,oesProjectId,oesInterId):
        projectInfo = self.OESProject.getOESProjectById(oesProjectId)
        OESInterList = projectInfo["OESInterList"]
        indexI = (i for i in VAList if i["OES_ID"] == oesInterId).__next__()
        OESInterList.remove(indexI)
        projectInfo["OESInterList"] = OESInterList
        updateProject = self.OESProject.updateOESProjectById(OES_ID,projectInfo)
        VADelRes = self.OESInter.deleteOESInter(oesInterId)
        return updateProject

    #接口运行
    def runOESInter(self,oesInterId):
        return "run"
