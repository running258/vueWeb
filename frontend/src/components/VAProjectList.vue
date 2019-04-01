<template>
<div id="vaProjectList">
    <div>
        <el-button type="primary" @click="showProjectWindow('new','')">新建VA项目</el-button>
        <el-input placeholder="项目名称" v-model="searchName" style="width:500px">
            <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
        </el-input>
    </div>
    <el-card class="box-card" v-for="(vaProject,index) in allProjects" :key="index">
        <div>
            <router-link :to="{path:'/VAView',query:{vaProjectName:vaProject.vaProjectName}}"><span>{{vaProject.vaProjectName}}</span></router-link><span class="authorAndDes">{{vaProject.author}}/{{vaProject.description}}</span>
            <el-button @click="showProjectWindow('edit',vaProject._id)">编辑</el-button>
            <el-button @click="projectDelete()">删除</el-button>
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
        showProjectWindow: function (type,projectId) {
            this.$emit('showWin', type,projectId)
        },
        search: function () {
            this.axios.get(global.backEndUrl + global.backEndPath["getVAProjectList"], {
                    params: {
                        vaProjectName: this.searchName
                    }
                })
                .then((response) => {
                    this.allProjects = response["data"]
                })
        },
    },
    created() {
        // 加载所有项目
        this.axios.get(global.backEndUrl + global.backEndPath["getVAProjectList"], {
                params: {
                    vaProjectName: ''
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
