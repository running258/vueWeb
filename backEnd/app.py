import json
from flask import Flask, jsonify
from flask_cors import CORS

from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB

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
    print(interInfo)
    return json.dumps(interInfo)

if __name__ == '__main__':
    # getInterInfo("5c7e21b2a76ccc33d0dde741","addRole")
    app.run()
