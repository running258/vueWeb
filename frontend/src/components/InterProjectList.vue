<template>
<div id="InterProjectList">
    <el-button type="primary" @click="showWin('')">新建项目</el-button>
    <el-card class="box-card" v-for="(project,index) in interProjectList" :key="index">
        <div slot="header" class="clearfix">
            <router-link :to="{path:'/projectDetail',query:{projectName:project.projectName,env:project.env}}"><span>{{project.projectName}}</span></router-link><span class="authorAndDes">{{project.author}}/{{project.description}}/{{project.env}}</span>
        </div>
        <div v-for="(inter,index) in project.interfaces" :key="index">
            <span>{{inter.interName}}</span>
            <el-button @click="interWindow(inter.interId,project.projectName)">查看</el-button>
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
            searchName:'',
            author: "",
            env: "",
            loginIndex: "",
            description: "",
            interProjectList: []
        }
    },
    methods: {
        showWin: function (projectId) {
            this.$emit('showWin', projectId)
        },
        projectDetail: function (projectName, env) {
            this.$router.push({
                name: 'projectDetail',
                query: {
                    projectName: projectName,
                    env: env
                }
            })
        },
        interShowFun: function (interId, projectName) {
            this.interShow = true
            if (interId != "") {
                this.interType = "编辑"
                this.interId = interId
                this.projectName = projectName
            }
        },
        interWindow: function (interId, projectName) {
            this.$emit("interWindow", interId, projectName)
        }
    },
    created() {
        // 加载所有项目
        this.axios.get(global.backEndUrl + global.backEndPath["getList"], {
                params: {
                    name: this.searchName,
                    collectionName: "interProject"
                }
            })
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
