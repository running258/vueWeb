<template>
<div id="interfaceLoginEnv">
    <el-button @click="addEnvCard()">add</el-button>
    <el-card v-for="(loginEnv, index) in loginEnvList" :key="index">
        <div><el-input class="urlInput" v-model="loginEnv.env"></el-input></div>
        <div><span>供端:</span></div>
        <div>
            <el-input class="urlInput" v-model="loginEnv.supply.url"></el-input>
        </div>
        <div>
            <el-input class="urlInput" v-model="loginEnv.supply.path"></el-input>
        </div>
        <div><span>院端:</span></div>
        <div>
            <el-input class="urlInput" v-model="loginEnv.hosp.url"></el-input>
        </div>
        <div>
            <el-input class="urlInput" v-model="loginEnv.hosp.path"></el-input>
        </div>
        <el-button class="primary" @click="saveLoginEnv(index,loginEnv._id)">保存</el-button>
        <el-button class="primary" @click="removeLoginEnv(index,loginEnv._id)">删除</el-button>
    </el-card>

</div>
</template>

<script>
export default {
    data() {
        return {
            loginEnvList: []
        }
    },
    methods: {
        addEnvCard() {
            var EmptyList = {
                "env": "",
                "supply": {
                    "url": "",
                    "path": ""
                },
                "hosp": {
                    "url": "",
                    "path": ""
                },
                "_id":""
            }
            this.loginEnvList.push(EmptyList)
        },
        saveLoginEnv(index,_id) {
            var loginInfo = JSON.stringify(this.loginEnvList[index])
            loginInfo = JSON.parse(loginInfo)
            // this.axios.post("http://localhost:5000/updateLoginEnv/",loginInfo)
            this.axios.post("http://localhost:5000/updateLoginEnv",this.loginEnvList[index])
            .then((res)=>{
                console.log(res)
            })
        },
        removeLoginEnv(index,_id) {
            this.loginEnvList.splice(index, 1)
            if(_id !=''){
                console.log("not null")
            }else{
                console.log("null")
            }
        },
    },
    created() {
        this.axios.get("http://localhost:5000/getAllLoginEnv")
            .then((res) => {
                this.loginEnvList = res["data"]
            })
    }
}
</script>

<style>
.urlInput {
    width: 500px
}
</style>
