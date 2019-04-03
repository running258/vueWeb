from src.controller.controllerIndex import controllerIndex
from src.entity.tools import mask
from src.entity.tools import getTime
from src.entity.requestsTemp import oesProjectInter
import json

class runController(controllerIndex):

    def __init__(self):
        self.OESProject = controllerIndex().getOESProjectMongoDB()
        self.OESInter = controllerIndex().getOESInterMongoDB()

    def runOESInter(self,oesProjectId,oesInterId):
        projectInfo = self.OESProject.getOESProjectById(oesProjectId)
        interInfo = self.OESInter.getOESInterById(oesInterId)
        hospsignature = str(projectInfo["signature"])
        timeStamp = str(getTime().getTimestamp())
        hospId = str(projectInfo["hospId"])
        url = str(projectInfo["url"])
        path = str(interInfo["path"])
        signature = mask().sha256(hospsignature+timeStamp+hospId)
        params = {
            "header": {
                "msgId": "virtualOES",
                "msgVer": "1.0.0.1",
                "thirdPartyMsgVer": "虚拟OES",
                "timestamp": timeStamp,
                "signature": signature
	        },
            "body": interInfo["raw"]
        }
        header = {"content-type": "application/json"}
        params = json.dumps(params)
        path = url+path
        res = oesProjectInter().oesProjectRun(path,header,params)
        return res


