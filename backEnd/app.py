import json
from flask import Flask, jsonify,request
from flask_cors import CORS

from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB
from src.dao.getLoginEnvMongoDB import getLoginEnvMongoDB

app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Hello World!')     


@app.route('/projects', methods=['GET'])
def getProjects():
    projectsList = getProjectsMongoDB().getAllProjects()
    return json.dumps(projectsList)

@app.route('/interInfo/<interName>', methods=['GET'])
# def getInterInfo(interfaceId,interName):
def getInterInfo(interName):
    interInfo = getInterfacesMongoDB().getInterfacesCollection("5c7e21b2a76ccc33d0dde741",interName)
    # interInfo = getInterfacesMongoDB().getInterfacesCollection(interfaceId,interName)
    return json.dumps(interInfo)

@app.route('/loginEnv/<sys>', methods=['GET'])
def getLoginEnv(sys):
    loginEnv = getLoginEnvMongoDB().getLoginEnvCollection(sys)
    return json.dumps(loginEnv)
    
@app.route('/runSingleInter', methods=['POST'])
def runSingleInter():
    print(json.loads(request.get_data(as_text=True)))
    # loginEnv = getLoginEnvMongoDB().getLoginEnvCollection(sys)
    # return json.dumps(loginEnv)
    return ('hello')

if __name__ == '__main__':
    # getLoginEnv("supply")
    app.run()
