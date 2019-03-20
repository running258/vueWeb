<template>
<div id="Project">

    <el-row>
        <el-col :span="12"></el-col>
        <el-col :span="12">
            <div class="grid-content bg-purple-light"></div>
        </el-col>
    </el-row>
    <el-button type="primary" @click="dialogVisible = true">新建项目</el-button>
    <el-card class="box-card" v-for="(project,index) in allProjects" :key="index">
        <div slot="header" class="clearfix">
            <!-- <router-link :to="'/ProjectDetail/'+project.projectName"><span>{{project.projectName}}</span></router-link> <span class="authorAndDes">{{project.author}}/{{project.description}}</span> -->
            <router-link :to="{path:'/ProjectDetail',query:{projectName:project.projectName,env:project.env}}"><span>{{project.projectName}}</span></router-link> <span class="authorAndDes">{{project.author}}/{{project.description}}/{{project.env}}</span>
        </div>
        <div v-for="(inter,index) in project.interfaces" :key="index">
            <router-link :to="'/project/'+project.projectName+'/'+project.env+'/InterfaceDetail/'+inter.interId">{{inter.interName}}</router-link>
        </div>
    </el-card>

    <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
        <span>项目名称</span>
        <el-input v-model="newProjectName" placeholder="项目名称"></el-input>
        <el-input v-model="author" placeholder="项目名称"></el-input>
        <el-select v-model="loginIndex" placeholder="环境选择" @change="changeEnv">
            <el-option v-for="(loginEnv, index) in loginEnvList" :key="index" :label="loginEnv.env" :value="index"></el-option>
        </el-select>
        <div>供端地址：<el-input v-model="supplyUrl"></el-input>登录Path：<el-input v-model="supplyPath"></el-input></div>
        <div>院端地址：<el-input v-model="hospUrl"></el-input>登录Path：<el-input v-model="hospPath"></el-input></div>
        <el-input type="textarea" v-model="description" placeholder="描述"></el-input>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="saveNewProject()">确 定</el-button>
        </span>
    </el-dialog>

</div>
</template>

<script>
export default {
    name: "Project",
    data() {
        return {
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
            hospPath:''
        }
    },
    methods: {
        handleClose(done) {
            this.$confirm('确认关闭？')
                .then(_ => {
                    done();
                })
                .catch(_ => {});
        },
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
                "description": this.description,
                "interfaces": []
            }
        },
        changeEnv() {
            var loginInfo = this.loginEnvList[this.loginIndex]
            console.log(this.loginEnvList)
            console.log(loginInfo)
            this.env = loginInfo["env"]
            this.supplyUrl = loginInfo["supply"]["url"]
            this.supplyPath = loginInfo["supply"]["path"]
            this.hospUrl = loginInfo["hosp"]["url"]
            this.hospPath = loginInfo["hosp"]["path"]
        }
    },
    created() {
        // 加载所有项目
        this.axios.get('http://localhost:5000/getProjects')
            .then((response) => {
                this.allProjects = response["data"]
            })
        this.axios.get("http://localhost:5000/getAllLoginEnv")
            .then((res) => {
                this.loginEnvList = res["data"]
            })
    }
}
</script>

<style lang="scss">
    .authorAndDes{
        font-style: italic,
    }
</style>
