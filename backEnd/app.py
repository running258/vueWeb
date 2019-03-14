import json
from flask import Flask, jsonify,request
from flask_cors import CORS

from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB
from src.dao.getLoginEnvMongoDB import getLoginEnvMongoDB
from src.dao.getVAMongoDB import getVAMongoDB
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


@app.route('/insertNewProject', methods=['POST'])
def insertNewProject():
    newProjectJson = json.loads(request.get_data(as_text=True))
    newProject = getProjectsMongoDB().insertNewProject(newProjectJson)
    return "done"
    # return json.dumps(newProject)


#get all interface by interName
@app.route('/interInfo/<interId>', methods=['GET'])
def getInterInfoWithID(interId):
    interInfo = getInterfacesMongoDB().getInterfacesCollectionWithInterID(interId)
    return json.dumps(interInfo)

#get sys env
@app.route('/loginEnv/<sys>', methods=['GET'])
def getLoginEnv(sys):
    loginEnv = getLoginEnvMongoDB().getLoginEnvCollection(sys)
    return json.dumps(loginEnv)
    
#call interface
@app.route('/runSingleInter', methods=['POST'])
def runSingleInter():
    singleInterJson = json.loads(request.get_data(as_text=True))
    res = requestsTemp("supply").supplyRequests(singleInterJson)
    return json.dumps(res)

#save interface and update project
@app.route('/saveInterAndUpdateProject', methods=['POST'])
def saveInterAndUpdateProject():
    interJson = json.loads(request.get_data(as_text=True))
    projectName = interJson["projectName"]
    interName = interJson["interName"]
    interId = getInterfacesMongoDB().insertInterfacesCollection(interJson)
    getProjectsMongoDB().updateProjectInter(projectName,interId,interName)
    return "done"

#get VA env
@app.route('/getVA/<vaName>', methods=['GET'])
def getVA(vaName):
    vaRes = getVAMongoDB().getVAByName(vaName)
    return json.dumps(vaRes)

if __name__ == '__main__':
    app.run()
