import mitmproxy.http
import json
from mitmproxy import ctx
from selenium import webdriver
from selenium import webdriver
from src.controller.commonController import commonController
from src.entity.tools import getTime

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--proxy-server=http://127.0.0.1:8080")
browser = webdriver.Chrome(chrome_options=chromeOptions)
projectName = "系统录制"+str(getTime().getTimestamp())
projectInfo = {
    "name": projectName, 
    "author": "系统录制", 
    "loginEnvId": "", 
    "supplyUsername", 
    "supplyPassword", 
    "hospUsername", 
    "hospPassword", 
    "description": "该项目为系统录制自动生成的项目", 
    "list": []
}
projectId = commonController("interProject").insert(projectInfo)


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):

        if flow.request.host == "vhsupply.staging.viewchain.net":
            if "application/json" in flow.request.headers["accept"]:
                self.num = self.num + 1
                sys = "supply"
                interName = flow.request.path
                path = flow.request.path
                method = flow.request.method
                headerList = {}
                paramsList = {}
                for key in flow.request.headers:
                    if key in ["accept", "accept-language", "content-length", "content-type"]:
                        headerList[key] = flow.request.headers[key]
                if method.lower() == 'post' and flow.request.headers["content-type"] != "application/x-www-form-urlencoded":
                    paramsList = json.loads(flow.request.get_text())
                    if "_t" in paramsList:
                        paramsList.pop("_t")
                elif method.lower() == 'get':
                    KeyParam = ''
                    ValueParam = ''
                    paramPath = flow.request.path.split("?")[-1]
                    for param in paramPath.split("&"):
                        temp_List = param.split("=")
                        if len(temp_List) == 2:
                            KeyParam = temp_List[0]
                            ValueParam = temp_List[1]
                        elif len(temp_List) == 1:
                            KeyParam = temp_List[0]
                    paramsList[KeyParam] = ValueParam
                    if "_t" in paramsList:
                        paramsList.pop("_t")
                jsonInfo = {"sys": sys, "name": interName, "path": path, "method": method,
                            "header": headerList, "params": paramsList, "projectName": '', "username": '', "password": ''}
                interId = commonController("inter").insert(jsonInfo)
                projectInfo["list"].append({
                    "interId": str(interId),
                    "interName": interName
                })
                commonController("interProject").updateById(
                    projectId, projectInfo)


# https://vhsupply.staging.viewchain.net/#/login
# mitmdump -s record.py

addons = [
    Counter()
]
