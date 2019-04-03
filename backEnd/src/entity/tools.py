import os
import json
import time,datetime
import hashlib

class jsonLoad(object):

    def __init__(self):
        self.jsonPath = os.path.abspath('.')+"/docs/data/"

    def jsonContext(self, jsonFileName):
        with open(self.jsonPath+jsonFileName,'r') as jsonContext:
            return json.load(jsonContext)

    def getVariable(self, jsonFileName, dataNode, varName):
        with open(self.jsonPath+jsonFileName,'r') as jsonContext:
            return json.load(jsonContext)[dataNode]["variable"][varName]

class getTime(object):

    def getTimestamp(self):
        return int(time.time())*1000

    def getYYYYMMDDTimestamp(self):
        nowTime = datetime.datetime.now()
        time_structure = datetime.datetime(nowTime.year, nowTime.month, nowTime.day, 8, 0, 0, 0)
        return int(time.mktime(time_structure.timetuple()))*1000


class mask(object):

    def sha256(self,stringBuffer):
        sha256 = hashlib.sha256()
        sha256.update(stringBuffer.encode('utf-8'))
        res = sha256.hexdigest()
        return res
