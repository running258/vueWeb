import json
from flask import Flask, jsonify,request,Response
from flask_cors import CORS

from src.controller.commonController import commonController
from src.controller.interProjectController import interProjectController

from src.controller.oesController import oesController
from src.controller.runController import runController
from src.controller.vaController import vaController

from src.scripts.scheduler import jobController

app = Flask(__name__)
CORS(app)



# ------通用Path-------------
# 保存
@app.route('/save', methods=['POST'])
def save():
    jsonInfo = json.loads(request.get_data(as_text=True))
    collectionName = jsonInfo["collectionName"]
    res = commonController(collectionName).save(jsonInfo)
    return res

# 获取List/名称查询
@app.route('/getList', methods=['GET'])
def getList():
    name = request.args.get('name')
    collectionName = request.args.get('collectionName')
    res = commonController(collectionName).getList(name)
    return json.dumps(res)

# 根据ID查看
@app.route('/getById', methods=['GET'])
def getById():
    _id = request.args.get('_id')
    collectionName = request.args.get('collectionName')
    res = commonController(collectionName).getById(_id)
    return json.dumps(res)

# 根据ID删除
@app.route('/deleteById', methods=['GET'])
def deleteById():
    _id = request.args.get('_id')
    collectionName = request.args.get('collectionName')
    res = commonController(collectionName).deleteById(_id)
    return res

# 根据ID获取接口项目下所有接口
@app.route('/getProjectAndIntersByProjectId', methods=['GET'])
def getProjectAndIntersByProjectId():
    _id = request.args.get('_id')
    projectCollectionName = request.args.get('projectCollectionName')
    interCollectionName = request.args.get('interCollectionName')
    projectInfo = commonController(projectCollectionName).getProjectAndIntersByProjectId(_id,interCollectionName)
    return json.dumps(projectInfo)

#-----------接口相关API-----------------
#save interface and update project
@app.route('/saveInterAndUpdateProject', methods=['POST'])
def saveInterAndUpdateProject():
    interJson = json.loads(request.get_data(as_text=True))
    projectCollectionName = interJson["projectCollectionName"]
    interCollectionName = interJson["interCollectionName"]
    insertInfo = interProjectController(projectCollectionName).saveInterAndUpdateProject(interCollectionName,interJson)
    return "done"

#单接口运行
@app.route('/runInterProjectInter', methods=['GET'])
def runInterProjectInter():
    projectId = request.args.get('projectId')
    interId = request.args.get('interId')
    projectCollectionName = request.args.get('projectCollectionName')
    interCollectionName = request.args.get('interCollectionName')
    loginEnvCollectionName = request.args.get('loginEnvCollectionName')
    res = runController().runInterProjectInter(projectId,interId,projectCollectionName,interCollectionName,loginEnvCollectionName)
    return json.dumps(res)

#批量运行
@app.route('/runInterBat', methods=['POST'])
def runInterBat():
    interBatJson = json.loads(request.get_data(as_text=True))
    res = runController().runInterBat(interBatJson)
    return json.dumps(res)
# -------------------------------OES可视化相关API-------------




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
@app.route('/runOESInter', methods=['GET'])
def runOESInter():
    oesProjectId = request.args.get('oesProjectId')
    oesInterId = request.args.get('oesInterId')
    runRes = runController().runOESInter(oesProjectId,oesInterId)
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
@app.route('/<vaProjectName>/getVAResponse/<vaName>', methods=['GET','POST'])
def getVAResponse(vaProjectName,vaName):
    vaRes = vaController().getVAResponse(vaProjectName,vaName)
    return Response(json.dumps(vaRes), mimetype='application/json')
    # return json.dumps(vaRes)
# ---------------------------------

# @app.route('/testPage')
# def testPage():
#     jobController().test()
#     jobController().addJob('5cb5634a8591d44ad083a73b',["5cb563568591d44ad083a73d", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
#     return "test page"


if __name__ == '__main__':
    app.run()
