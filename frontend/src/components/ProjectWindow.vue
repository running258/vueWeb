<template>
<div id="ProjectWindow">
    <div >
        <span>项目名称</span>
        <el-input v-model="newProjectName" placeholder="项目名称"></el-input>
        <el-input v-model="author" placeholder="项目名称"></el-input>
        <el-select v-model="loginIndex" placeholder="环境选择" @change="changeEnv">
            <el-option v-for="(loginEnv, index) in loginEnvList" :key="index" :label="loginEnv.env" :value="index"></el-option>
        </el-select>
        <div>供端地址：<el-input v-model="supplyUrl"></el-input>登录Path：<el-input v-model="supplyPath"></el-input></div>
        <div>供端用户名：<el-input v-model="supplyUsername"></el-input>供端密码：<el-input v-model="supplyPassword"></el-input></div>
        <div>院端地址：<el-input v-model="hospUrl"></el-input>登录Path：<el-input v-model="hospPath"></el-input></div>
        <div>院端用户名：<el-input v-model="hospUsername"></el-input>院端密码：<el-input v-model="hospPassword"></el-input></div>
        <el-input type="textarea" v-model="description" placeholder="描述"></el-input>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="saveNewProject()">确 定</el-button>
        </span>
    </div>

</div>
</template>

<script>
import eventBus from '@/js/eventBus'

export default {
    name: "Project",
    data() {
        return {
            windowShow: false,
            author: "",
            env: "",
            loginIndex:"",
            description: "",
            allProjects: [],
            dialogVisible: false,
            accessRadio: 0,
            newProjectName: '',
            projectJson: {},
            loginEnvList: [],
            supplyUrl:'',
            supplyPath:'',
            hospUrl:'',
            hospPath:'',
            supplyUsername:'',
            supplyPassword:'',
            hospUsername:'',
            hospPassword:''
        }
    },
    methods: {
        saveNewProject() {
            this.formatProjectJson()
            console.log(this.projectJson)
            this.axios.post("http://localhost:5000/insertNewProject", this.projectJson)
                .then((res) => {
                    console.log(res)
                })
        },
        formatProjectJson() {
            this.projectJson = {
                "projectName": this.newProjectName,
                "author": this.author,
                "env":this.env,
                "supplyUsername":this.supplyUsername,
                "supplyPassword":this.supplyPassword,
                "hospUsername":this.hospUsername,
                "hospPassword":this.hospPassword,
                "description": this.description,
                "interfaces": []
            }
        },
        changeEnv() {
            var loginInfo = this.loginEnvList[this.loginIndex]
            this.env = loginInfo["env"]
            this.supplyUrl = loginInfo["supply"]["url"]
            this.supplyPath = loginInfo["supply"]["path"]
            this.hospUrl = loginInfo["hosp"]["url"]
            this.hospPath = loginInfo["hosp"]["path"]
        },
    },
    mounted(){
        eventBus.$on('showProjectWindow',function(type){
            console.log(type)
            this.windowShow = true
            console.log(this.windowShow)
        })
    }
}
</script>

<style lang="scss">
    .authorAndDes{
        font-style: italic,
    }
</style>
