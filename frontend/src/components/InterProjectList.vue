<template>
<div id="InterProjectList">
    <el-button type="primary" @click="projectWin('')">新建项目</el-button>
    <el-card class="box-card" v-for="(project,index) in interProjectList" :key="index">
        <div slot="header" class="clearfix">
            <router-link :to="{path:'/InterProjectDetailView',query:{projectId:project._id,env:project.env}}"><span>{{project.name}}</span></router-link><span class="authorAndDes">{{project.author}}/{{project.description}}/{{project.env}}</span>
        </div>
        <div v-for="(inter,index) in project.interfaces" :key="index">
            <span>{{inter.interName}}</span>
            <el-button @click="interWindow(inter.interId,project.projectId)">查看</el-button>
        </div>
    </el-card>
</div>
</template>

<script>
import eventBus from '@/js/eventBus'
import global from '@/config/global'

export default {

    props:{
        projectCollectionName: String
    },
    data() {
        return {
            searchName:'',
            author: "",
            env: "",
            loginIndex: "",
            description: "",
            interProjectList: []
        }
    },
    methods: {
        projectWin: function (projectId) {
            this.$emit('projectWin', projectId)
        },
        interShowFun: function (interId, projectId) {
            this.interShow = true
            if (interId != "") {
                this.interId = interId
                this.projectId = projectId
            }
        },
        interWindow: function (interId, projectId) {
            this.$emit("interWindow", interId, projectId)
        }
    },
    created() {
        // 加载所有项目
        this.commonJs.getList(this.projectCollectionName,'')
            .then((response) => {
                this.interProjectList = response["data"]
            })
    }
}
</script>

<style lang="scss">
.authorAndDes {
    font-style: italic,
}
</style>
