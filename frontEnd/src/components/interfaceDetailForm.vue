<template>
<div id="InterfaceDetailForm">

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

    <el-button type="primary" icon="el-icon-caret-right" @click="run()">运行</el-button>

</div>
</template>

<script>
export default {
    data() {
        return {
            interInfo: [],
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
            rawarea: ''
        };
    },
    methods: {
        run() {
            this.axios.post('http://localhost:5000/runSingleInter',{
                    "addRole": {
                        "path": "/api1/api/account/role/create",
                        "method": "post",
                        "header": {
                            "content-type": "application/json"
                        },
                        "params": {
                            "resIdList": [0, 3, 6, 12, 63, 15, 18, 24, 60, 27, 21, 30, 33, 66, 62, 69, 161, 164, 167, 170, 173, 72, 75, 102],
                            "roleVo": {
                                "name": "interfaceRole",
                                "description": "",
                                "builtIn": 2
                            }
                        }
                    }
                })
                .then(res => {
                    console.log(res)
                })

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
        var interName = this.$route.params.interName
        if (interName != '') {
            this.axios.get('http://localhost:5000/interInfo/' + interName)
                .then((response) => {
                    this.interInfo = response["data"]
                    this.method = this.interInfo["method"]
                    this.path = this.interInfo["path"]
                    this.interName = this.interInfo["interName"]
                    this.description = this.interInfo["description"]
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
