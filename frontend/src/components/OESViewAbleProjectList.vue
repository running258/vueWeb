<template>
<div id="OESViewAbleProjectList">
    <el-button @click="addEnvCard()">add</el-button>
    <el-card v-for="(oesViewAbleProject, index) in oesViewAbleProjectList" :key="index">
        <div>
            <el-input class="urlInput" v-if="oesViewAbleProject._id==''" v-model="oesViewAbleProject.name"></el-input>
            <el-input class="urlInput" v-if="oesViewAbleProject._id!=''" v-model="oesViewAbleProject.name" disabled></el-input>
        </div>
        <div><span>url:</span></div>
        <div>
            <el-input class="urlInput" v-model="oesViewAbleProject.url"></el-input>
        </div>
        <div><span>signature:</span></div>
        <div>
            <el-input class="urlInput" v-model="oesViewAbleProject.signature"></el-input>
        </div>
        <div><span>hospId:</span></div>
        <div>
            <el-input class="urlInput" v-model="oesViewAbleProject.hospId"></el-input>
        </div>
        <div><span>描述:</span>
            <el-input type="textarea" v-model="oesViewAbleProject.description"></el-input>
        </div>
        <el-button class="primary" @click="saveLoginEnv(index,oesViewAbleProject._id)">保存</el-button>
        <el-button class="primary" v-if="oesViewAbleProject._id==''" @click="removeLoginEnv(index)">删除</el-button>
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
            oesViewAbleProjectList: [],
            searchName: "",
        }
    },
    methods: {
        addEnvCard() {
            var EmptyList = {
                "name": "",
                "url": "",
                "signature": "",
                "hospId": "",
                "description": "",
                "_id": "",
                "collectionName":this.collectionName
            }
            this.oesViewAbleProjectList.push(EmptyList)
        },
        saveLoginEnv(index, _id) {
            var projectInfo = JSON.stringify(this.oesViewAbleProjectList[index])
            projectInfo = JSON.parse(projectInfo)
            projectInfo["_id"] = _id
            console.log(projectInfo)
            this.commonJs.save(projectInfo)
                .then((res) => {
                    this.reload()
                })
        },
        removeLoginEnv(index) {
            this.oesViewAbleProjectList.splice(index, 1)
        },
    },
    created() {
        this.commonJs.getList(this.collectionName, this.searchName)
            .then((res) => {
                this.oesViewAbleProjectList = res["data"]
            })
    }
}
</script>

<style>
.urlInput {
    width: 500px
}
</style>
