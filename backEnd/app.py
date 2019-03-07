import json
from flask import Flask, jsonify
from flask_cors import CORS

from src.dao.getProjectsMongoDB import getProjectsMongoDB

app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Hello World!')     


@app.route('/projects', methods=['GET'])
def getProjects():
    projectsList = getProjectsMongoDB().getAllProjects()
    jsonRe = json.dumps(projectsList,ensure_ascii=False)
    # print(jsonRe)
    return jsonify(jsonRe)


if __name__ == '__main__':
    print(getProjects())
    app.run()
