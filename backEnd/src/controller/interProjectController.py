from src.controller.controllerIndex import controllerIndex

class interProjectController(controllerIndex):

    def __init__(self):
        self.interProject = controllerIndex().getInterProjectMongoDB()

    #获取所有项目/查询
    def getProjectList(self,projectName):
        resultList = []
        res = self.interProject.getInterProjectList(projectName)
        for result in res:
            result["_id"] = str(result["_id"])
            projectList.append(result)
        return  projectList

    # #接口项目保存
    # def saveProject(self,projectInfo):

        

    #     res = self.interProject.getInterProjectList(projectName)
    #     for result in res:
    #         result["_id"] = str(result["_id"])
    #         projectList.append(result)
    #     return  projectList
    