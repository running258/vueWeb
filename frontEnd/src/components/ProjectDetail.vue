<template>
<div id="projectDetail">
    <div class="projectInfoArea">
        <span>{{projectName}}{{author}}{{description}}</span>
    </div>
    <router-link :to="'/project/'+projectName+'/InterfaceDetail/'+'NULL'"><span class="el-icon-plus" id="addNewInter"></span></router-link>
    <el-card class="box-card" v-for="(interInfo,index) in interList" :key="index">
        <router-link :to="'/project/'+projectName+'/InterfaceDetail/'+interInfo.interId">{{interInfo.interName}}
        <div class="interName">{{interInfo.interName}}</div>
        <div>
            <span>path:{{interInfo.path}}</span>
            <span>method:{{interInfo.method}}</span><br>
            <span>header:{{interInfo.header}}</span><br>
            <span>params:{{interInfo.params}}</span><br>
        </div>
        </router-link>
    </el-card>
</div>
</template>

<script>
export default {
    data() {
        return {
            projectName: '',
            author: '',
            description: '',
            interList: []
        }

    },
    methods: {
       
    },
    created() {
        this.axios.get("http://localhost:5000/getProjectAndIntersByProjectName/" + this.$route.params.projectName)
            .then((res) => {
                this.projectName = res["data"]["projectName"]
                this.author = res["data"]["author"]
                this.description = res["data"]["description"]
                this.interList = res["data"]["interfaces"]
            })

    }
}
</script>

<style>
#addNewInter {
    width: 400px;
}
</style>
