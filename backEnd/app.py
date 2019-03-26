import json
from flask import Flask, jsonify,request
from flask_cors import CORS

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

#get VA env
@app.route('/getVA/<vaName>', methods=['GET'])
def getVA(vaName):
    vaRes = getVAMongoDB().getVAByName(vaName)
    return json.dumps(vaRes)

#get all VA
@app.route('/VAList', methods=['GET'])
def vaList():
    vaList = getVAMongoDB().getVAList()
    return json.dumps(vaList)

@app.route('/insertVA', methods=['POST'])
def insertVA():
    VAInfo = json.loads(request.get_data(as_text=True))
    VA_ID = getVAMongoDB().insertVA(VAInfo)
    return str(VA_ID)

#delete VA by id
@app.route('/deleteVA', methods=['POST'])
def deleteVA():
    VA_ID = request.get_data(as_text=True)
    print(VA_ID)
    deleteRes = getVAMongoDB().deleteVA(VA_ID)
    return "done"

#get VA env
@app.route('/Record', methods=['POST'])
def Record():
    runEnv = json.loads(request.get_data(as_text=True))
    vaRes = record().setUP(runEnv)
    return "done"


if __name__ == '__main__':
    app.run()
