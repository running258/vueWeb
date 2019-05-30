from src.dao.getCommonMongoDB import getCommonMongoDB

class commonController():

    def __init__(self,collectionName,dbName=None):
        self.commonDao = getCommonMongoDB(collectionName,dbName)
        
    # 获取所有数据/查询
    def getList(self,name):
        resultList = []
        res = self.commonDao.getList(name)
        for result in list(res):
            result["_id"] = str(result["_id"])
            resultList.append(result)
        return  resultList

    # 根据ID获取数据
    def getById(self,_id):
        res = self.commonDao.getById(_id)
        res["_id"] = str(res["_id"])
        return  res

    # 保存
    def save(self,jsonInfo):
        _id = jsonInfo["_id"]
        jsonInfo.pop("_id")
        jsonInfo.pop("collectionName")
        if _id != '':
            res = self.updateById(_id,jsonInfo)
            return str(res)
        else:
            res = self.insert(jsonInfo)
            return str(res)

    # 新建
    def insert(self,insertJson):
        res = self.commonDao.insert(insertJson)
        return  res

    # 根据ID更新
    def updateById(self, _id, updateJson):
        res = self.commonDao.updateById(_id,updateJson)
        return  str(res)

    # 根据ID删除
    def deleteById(self,_id):
        res = self.commonDao.deleteById(_id)
        return str(res)

    # 根据项目ID获取所有项目
    def getProjectAndIntersByProjectId(self,_id,interCollectionName):
        projectInfo = self.commonDao.getById(_id)
        interList = projectInfo["list"]
        interQueryList = []    
        for inter in interList:
            interId = inter["interId"]
            interInfo = getCommonMongoDB(interCollectionName).getById(interId)
            interInfo["_id"] = str(interInfo["_id"])
            interInfo["interId"] = interId
            interQueryList.append(interInfo)
        projectInfo["list"] = interQueryList
        projectInfo["_id"] = str(projectInfo["_id"])
        return  projectInfo


