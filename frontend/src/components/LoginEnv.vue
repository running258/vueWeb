<template>
<div id="interfaceLoginEnv">
    <el-button @click="addEnvCard()">add</el-button>
    <el-card v-for="(loginEnv, index) in loginEnvList" :key="index">
        <div><el-input class="urlInput" v-model="loginEnv.env"></el-input></div>
        <div><span>供端:</span></div>
        <div>
            <el-input class="urlInput" v-model="loginEnv.supply.url"></el-input>
            <el-input class="urlInput" v-model="loginEnv.supply.path"></el-input>
        </div>
        <div><span>院端:</span></div>
        <div>
            <el-input class="urlInput" v-model="loginEnv.hosp.url"></el-input>
            <el-input class="urlInput" v-model="loginEnv.hosp.path"></el-input>
        </div>
        <el-button class="primary" @click="saveLoginEnv(index,loginEnv._id)">保存</el-button>
        <el-button class="primary" @click="removeLoginEnv(index,loginEnv._id)">删除</el-button>
    </el-card>

</div>
</template>

<script>
import global from '@/config/global'

export default {
    inject: ['reload'],
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
            this.axios.post(global.backEndUrl + global.backEndPath["updateLoginEnv"],this.loginEnvList[index])
            .then((res)=>{
                console.log(res)
                this.reload()
            })
        },
        removeLoginEnv(index,_id) {
            if(_id !=''){
                this.$confirm('当前环境已保存并可已被项目引用，如删除会造成接口项目无法运行，确认删除吗')
                .then(_ => {
                    this.axios.post(global.backEndUrl + global.backEndPath["deleteLoginEnv"], _id)
                        .then((res) => {
                            this.reload()
                        })
                    done();
                })
                .catch(_ => {

                });
            }else{
                this.loginEnvList.splice(index, 1)
            }
        },
    },
    created() {
        this.axios.get(global.backEndUrl + global.backEndPath["getAllLoginEnv"])
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
