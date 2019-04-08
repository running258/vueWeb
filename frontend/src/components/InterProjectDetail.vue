<template>
<div id="projectDetail">
    <div>
        <span>{{name}}/{{author}}/{{description}}/{{env}}</span>
    </div>
    <el-button @click="interWindow('',projectId)">新添</el-button>
    <el-card class="box-card" v-for="(interInfo,index) in interList" :key="index">
        <div>
            <el-button @click="interWindow(interInfo.interId,projectId)">编辑</el-button>
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
    props:{
        projectCollectionName:String,
        interCollectionName:String
    },
    data() {
        return {
            name: '',
            author: '',
            env: '',
            supplyUsername: '',
            supplyPassword: '',
            hospUsername: '',
            hospPassword: '',
            description: '',
            interList: [],
            projectId:'',
        }

    },
    methods: {
        interWindow:function(interId,name) {
            this.$emit("interWindow",interId,name)
        }
    },
    created() {
        this.commonJs.getProjectAndIntersByProjectId(this.projectCollectionName,this.interCollectionName,this.$route.query.projectId)
            .then((res) => {
                this.name = res["data"]["name"]
                this.author = res["data"]["author"]
                this.env = res["data"]["env"]
                this.supplyUsername = res["data"]["supplyUsername"]
                this.supplyPassword = res["data"]["supplyPassword"]
                this.hospUsername = res["data"]["hospUsername"]
                this.hospPassword = res["data"]["hospPassword"]
                this.description = res["data"]["description"]
                this.interList = res["data"]["list"]
                this.projectId = res["data"]["_id"]
            })
    }
}
</script>
