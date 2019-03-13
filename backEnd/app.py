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
    print(projectsList)
    return json.dumps(projectsList)

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
    # res = requestsTemp("supply").supplyRequestsMongo("demoTest","addRole")
    res = requestsTemp("supply").supplyRequests(singleInterJson)
    # loginEnv = getLoginEnvMongoDB().getLoginEnvCollection(sys)
    # return json.dumps(loginEnv)
    return json.dumps(res)

#save interface and update project
@app.route('/saveInterAndUpdateProject', methods=['POST'])
def saveInterAndUpdateProject():
    interJson = json.loads(request.get_data(as_text=True))
    projectName = interJson["projectName"]
    interName = interJson["interName"]
    interId = getInterfacesMongoDB().insertInterfacesCollection(interJson)
    print(interId)
    getProjectsMongoDB().updateProjectInter(projectName,interId,interName)
    return "done"

#get VA env
@app.route('/getVA/<vaName>', methods=['GET'])
def getVA(vaName):
    vaRes = getVAMongoDB().getVAByName(vaName)
    return json.dumps(vaRes)

if __name__ == '__main__':
    # getLoginEnv("supply")
    app.run()
