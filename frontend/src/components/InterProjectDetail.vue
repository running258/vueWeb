<template>
<div id="projectDetail">
    <div>
        <span>{{name}}/{{author}}/{{description}}</span>
    </div>
    <el-button @click="interWindow('',projectId)">新添</el-button>
    <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" label="全选" @change="selectAll"></el-checkbox>
    <el-button @click="runSelected">选中运行</el-button>
    <el-card class="box-card" v-for="(interInfo,index) in interList" :key="index">
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
    props:{
        projectCollectionName:String,
        interCollectionName:String,
        loginEnvCollectionName:String,
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
            projectId:'',
            interIdList:[],
            checkAll:false,
            isIndeterminate:false,
            singleCheckbox:[]
        }

    },
    methods: {
        run(interId,index) {
            this.axios.get(global.backEndUrl + global.backEndPath["runInterProjectInter"], {
                    params: {
                        projectId: this.projectId,
                        interId: interId,
                        projectCollectionName:this.projectCollectionName,
                        interCollectionName:this.interCollectionName,
                        loginEnvCollectionName:this.loginEnvCollectionName
                    }
                })
                .then(res => {
                    this.interList[index]["response"] = JSON.stringify(res["data"]);
                    let m = [... this.interList];
                    this.interList = [];
                    this.interList = m;
                })

        },
        runSelected() {
            var runInterBatJson = {
                "projectId":this.projectId,
                "interIdList":this.interIdList,
                "projectCollectionName":this.projectCollectionName,
                "interCollectionName":this.interCollectionName,
                "loginEnvCollectionName":this.loginEnvCollectionName
            }
            this.axios.post(global.backEndUrl + global.backEndPath["runInterBat"], runInterBatJson)
                .then(res => {
                    for (let index = 0; index < this.interIdList.length; index++) {
                        this.interList[index]["response"] = JSON.stringify(res["data"][index]);
                        
                    }
                    let m = [... this.interList];
                    this.interList = [];
                    this.interList = m;
                })

        },
        selectAll:function(){
            this.isIndeterminate = false
            if(this.checkAll){
                console.log("选中")
                for (let index = 0; index < this.interList.length; index++) {
                    this.interIdList[index] = this.interList[index]["interId"]
                    this.singleCheckbox[index] = true
                }
            }else{
                console.log("不选")
                for (let index = 0; index < this.interList.length; index++) {
                    this.interIdList[index] = ''
                    this.singleCheckbox[index] = false
                }
            }
            console.log(this.interIdList)
        },
        interWindow:function(interId,name) {
            this.$emit("interWindow",interId,name)
        },
        selectInter:function(interId,index){
            if(this.interIdList[index]!=''){
                this.interIdList[index] = ''
                this.checkAllSelected()
            }else{
                this.interIdList[index] = interId
                this.checkAllSelected()
            }
        },
        checkAllSelected:function(){
            var idListLength = 0
            for (let index = 0; index < this.interIdList.length; index++) {
                if(this.interIdList[index] != ''){
                    idListLength++
                }
            }
            var interListLength = this.interList.length
            if(idListLength != 0){
                if(idListLength != interListLength){
                    this.checkAll = false
                    this.isIndeterminate = true
                }else if(idListLength == interListLength){
                    this.checkAll = true
                    this.isIndeterminate = false
                }
            }else{
                this.checkAll = false
                this.isIndeterminate = false
            }
        }
    },
    created() {
        this.commonJs.getProjectAndIntersByProjectId(this.projectCollectionName,this.interCollectionName,this.$route.query.projectId)
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
