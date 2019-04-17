<template>
<div id="projectDetail">
    <div>
        <span>{{name}}/{{author}}/{{description}}</span>
    </div>
    <el-button @click="interWindow('',projectId)">新添</el-button>
    <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" label="全选" @change="selectAll"></el-checkbox>
    <el-button @click="runSelected" :loading="runningFlag" :disabled="canRunAll">选中运行</el-button>
    <el-card class="box-card" v-for="(interInfo,index) in interList" :key="index" ref="interCard">
        <!-- <el-card class="box-card" v-for="(interInfo,index) in interList" :key="index" ref="interCard" style="background-color:#E6A23C"> -->
        <div>
            <el-checkbox label="选中" v-model="singleCheckbox[index]" @change="selectInter(interInfo.interId,index)"></el-checkbox>
            <el-button type="primary" icon="el-icon-caret-right" @click="run(interInfo.interId,index)">运行</el-button>
            <el-button @click="interWindow(interInfo.interId,projectId)">编辑</el-button>
        </div>
        <div class="name">{{interInfo.name}}</div>
        <div>
            <span>返回结果：</span><br>
            <el-input placeholder="response" v-model="interInfo.response"></el-input>
        </div>
        <div>
            <span>path:{{interInfo.path}}</span><br>
            <span>method:{{interInfo.method}}</span><br>
            <span>header:{{interInfo.header}}</span><br>
            <span>params:{{interInfo.params}}</span><br>
            </div>
    </el-card>
</div>
</template>

<script>
import global from '@/config/global'

export default {
    props: {
        projectCollectionName: String,
        interCollectionName: String,
        loginEnvCollectionName: String,
    },
    data() {
        return {
            name: '',
            author: '',
            supplyUsername: '',
            supplyPassword: '',
            hospUsername: '',
            hospPassword: '',
            description: '',
            interList: [],
            projectId: '',
            interIdList: [],
            checkAll: false,
            isIndeterminate: false,
            singleCheckbox: [],
            runningFlag: false,
            canRunAll: true
        }

    },
    methods: {
        run(interId, index) {
            this.runningFlag = true
            this.axios.get(global.backEndUrl + global.backEndPath["runInterProjectInter"], {
                    params: {
                        projectId: this.projectId,
                        interId: interId,
                        projectCollectionName: this.projectCollectionName,
                        interCollectionName: this.interCollectionName,
                        loginEnvCollectionName: this.loginEnvCollectionName
                    }
                })
                .then(res => {
                    var isPass = JSON.stringify(res["data"]["isPass"]);
                    this.interList[index]["response"] = JSON.stringify(res["data"]["res"]);
                    this.interList[index]["isPass"] = isPass;
                    let m = [...this.interList];
                    this.interList = [];
                    this.interList = m;
                    if (isPass == 'true') {
                        this.$refs.interCard[index].$el.style.backgroundColor = "#67C23A" //绿色，通过
                    } else if (isPass == 'false') {
                        this.$refs.interCard[index].$el.style.backgroundColor = "#F56C6C" //红色，失败
                    } else {
                        this.$refs.interCard[index].$el.style.backgroundColor = "#E6A23C" //黄色，没有期望结果
                    }
                    this.runningFlag = false
                })
        },
        runSelected() {
            this.runningFlag = true
            var cardList = this.$refs.interCard
            for (let index = 0; index < cardList.length; index++) {
                cardList[index].$el.style.backgroundColor = ""
            }
            var runInterBatJson = {
                "projectId": this.projectId,
                "interIdList": this.interIdList,
                "projectCollectionName": this.projectCollectionName,
                "interCollectionName": this.interCollectionName,
                "loginEnvCollectionName": this.loginEnvCollectionName
            }
            this.axios.post(global.backEndUrl + global.backEndPath["runInterBat"], runInterBatJson)
                .then(res => {
                    for (let index = 0; index < this.interIdList.length; index++) {
                        var isPass = JSON.stringify(res["data"][index]["isPass"]);
                        var interRes = JSON.stringify(res["data"][index]["res"]);
                        if (interRes != undefined) {
                            this.interList[index]["response"] = JSON.stringify(res["data"][index]);
                        }
                        this.interList[index]["isPass"] = isPass;
                        if (isPass == 'true') {
                            this.$refs.interCard[index].$el.style.backgroundColor = "#67C23A" //绿色，通过
                        } else if (isPass == 'false') {
                            this.$refs.interCard[index].$el.style.backgroundColor = "#F56C6C" //红色，失败
                        } else if (interRes != undefined) {
                            this.$refs.interCard[index].$el.style.backgroundColor = "#E6A23C" //黄色，没有期望结果
                        }
                    }
                    let m = [...this.interList];
                    this.interList = [];
                    this.interList = m;
                    this.runningFlag = false
                })

        },
        selectAll: function () {
            this.isIndeterminate = false
            if (this.checkAll) {
                for (let index = 0; index < this.interList.length; index++) {
                    this.interIdList[index] = this.interList[index]["interId"]
                    this.singleCheckbox[index] = true
                    this.canRunAll = false
                }
            } else {
                for (let index = 0; index < this.interList.length; index++) {
                    this.interIdList[index] = ''
                    this.singleCheckbox[index] = false
                    this.canRunAll = true
                }
            }
        },
        interWindow: function (interId, name) {
            this.$emit("interWindow", interId, name)
        },
        selectInter: function (interId, index) {
            if (this.interIdList[index] != '') {
                this.interIdList[index] = ''
                this.checkAllSelected()
            } else {
                this.interIdList[index] = interId
                this.checkAllSelected()
            }
        },
        checkAllSelected: function () {
            var idListLength = 0
            for (let index = 0; index < this.interIdList.length; index++) {
                if (this.interIdList[index] != '') {
                    idListLength++
                }
            }
            var interListLength = this.interList.length
            if (idListLength != 0) {
                if (idListLength != interListLength) {
                    this.checkAll = false
                    this.isIndeterminate = true
                } else if (idListLength == interListLength) {
                    this.checkAll = true
                    this.isIndeterminate = false
                }
                this.canRunAll = false
            } else {
                this.checkAll = false
                this.isIndeterminate = false
                this.canRunAll = true
            }
        }
    },
    created() {
        this.commonJs.getProjectAndIntersByProjectId(this.projectCollectionName, this.interCollectionName, this.$route.query.projectId)
            .then((res) => {
                this.name = res["data"]["name"]
                this.author = res["data"]["author"]
                this.supplyUsername = res["data"]["supplyUsername"]
                this.supplyPassword = res["data"]["supplyPassword"]
                this.hospUsername = res["data"]["hospUsername"]
                this.hospPassword = res["data"]["hospPassword"]
                this.description = res["data"]["description"]
                this.interList = res["data"]["list"]
                this.projectId = res["data"]["_id"]
                for (let index = 0; index < this.interList.length; index++) {
                    this.interIdList.push('');
                    this.singleCheckbox.push(false);
                }
            })
    }
}
</script>
