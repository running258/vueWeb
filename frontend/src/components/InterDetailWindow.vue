<template>
<div id="InterDetailWindow">
    <el-form :model="interFrom" ref="interFrom" label-width="110px" class="interFrom">
        <el-row>
            <el-form-item label="接口名称">
                <el-input placeholder="接口名称" class="name" v-model="interFrom.name"></el-input>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item label="运行系统">
                <el-radio v-model="interFrom.sys" label="supply">供端</el-radio>
                <el-radio v-model="interFrom.sys" label="hosp">院端</el-radio>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item>
                <el-input placeholder="请输入接口地址" v-model="interFrom.path" class="input-with-select">
                    <el-select v-model="interFrom.method" slot="prepend" placeholder="请选择" style="width:110px">
                        <el-option label="GET" value="GET"></el-option>
                        <el-option label="POST" value="POST"></el-option>
                        <el-option label="PUT" value="PUT"></el-option>
                    </el-select>
                </el-input>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item>
                <el-input placeholder="使用指定用户名登录" v-model="interFrom.runUsername" style="width:45%"></el-input>
                <el-input placeholder="使用指定密码登录" v-model="interFrom.runPassword" style="width:45%"></el-input>
            </el-form-item>
        </el-row>
        <el-row v-for="(header, index) in interFrom.headerList" :key="index">
            <el-form-item label="header">
                <el-input placeholder="header" class="headerParams" v-model="header.header" style="width:45%"></el-input>
                <el-input placeholder="value" class="headerValues" v-model="header.value" style="width:45%"></el-input>
                <i class="el-icon-circle-plus" @click="addHeader()"></i>
                <i class="el-icon-remove" @click="removeHeader(index)" v-if="interFrom.headerList.length != 1"></i>
            </el-form-item>
        </el-row>
        <div v-if="interFrom.method!='GET' && interFrom.method!=''">
            <el-tabs v-model="activeName" @tab-click="handleClick">
                <el-tab-pane label="payload" name="payload">payload</el-tab-pane>
                <el-tab-pane label="raw" name="raw">raw</el-tab-pane>
            </el-tabs>
            <div v-if="activeName=='payload'">
                <el-row v-for="(payload, index) in interFrom.payloadList" :key="index">
                    <el-form-item label="params">
                        <el-input placeholder="name" class="payloadName" v-model="payload.name" style="width:45%"></el-input>
                        <el-input placeholder="value" class="payloadValues" v-model="payload.value" style="width:45%"></el-input>
                        <i class="el-icon-circle-plus" @click="addPayload()"></i>
                        <i class="el-icon-remove" @click="removePayload(index)" v-if="interFrom.payloadList.length!=1"></i>
                    </el-form-item>
                </el-row>
            </div>
            <div v-if="activeName=='raw'">
                <el-row>
                    <el-form-item label="rawData">
                        <el-input type="textarea" :autosize="{ minRows: 5}" placeholder="请输入内容" v-model="interFrom.rawarea"></el-input>
                    </el-form-item>
                </el-row>
            </div>
        </div>
         <el-form-item label="期望结果">
            <el-input type="textarea" :autosize="{ minRows: 3}" placeholder="期望结果" v-model="interFrom.expectedResult"></el-input>
        </el-form-item>
        <el-form-item>
            <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="运行结果" v-model="runResult"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" icon="el-icon-caret-right" @click="run">运行</el-button>
            <el-button type="primary" @click="save">保存</el-button>
        </el-form-item>
    </el-form>

</div>
</template>

<script>
import global from '@/config/global'

export default {
    props: {
        interId: String,
        projectId: String,
        projectCollectionName: String,
        interCollectionName: String
    },
    data() {
        return {
            interFrom: {
                name: '',
                sys: '',
                method: '',
                path: '',
                runUsername: '',
                runPassword: '',
                headerList: [{
                    'header': '',
                    'value': '',
                }],
                payloadList: [{
                    'name': '',
                    'value': ''
                }],
                rawarea: '',
                expectedResult:''
            },
            interInfo: [],
            description: '',
            activeName: 'payload',
            runResult: '',
            isPass: '',
            interJson: {},
            author: '',
            supplyUsername: '',
            supplyPassword: '',
            hospUsername: '',
            hospPassword: '',
            description: '',
            loginEnvCollectionName:'interLoginEnv'
        };
    },
    methods: {
        run() {
            this.axios.get(global.backEndUrl + global.backEndPath["runInterProjectInter"], {
                    params: {
                        projectId: this.projectId,
                        interId: this.interId,
                        projectCollectionName:this.projectCollectionName,
                        interCollectionName:this.interCollectionName,
                        loginEnvCollectionName:this.loginEnvCollectionName
                    }
                })
                .then(res => {
                    this.runResult = JSON.stringify(res["data"]["res"])
                    this.isPass = JSON.stringify(res["data"]["isPass"]);
                })

        },
        save: function () {
            this.getInterJson()
            this.axios.post(global.backEndUrl + global.backEndPath["saveInterAndUpdateProject"], this.interJson)
                .then(response => {
                    this.runResult = JSON.stringify(response["data"])
                    this.$emit('closeInterWindow')
                })

        },
        getInterJson: function () {
            var headerList = this.interFrom.headerList
            var paramList = this.interFrom.payloadList
            var headerStr = ""
            var paramStr = ""
            headerList.forEach(element => {
                var header = element["header"]
                var value = element["value"]
                if (header != '' && value != '') {
                    if (headerStr.length == 0) {
                        headerStr = "\"" + header + "\":" + value
                    } else {
                        headerStr = headerStr + ",\"" + header + "\":" + value
                    }
                }
            });
            headerStr = "{" + headerStr + "}"
            paramList.forEach(element => {
                var header = element["name"]
                var value = element["value"]
                if (header != '' && value != '') {
                    if (paramStr.length == 0) {
                        paramStr = "\"" + header + "\":" + value
                    } else {
                        paramStr = paramStr + ",\"" + header + "\":" + value
                    }
                }
            });
            paramStr = "{" + paramStr + "}"
            var headerJson = JSON.parse(headerStr)
            var paramJson = JSON.parse(paramStr)
            var runUsername = ''
            var runPassword = ''
            var isNewUser = false
            if (this.interFrom.runUsername != '') {
                runUsername = this.interFrom.runUsername
                isNewUser = true
            } else {
                if (this.interFrom.sys == 'supply') {
                    runUsername = this.supplyUsername
                } else if (this.interFrom.sys == 'hosp') {
                    runUsername = this.hospUsername
                }
            }
            if (this.interFrom.runPassword != '') {
                runPassword = this.interFrom.runPassword
                isNewUser = true
            } else {
                if (this.interFrom.sys == 'supply') {
                    runPassword = this.supplyPassword
                } else if (this.interFrom.sys == 'hosp') {
                    runPassword = this.hospPassword
                }
            }
            this.interJson = {
                "sys": this.interFrom.sys,
                "name": this.interFrom.name,
                "path": this.interFrom.path,
                "method": this.interFrom.method,
                "header": headerJson,
                "params": paramJson,
                "expectedResult": this.interFrom.expectedResult,
                "runUsername": runUsername,
                "runPassword": runPassword,
                "isNewUser": isNewUser,
                "_id": this.interId,
                "projectId": this.projectId,
                "interCollectionName": this.interCollectionName,
                "projectCollectionName": this.projectCollectionName
            }
        },
        addHeader() {
            this.interFrom.headerList.push({
                'header': '',
                'value': '',
            });
        },
        removeHeader(index) {
            this.interFrom.headerList.splice(index, 1)
        },
        addPayload() {
            this.interFrom.payloadList.push({
                'name': '',
                'value': '',
            });
        },
        removePayload(index) {
            this.interFrom.payloadList.splice(index, 1)
        },
        handleClick(tab, event) {}
    },
    created() {
        this.commonJs.getById(this.projectCollectionName, this.projectId)
            .then((res) => {
                this.supplyUsername = res["data"]["supplyUsername"]
                this.supplyPassword = res["data"]["supplyPassword"]
                this.hospUsername = res["data"]["hospUsername"]
                this.hospPassword = res["data"]["hospPassword"]
            })
        var interId = this.interId
        if (interId != '' && interId != 'NULL') {
            this.commonJs.getById(this.interCollectionName, interId)
                .then((response) => {
                    this.interInfo = response["data"]
                    this.interFrom.method = this.interInfo["method"]
                    this.interFrom.sys = this.interInfo["sys"]
                    this.interFrom.path = this.interInfo["path"]
                    this.interFrom.name = this.interInfo["name"]
                    this.interFrom.runUsername = this.interInfo["username"]
                    this.interFrom.runPassword = this.interInfo["password"]
                    this.interFrom.expectedResult = this.interInfo["expectedResult"].replace(/\\"/g,'"')
                    var header = this.interInfo["header"]
                    var headerInitFlag = true
                    var paramInitFlag = true
                    for (var key in header) {
                        if (headerInitFlag) {
                            this.interFrom.headerList = [{
                                'header': key,
                                'value': JSON.stringify(header[key])
                            }]
                            headerInitFlag = false
                        } else {
                            this.interFrom.headerList.push({
                                'header': key,
                                'value': JSON.stringify(header[key])
                            })
                        }
                    }
                    var params = this.interInfo["params"]
                    for (var key in params) {
                        if (paramInitFlag) {
                            this.interFrom.payloadList = [{
                                'name': key,
                                'value': JSON.stringify(params[key])
                            }]
                            paramInitFlag = false
                        } else {
                            this.interFrom.payloadList.push({
                                'name': key,
                                'value': JSON.stringify(params[key])
                            })
                        }
                    }

                })
        }

    }
};
</script>

<style>
.headerParams {
    width: 400px;
}

.headerValues {
    width: 400px;
}

.payloadName {
    width: 400px;
}

.payloadValues {
    width: 400px;
}
</style>
