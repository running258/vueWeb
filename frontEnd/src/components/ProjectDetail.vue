<template>
<div id="projectDetail">
    <div>
        <span>{{projectName}}/{{author}}/{{description}}/{{env}}</span>
    </div>
    <el-button @click="interWindow('',projectName)">新添</el-button>
    <router-link :to="'/project/'+projectName+'/InterfaceDetail/'+'NULL'"><span class="el-icon-plus" id="addNewInter"></span></router-link>
    <el-card class="box-card" v-for="(interInfo,index) in interList" :key="index">
        <div>
            <el-button @click="interWindow(interInfo.interId,projectName)">编辑</el-button>
        </div>
        <div class="interName">{{interInfo.interName}}</div>
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
    data() {
        return {
            projectName: '',
            author: '',
            env: '',
            supplyUsername: '',
            supplyPassword: '',
            hospUsername: '',
            hospPassword: '',
            description: '',
            interList: []
        }

    },
    methods: {
        interWindow:function(interId,projectName) {
            this.$emit("interWindow",interId,projectName)
        }
    },
    created() {
        this.axios.get(global.backEndUrl + global.backEndPath["getProjectAndIntersByProjectName"] + "/" + this.$route.query.projectName)
            .then((res) => {
                this.projectName = res["data"]["projectName"]
                this.author = res["data"]["author"]
                this.env = res["data"]["env"]
                this.supplyUsername = res["data"]["supplyUsername"]
                this.supplyPassword = res["data"]["supplyPassword"]
                this.hospUsername = res["data"]["hospUsername"]
                this.hospPassword = res["data"]["hospPassword"]
                this.description = res["data"]["description"]
                this.interList = res["data"]["interfaces"]
            })
    }
}
</script>
