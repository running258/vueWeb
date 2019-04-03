import json
from flask import Flask, jsonify,request
from flask_cors import CORS

from src.controller.oesController import oesController
from src.controller.vaController import vaController
from src.controller.envController import envController
from src.controller.interProjectController import interProjectController

from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB
from src.requestsTemp import requestsTemp

app = Flask(__name__)
CORS(app)

#获取所有环境地址
@app.route('/getAllLoginEnv', methods=['GET'])
def getAllLoginEnv():
    loginEnv = envController().getAllLoginEnv()
    return json.dumps(loginEnv)

#保存/更新环境信息
@app.route('/updateLoginEnv', methods=['POST'])
def updateLoginEnv():
    loginEnvJson = json.loads(request.get_data(as_text=True))
    updateRes = envController().updateLoginEnv(loginEnvJson)
    return "done"

#保存/更新环境信息
@app.route('/deleteLoginEnv', methods=['POST'])
def deleteLoginEnv():
    loginEnvId = request.get_data(as_text=True)
    deleteRes = envController().deleteLoginEnv(loginEnvId)
    return "done"

#-----------接口相关API-----------------
#查看所有接口项目
@app.route('/getInterProject', methods=['GET'])
def getInterProject():
    projectList = interProjectController().getInterProject()
    return json.dumps(projectList)

@app.route('/insertInterProject', methods=['POST'])
def insertNewProject():
    newProjectJson = json.loads(request.get_data(as_text=True))
    newProject = getProjectsMongoDB().insertNewProject(newProjectJson)
    return "done"


@app.route('/getProjectAndIntersByProjectName/<projectName>', methods=['GET'])
def getProjectAndIntersByProjectName(projectName):
    projectInfo = getProjectsMongoDB().getProjectsByProjectName(projectName)
    interList = projectInfo["interfaces"]
    interQueryList = []    
    for inter in interList:
        interId = inter["interId"]
        interName = inter["interName"]
        interInfo = getInterfacesMongoDB().getInterfacesCollectionWithInterIDAndName(interId,interName)
        interInfo["interId"] = interId
        interQueryList.append(interInfo)
    projectInfo["interfaces"] = interQueryList
    return json.dumps(projectInfo)

#get all interface by interName
@app.route('/interInfoById/<interId>', methods=['GET'])
def getInterInfoWithID(interId):
    interInfo = getInterfacesMongoDB().getInterfacesCollectionWithInterID(interId)
    return json.dumps(interInfo)

#call interface
@app.route('/runSingleInter', methods=['POST'])
def runSingleInter():
    singleInterJson = json.loads(request.get_data(as_text=True))
    sys = singleInterJson["sys"]
    env = singleInterJson["env"]
    username = singleInterJson["runUsername"]
    password = singleInterJson["runPassword"]
    if sys == "supply":
        res = requestsTemp(env,username,password).supplyRequests(singleInterJson)
        return json.dumps(res)

#save interface and update project
@app.route('/saveInterAndUpdateProject', methods=['POST'])
def saveInterAndUpdateProject():
    interJson = json.loads(request.get_data(as_text=True))
    projectName = interJson["projectName"]
    interName = interJson["interName"]
    if interJson["isNewUser"]:
        interJson["username"] = interJson["runUsername"]
        interJson["password"] = interJson["runPassword"]
    else:
        interJson["username"] = ""
        interJson["password"] = ""
    interJson.pop("isNewUser")
    interJson.pop("runUsername")
    interJson.pop("runPassword")
    interId = getInterfacesMongoDB().insertInterfacesCollection(interJson)
    getProjectsMongoDB().updateProjectInter(projectName,interId,interName)
    return "done"
# -------------------------------OES相关API-------------
#新建OES项目
@app.route('/saveOESProject', methods=['POST'])
def saveOESProject():
    oesProjectInfo = json.loads(request.get_data(as_text=True))
    res = oesController().saveOESProject(oesProjectInfo)
    return json.dumps(res)

#查看OES项目列表
@app.route('/getOESProjectList', methods=['GET'])
def getOESProjectList():
    projectName = request.args.get('projectName')
    res = oesController().getOESProjectList(projectName)
    return json.dumps(res)

#根据项目ID查看项目
@app.route('/getOESProjectById', methods=['GET'])
def getOESProjectById():
    oesProjectId = request.args.get('oesProjectId')
    res = oesController().getOESProjectById(oesProjectId)
    return json.dumps(res)

#删除OES项目
@app.route('/deleteOESProjectById', methods=['POST'])
def deleteOESProjectById():
    oesProjectId = request.get_data(as_text=True)
    deleteRes = oesController().deleteOESProjectById(oesProjectId)
    return "done"

#保存OES接口
@app.route('/saveOESInter', methods=['POST'])
def saveOESInter():
    OESInterInfo = json.loads(request.get_data(as_text=True))
    saveRes = oesController().saveOESInter(OESInterInfo)
    return str(saveRes)

#查看项目下所有OES接口
@app.route('/getOESProjectInterList', methods=['GET'])
def getOESProjectInterList():
    oesProjectId = request.args.get('oesProjectId')
    OESInterList = oesController().getOESProjectInterList(oesProjectId)
    return json.dumps(OESInterList)

#根据ID查看项目下指定OES接口
@app.route('/getOESInterById', methods=['GET'])
def getOESInterById():
    oesInterId = request.args.get('oesInterId')
    OESInterInfo = oesController().getOESInterById(oesInterId)
    return json.dumps(OESInterInfo)

#根据ID删除VA
@app.route('/deleteOESProjectInter', methods=['GET'])
def deleteOESProjectInter():
    oesProjectId = request.args.get('oesProjectId')
    oesInterId = request.args.get('oesInterId')
    deleteRes = oesController().deleteOESProjectInter(oesProjectId,oesInterId)
    return "done"

#运行oes接口
@app.route('/runOESInter', methods=['POST'])
def runOESInter():
    oesInterId = request.args.get('oesInterId')
    runRes = oesController().runOESInter(oesInterId)
    return str(runRes)

# -------------------------------VA相关API-------------
#新建VA项目
@app.route('/insertVAProject', methods=['POST'])
def insertVAProject():
    vaProjectInfo = json.loads(request.get_data(as_text=True))
    res = vaController().insertVAProject(vaProjectInfo)
    return json.dumps(res)

#更新VA项目
@app.route('/updateVAProject', methods=['POST'])
def updateVAProject():
    vaProjectInfo = json.loads(request.get_data(as_text=True))
    res = vaController().updateVAProject(vaProjectInfo)
    return json.dumps(res)

#删除VA项目
@app.route('/deleteVAProject', methods=['POST'])
def deleteVAProject():
    projectId = request.get_data(as_text=True)
    deleteRes = vaController().deleteVAProject(projectId)
    return "done"

#查看VAProjectList
@app.route('/getVAProjectList', methods=['GET'])
def getVAProjectList():
    vaProjectName = request.args.get('vaProjectName')
    res = vaController().getVAProjectList(vaProjectName)
    return json.dumps(res)

#根据项目名查看项目
@app.route('/getVAProjectsByProjectName', methods=['GET'])
def getVAProjectsByProjectName():
    vaProjectName = request.args.get('vaProjectName')
    res = vaController().getVAProjectsByProjectName(vaProjectName)
    return json.dumps(res)

#根据项目ID查看项目
@app.route('/getVAProjectsByProjectId', methods=['GET'])
def getVAProjectsByProjectId():
    vaProjectId = request.args.get('vaProjectId')
    res = vaController().getVAProjectsByProjectId(vaProjectId)
    return json.dumps(res)

#插入VA
@app.route('/insertVA', methods=['POST'])
def insertVA():
    VAInfo = json.loads(request.get_data(as_text=True))
    VA_ID = vaController().insertVAInProject(VAInfo)
    return str(VA_ID)

#查看项目下所有VA
@app.route('/getProjectVAList', methods=['GET'])
def getProjectVAList():
    vaProjectId = request.args.get('vaProjectId')
    projectVAList = vaController().getProjectVAList(vaProjectId)
    return json.dumps(projectVAList)

#根据ID查看项目下指定VA
@app.route('/getProjectVA/<VA_ID>', methods=['GET'])
def getProjectVA(VA_ID):
    VAInfo = vaController().getProjectVA(VA_ID)
    return json.dumps(VAInfo)

#根据ID删除VA
@app.route('/deleteProjectVA', methods=['GET'])
def deleteProjectVA():
    vaProjectName = request.args.get('vaProjectName')
    VA_ID = request.args.get('VA_ID')
    deleteRes = vaController().deleteProjectVA(vaProjectName,VA_ID)
    return "done"

#更新项目下VA
@app.route('/updateProjectVA', methods=['POST'])
def updateProjectVA():
    VAInfo = json.loads(request.get_data(as_text=True))
    updateRes = vaController().updateProjectVA(VAInfo)
    return str(updateRes)

#获取response
@app.route('/<vaProjectName>/getVAResponse/<vaName>', methods=['GET'])
def getVAResponse(vaProjectName,vaName):
    vaRes = vaController().getVAResponse(vaProjectName,vaName)
    return json.dumps(vaRes)
# ---------------------------------

@app.route('/testPage')
def testPage():
    return "test page"


if __name__ == '__main__':
    app.run()
