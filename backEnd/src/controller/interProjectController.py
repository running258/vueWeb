from src.controller.controllerIndex import controllerIndex

class interProjectController(controllerIndex):

    def __init__(self):
        self.interProject = controllerIndex().getProjectsMongoDB()

    #新建接口项目
    def getInterProject(self):
        res = self.interProject.getInterProject()
        return  res

    