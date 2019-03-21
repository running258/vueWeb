<template>
<div id="InterfaceDetailForm">
    <el-input placeholder="接口名称" class="interName" v-model="interName"></el-input>
    <el-radio v-model="sys" label="supply">供端</el-radio>
    <el-radio v-model="sys" label="hosp">院端</el-radio>
    <div style="margin-top: 15px;">
        <el-input placeholder="请输入接口地址" v-model="path" class="input-with-select">
            <el-select v-model="method" slot="prepend" placeholder="请选择">
                <el-option label="GET" value="GET"></el-option>
                <el-option label="POST" value="POST"></el-option>
                <el-option label="PUT" value="PUT"></el-option>
            </el-select>
        </el-input>
    </div>
    <div>
        <el-row v-for="(header, index) in headerList" :key="index">
            <el-input placeholder="header" class="headerParams" v-model="header.header"></el-input>
            <el-input placeholder="value" class="headerValues" v-model="header.value"></el-input>
            <i class="el-icon-circle-plus" @click="addHeader()"></i>
            <i class="el-icon-remove" @click="removeHeader(index)" v-if="headerList.length != 1"></i>
        </el-row>
    </div>

    <div v-if="method!='GET' && method!=''">
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="payload" name="payload">payload</el-tab-pane>
            <el-tab-pane label="raw" name="raw">raw</el-tab-pane>
        </el-tabs>

        <div>
            <el-input placeholder="使用指定用户名登录" v-model="runUsername"></el-input>
            <el-input placeholder="使用指定密码登录" v-model="runPassword"></el-input>
        </div>
        
        <div v-if="activeName=='payload'">
            <el-row v-for="(payload, index) in payloadList" :key="index">
                <el-input placeholder="name" class="payloadName" v-model="payload.name"></el-input>
                <el-input placeholder="value" class="payloadValues" v-model="payload.value"></el-input>
                <i class="el-icon-circle-plus" @click="addPayload()"></i>
                <i class="el-icon-remove" @click="removePayload(index)" v-if="payloadList.length!=1"></i>
            </el-row>
        </div>
        <div v-if="activeName=='raw'">
            <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="请输入内容" v-model="rawarea">
            </el-input>
        </div>
    </div>
    <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="运行结果" v-model="runResult"></el-input>

    <el-button type="primary" icon="el-icon-caret-right" @click="run(projectName)">运行</el-button>
    <el-button type="primary" icon="el-icon-caret-right" @click="save(projectName)">保存</el-button>

</div>
</template>

<script>
export default {
    data() {
        return {
            interInfo: [],
            sys:'',
            interName: '',
            description: '',
            activeName: 'payload',
            path: '',
            method: '',
            headerList: [{
                'header': '',
                'value': '',
            }],
            payloadList: [{
                'name': '',
                'value': ''
            }],
            rawarea: '',
            runResult: '',
            interJson: {},
            runUsername:'',
            runPassword:'',
            projectName: '',
            author: '',
            env: '',
            supplyUsername: '',
            supplyPassword: '',
            hospUsername: '',
            hospPassword: '',
            description: '',
        };
    },
    methods: {
        run(projectName) {
            this.getInterJson(projectName)
            this.axios.post('http://localhost:5000/runSingleInter', this.interJson)
                .then(response => {
                    this.runResult = JSON.stringify(response["data"])
                })

        },
        save(projectName) {
            this.getInterJson(projectName)
            this.axios.post('http://localhost:5000/saveInterAndUpdateProject', this.interJson)
                .then(response => {
                    this.runResult = JSON.stringify(response["data"])
                })

        },
        getInterJson(projectName) {
            var headerList = this.headerList
            var paramList = this.payloadList
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
            if (this.runUsername != ''){
                runUsername = this.runUsername
            }else {
                if(this.sys=='supply'){
                    runUsername = this.supplyUsername
                }
                else if(this.sys=='hosp'){
                    runUsername = this.hospUsername
                }
            }
            if (this.runPassword != ''){
                runPassword = this.runPassword
            }else {
                if(this.sys=='supply'){
                    runPassword = this.supplyPassword
                }
                else if(this.sys=='hosp'){
                    runPassword = this.hospPassword
                }
            }

            this.interJson = {
                "sys":this.sys,
                "interName": this.interName,
                "path": this.path,
                "method": this.method,
                "header": headerJson,
                "params": paramJson,
                "projectName": projectName,
                "env": this.$route.params.env,   
                "runUsername": runUsername,
                "runPassword": runPassword
            }
        },
        addHeader() {
            this.headerList.push({
                'header': '',
                'value': '',
            });
        },
        removeHeader(index) {
            this.headerList.splice(index, 1)
        },
        addPayload() {
            this.payloadList.push({
                'name': '',
                'value': '',
            });
        },
        removePayload(index) {
            this.payloadList.splice(index, 1)
        },
        handleClick(tab, event) {}

    },
    created() {
        var interId = this.$route.params.interId
        if (interId != '' && interId != 'NULL') {
            this.axios.get('http://localhost:5000/interInfo/' + interId)
                .then((response) => {
                    this.interInfo = response["data"]
                    this.method = this.interInfo["method"]
                    this.sys = this.interInfo["sys"]
                    this.path = this.interInfo["path"]
                    this.interName = this.interInfo["interName"]
                    this.description = this.interInfo["description"]
                    this.runUsername = this.interInfo["username"]
                    this.runPassword = this.interInfo["password"]
                    var header = this.interInfo["header"]
                    var headerInitFlag = true
                    var paramInitFlag = true
                    for (var key in header) {
                        if (headerInitFlag) {
                            this.headerList = [{
                                'header': key,
                                'value': JSON.stringify(header[key])
                            }]
                            headerInitFlag = false
                        } else {
                            this.headerList.push({
                                'header': key,
                                'value': JSON.stringify(header[key])
                            })
                        }
                    }
                    var params = this.interInfo["params"]
                    for (var key in params) {
                        if (paramInitFlag) {
                            this.payloadList = [{
                                'name': key,
                                'value': JSON.stringify(params[key])
                            }]
                            paramInitFlag = false
                        } else {
                            this.payloadList.push({
                                'name': key,
                                'value': JSON.stringify(params[key])
                            })
                        }
                    }

                })
        }
        this.axios.get("http://localhost:5000/getProjectAndIntersByProjectName/" + this.$route.params.projectName)
            .then((res) => {
                this.projectName = res["data"]["projectName"]
                this.author = res["data"]["author"]
                this.env = res["data"]["env"]
                this.supplyUsername = res["data"]["supplyUsername"]
                this.supplyPassword = res["data"]["supplyPassword"]
                this.hospUsername = res["data"]["hospUsername"]
                this.hospPassword = res["data"]["hospPassword"]
                this.description = res["data"]["description"]
            })
    },
    mounted() {}
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
