<template>
<div id="OESProjectList">
    <div>
        <el-button type="primary" @click="showProjectWindow('new','')">新建OES项目</el-button>
        <el-input placeholder="项目名称" v-model="searchName" style="width:500px">
            <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
        </el-input>
    </div>
    <el-card class="box-card" v-for="(project,index) in allProjects" :key="index">
        <div>
            <router-link :to="{path:'/OESProjectDetailView',query:{projectId:project._id}}"><span>{{project.projectName}}</span></router-link><span class="authorAndDes">{{project.author}}/{{project.url}}/{{project.description}}</span>
            <el-button @click="showProjectWindow('edit',project._id)">编辑</el-button>
            <el-button @click="projectDelete(project._id)">删除</el-button>
        </div>
    </el-card>
</div>
</template>

<script>
import eventBus from '@/js/eventBus'
import global from '@/config/global'

export default {
    inject: ['reload'],
    data() {
        return {
            author: "",
            description: "",
            allProjects: [],
            searchName: '',
        }
    },
    methods: {
        showProjectWindow: function (type, projectId) {
            this.$emit('showWin', type, projectId)
        },
        search: function () {
            this.axios.get(global.backEndUrl + global.backEndPath["getOESProjectList"], {
                    params: {
                        projectName: this.searchName
                    }
                })
                .then((response) => {
                    this.allProjects = response["data"]
                })
        },
        projectDelete: function (projectId) {
            this.$confirm('删除项目同时会删除项目下所有接口，确认该操作吗')
                .then(_ => {
                    this.axios.post(global.backEndUrl + global.backEndPath["deleteOESProjectById"], projectId)
                        .then((res) => {
                            this.reload()
                        })
                    done();
                })
                .catch(_ => {

                });
        },

    },
    created() {
        // 加载所有项目
        this.axios.get(global.backEndUrl + global.backEndPath["getOESProjectList"], {
                params: {
                    projectName: ''
                }
            })
            .then((response) => {
                this.allProjects = response["data"]
            })
    }
}
</script>

<style lang="scss">
.authorAndDes {
    font-style: italic,
}
</style>
