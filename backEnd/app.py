import json
from flask import Flask, jsonify,request
from flask_cors import CORS

from src.controller.vaController import vaController

from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB
from src.dao.getLoginEnvMongoDB import getLoginEnvMongoDB
from src.dao.getVAMongoDB import getVAMongoDB
# from record.record import record
from src.requestsTemp import requestsTemp

app = Flask(__name__)
CORS(app)

#get all projects 
@app.route('/getProjects', methods=['GET'])
def getProjects():
    projectsList = getProjectsMongoDB().getAllProjects()
    return json.dumps(projectsList)

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

@app.route('/getAllLoginEnv', methods=['GET'])
def getAllLoginEnv():
    loginEnv = getLoginEnvMongoDB().getAllLoginEnv()
    return json.dumps(loginEnv)

@app.route('/updateLoginEnv', methods=['POST'])
def updateLoginEnv():
    loginEnvJson = json.loads(request.get_data(as_text=True))
    if loginEnvJson["_id"]!='':
        _id = loginEnvJson["_id"]
        loginEnvJson.pop("_id")
        updateResult = getLoginEnvMongoDB().updateLoginEnv(_id,loginEnvJson)
    else:
        loginEnvJson.pop("_id")
        insertResult = getLoginEnvMongoDB().insertLoginEnvCollection(loginEnvJson)
    return "done"

@app.route('/insertNewProject', methods=['POST'])
def insertNewProject():
    newProjectJson = json.loads(request.get_data(as_text=True))
    newProject = getProjectsMongoDB().insertNewProject(newProjectJson)
    return "done"

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

#get all project VA
@app.route('/getProjectVAList', methods=['GET'])
def getProjectVAList():
    vaProjectName = request.args.get('vaProjectName')
    projectVAList = vaController().getProjectVAList(vaProjectName)
    return json.dumps(projectVAList)

#查看项目下VA
@app.route('/getProjectVA/<VA_ID>', methods=['GET'])
def getProjectVA(VA_ID):
    VAInfo = vaController().getProjectVA(VA_ID)
    return json.dumps(VAInfo)

#delete VA by id
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


#get VA env
@app.route('/Record', methods=['POST'])
def Record(): 
    runEnv = json.loads(request.get_data(as_text=True))
    vaRes = record().setUP(runEnv)
    return "done"

@app.route('/testPage')
def testPage():
    return "test page"


if __name__ == '__main__':
    app.run()
