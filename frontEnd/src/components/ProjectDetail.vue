<template>
<div id="projectDetail">
    <div class="projectInfoArea">
        <span>{{projectName}}/{{author}}/{{description}}/{{env}}</span>
    </div>
    <router-link :to="'/project/'+projectName+'/InterfaceDetail/'+'NULL'"><span class="el-icon-plus" id="addNewInter"></span></router-link>
    <el-card class="box-card" v-for="(interInfo,index) in interList" :key="index">
        <router-link :to="'/project/'+projectName+'/'+env+'/InterfaceDetail/'+interInfo.interId">{{interInfo.interName}}</router-link>
            <div class="interName">{{interInfo.interName}}</div>
            <div>
                <span>path:{{interInfo.path}}</span>
                <span>method:{{interInfo.method}}</span><br>
                <span>header:{{interInfo.header}}</span><br>
                <span>params:{{interInfo.params}}</span><br>
            </div>
    </el-card>
</div>
</template>

<script>
export default {
    data() {
        return {
            projectName: '',
            author: '',
            env: '',
            description: '',
            interList: []
        }

    },
    methods: {
       
    },
    created() {
        console.log(this.$route.query)
        this.axios.get("http://localhost:5000/getProjectAndIntersByProjectName/" + this.$route.query.projectName)
            .then((res) => {
                this.projectName = res["data"]["projectName"]
                this.author = res["data"]["author"]
                this.env = res["data"]["env"]
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
