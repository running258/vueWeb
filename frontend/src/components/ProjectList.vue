<template>
<div id="ProjectList">
    <el-row>
        <el-col :span="12"></el-col>
        <el-col :span="12">
            <div class="grid-content bg-purple-light"></div>
        </el-col>
    </el-row>
    <el-button type="primary" @click="showProjectWindow('new')">新建项目</el-button>
    <el-card class="box-card" v-for="(project,index) in allProjects" :key="index">
        <div slot="header" class="clearfix">
            <router-link :to="{path:'/ProjectDetail',query:{projectName:project.projectName,env:project.env}}"><span>{{project.projectName}}</span></router-link><span class="authorAndDes">{{project.author}}/{{project.description}}/{{project.env}}</span>
        </div>
        <div v-for="(inter,index) in project.interfaces" :key="index">
            <router-link :to="'/project/'+project.projectName+'/'+project.env+'/InterfaceDetail/'+inter.interId">{{inter.interName}}</router-link>
        </div>
    </el-card>
</div>
</template>

<script>
import eventBus from '@/js/eventBus'
import global from '@/config/global'

export default {
    data() {
        return {
            author: "",
            env: "",
            loginIndex:"",
            description: "",
            allProjects: []
        }
    },
    methods: {
        showProjectWindow:function(type){
            this.$emit('showWin',type)
        }
    },
    created() {
        // 加载所有项目
        this.axios.get(global.backEndUrl+global.backEndPath["getProject"])
            .then((response) => {
                this.allProjects = response["data"]
            })
    }
}
</script>

<style lang="scss">
    .authorAndDes{
        font-style: italic,
    }
</style>
