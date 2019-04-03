from src.controller.controllerIndex import controllerIndex
from bson.objectid import ObjectId


class oesController(controllerIndex):

    def __init__(self):
        self.OESProject = controllerIndex().getOESProjectMongoDB()
        self.OESInter = controllerIndex().getOESInterMongoDB()

    #保存OES项目
    def saveOESProject(self,oesProjectInfo):
        OES_ID = oesProjectInfo["OES_ID"]
        oesProjectInfo.pop("OES_ID")
        if OES_ID != '':
            updateRes = self.OESProject.updateOESProjectById(OES_ID,oesProjectInfo)
        else :
            OES_ID = self.OESProject.insertOESProject(oesProjectInfo)
        return  "done"

    #查看OES项目
    def getOESProjectList(self,projectName):
        resList = self.OESProject.getOESProjectList(projectName)
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
            Inter_ID = OESInter["Inter_ID"]
            self.OESInter.deleteOESInter(Inter_ID)
        return "done"

    #项目下新建OES接口
    def saveOESInter(self,OESInterInfo):
        oesProjectId = OESInterInfo["oesProjectId"]
        Inter_ID = OESInterInfo["Inter_ID"]
        InterName = OESInterInfo["interName"]
        OESInterInfo.pop("oesProjectId")
        OESInterInfo.pop("Inter_ID")
        if Inter_ID != '':
            updateRes = self.OESInter.updateOESInterById(Inter_ID,OESInterInfo)
            return  "done"
        else :
            newInter_ID = self.OESInter.insertOESInter(OESInterInfo)
            res = self.OESProject.getOESProjectById(oesProjectId)
            interJson = {'Inter_ID': str(newInter_ID), 'InterName': InterName}
            OESInterList = res["OESInterList"]
            OESInterList.append(interJson)
            res["OESInterList"] = OESInterList
            res["_id"] = ObjectId(res["_id"])
            result = self.OESProject.updateOESProjectById(oesProjectId,res)
            return result

    #查看项目下所有OES接口
    def getOESProjectInterList(self,oesProjectId):
        res = self.OESProject.getOESProjectById(oesProjectId)
        OESInterList = res["OESInterList"]
        OESInterListInfo = []
        for OESInter in OESInterList:
            Inter_ID = OESInter["Inter_ID"]
            OESInterRes = self.OESInter.getOESInterById(Inter_ID)
            OESInterRes["_id"] = str(OESInterRes["_id"])
            OESInterListInfo.append(OESInterRes)
        return OESInterListInfo

    #查看项目下OES接口详情
    def getOESInterById(self,oesInterId):
        OESinterInfo = self.OESInter.getOESInterById(oesInterId)
        return OESinterInfo

    #删除项目下Inter
    def deleteOESProjectInter(self,oesProjectId,oesInterId):
        projectInfo = self.OESProject.getOESProjectById(oesProjectId)
        OESInterList = projectInfo["OESInterList"]
        indexI = (i for i in OESInterList if i["Inter_ID"] == oesInterId).__next__()
        OESInterList.remove(indexI)
        projectInfo["OESInterList"] = OESInterList
        projectInfo["_id"] = ObjectId(projectInfo["_id"])
        updateProject = self.OESProject.updateOESProjectById(oesProjectId,projectInfo)
        deleteRes = self.OESInter.deleteOESInter(oesInterId)
        return updateProject

    #接口运行
    def runOESInter(self,oesInterId):
        return "run"
