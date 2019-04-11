<template>
<div id="interfaceLoginEnv">
    <el-button @click="addEnvCard()">add</el-button>
    <el-card v-for="(loginEnv, index) in loginEnvList" :key="index">
        <div>
            <el-input class="urlInput" v-if="loginEnv._id==''" v-model="loginEnv.name"></el-input>
            <el-input class="urlInput" v-if="loginEnv._id!=''" v-model="loginEnv.name" disabled></el-input>
        </div>
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
        <el-button class="primary" v-if="loginEnv._id==''" @click="removeLoginEnv(index)">删除</el-button>
    </el-card>

</div>
</template>

<script>

export default {
    inject: ['reload'],
    props: {
        collectionName: String
    },
    data() {
        return {
            loginEnvList: [],
            searchName: "",
        }
    },
    methods: {
        addEnvCard() {
            var EmptyList = {
                "name": "",
                "supply": {
                    "url": "",
                    "path": ""
                },
                "hosp": {
                    "url": "",
                    "path": ""
                },
                "_id": "",
                "collectionName":this.collectionName
            }
            this.loginEnvList.push(EmptyList)
        },
        saveLoginEnv(index, _id) {
            var loginInfo = JSON.stringify(this.loginEnvList[index])
            loginInfo = JSON.parse(loginInfo)
            loginInfo["_id"] = _id
            console.log(loginInfo)
            this.commonJs.save(loginInfo)
                .then((res) => {
                    this.reload()
                })
        },
        removeLoginEnv(index) {
            this.loginEnvList.splice(index, 1)
        },
    },
    created() {
        this.commonJs.getList(this.collectionName, this.searchName)
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
