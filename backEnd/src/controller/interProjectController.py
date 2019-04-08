from src.controller.commonController import commonController

class interProjectController(commonController):

    def __init__(self,collectionName):
        self.projectController = commonController(collectionName)

    # 新建接口并更新项目
    def saveInterAndUpdateProject(self,interCollectionName,interJson):
        interName = interJson["name"]
        projectId = interJson["projectId"]
        interId = interJson["_id"]
        if interJson["isNewUser"]:
            interJson["username"] = interJson["runUsername"]
            interJson["password"] = interJson["runPassword"]
        else:
            interJson["username"] = ""
            interJson["password"] = ""
        interJson.pop("isNewUser")
        interJson.pop("runUsername")
        interJson.pop("runPassword")
        interJson.pop("projectId")
        interJson.pop("_id")
        interJson.pop("interCollectionName")
        interJson.pop("projectCollectionName")
        if interId=='':
            interId = commonController(interCollectionName).insert(interJson)
            projectInfo = self.projectController.getById(projectId)
            projectInfo.pop("_id")
            interList = projectInfo["list"]
            interList.append({
                "interId": str(interId),
                "interName": interName
            })
            projectInfo["list"] = interList
            updateRes = self.projectController.updateById(projectId,projectInfo)
        else:
            updateRes = commonController(interCollectionName).updateById(interId,interJson)
        return "done"



   
