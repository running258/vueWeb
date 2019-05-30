<template>
<div id="InterProjectWindow">
    <el-form :model="projectInfoForm" :rules="rules" ref="projectInfoForm" label-width="110px" class="projectInfoForm">
        <el-row>
            <el-col :span="11">
                <el-form-item label="项目名称" prop="name">
                    <el-input v-model="projectInfoForm.name"></el-input>
                </el-form-item>
            </el-col>
            <el-col :span="11">
                <el-form-item label="创建人" prop="author">
                    <el-input v-model="projectInfoForm.author"></el-input>
                </el-form-item>
            </el-col>
        </el-row>
        <el-form-item label="环境选择" prop="loginIndex">
            <el-select v-model="projectInfoForm.loginIndex" placeholder="请选择系统环境" @change="changeEnv">
                <el-option v-for="(loginEnv, index) in loginEnvList" :key="index" :label="loginEnv.name" :value="index"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="供端地址">
            <el-col :span="11">
                <el-form-item prop="supplyUrl">
                    <el-input v-model="projectInfoForm.supplyUrl" :disabled="true"></el-input>
                </el-form-item>
            </el-col>
            <el-col :span="11">
                <el-form-item prop="supplyPath">
                    <el-input v-model="projectInfoForm.supplyPath" :disabled="true"></el-input>
                </el-form-item>
            </el-col>
        </el-form-item>
        <el-row>
            <el-form-item label="供端用户/密码">
                <el-col :span="11">
                    <el-form-item prop="supplyUsername">
                        <el-input v-model="projectInfoForm.supplyUsername"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="11">
                    <el-form-item prop="supplyPassword">
                        <el-input v-model="projectInfoForm.supplyPassword"></el-input>
                    </el-form-item>
                </el-col>
            </el-form-item>
        </el-row>
        <el-form-item label="院端地址">
            <el-col :span="11">
                <el-form-item prop="hospUrl">
                    <el-input v-model="projectInfoForm.hospUrl" :disabled="true"></el-input>
                </el-form-item>
            </el-col>
            <el-col :span="11">
                <el-form-item prop="hospPath">
                    <el-input v-model="projectInfoForm.hospPath" :disabled="true"></el-input>
                </el-form-item>
            </el-col>
        </el-form-item>
        <el-row>
            <el-form-item label="院端用户/密码" prop>
                <el-col :span="11">
                    <el-form-item prop="hospUsername">
                        <el-input v-model="projectInfoForm.hospUsername"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="11">
                    <el-form-item prop="hospPassword">
                        <el-input v-model="projectInfoForm.hospPassword"></el-input>
                    </el-form-item>
                </el-col>
            </el-form-item>
        </el-row>

        <el-row>
            <el-form-item label="定时执行">
                <el-col :span="11">
                    <el-form-item>
                        <el-checkbox v-model="projectInfoForm.isTime" @change="isTime">是否定时执行</el-checkbox>
                    </el-form-item>
                </el-col>
                <el-col :span="11">
                    <el-form-item>
                        <el-time-picker v-model="projectInfoForm.runTime"></el-time-picker>
                    </el-form-item>
                </el-col>
            </el-form-item>
        </el-row>

        <el-form-item label="描述" prop="description">
            <el-input type="textarea" v-model="projectInfoForm.description"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitForm('projectInfoForm')">确定</el-button>
            <el-button @click="resetForm('projectInfoForm')">重置</el-button>
        </el-form-item>
    </el-form>

</div>
</template>

<script>
import global from '@/config/global'

export default {
    props: {
        projectId: String,
        loginCollectionName: String,
        projectCollectionName: String
    },
    data() {
        return {
            loginEnvList: [],
            projectJson: {},
            projectInfoForm: {
                name: '',
                author: '',
                loginIndex: '',
                loginEnvId: '',
                supplyUrl: '',
                supplyPath: '',
                hospUrl: '',
                hospPath: '',
                supplyUsername: '',
                supplyPassword: '',
                hospUsername: '',
                hospPassword: '',
                isTime: '',
                runTime: '',
                description: '',
            },
            list: [],
            rules: {
                name: [{
                    required: true,
                    message: '请输入项目名称',
                    trigger: 'blur'
                }],
                author: [{
                    required: true,
                    message: '请输入创建人',
                    trigger: 'blur'
                }],
                loginIndex: [{
                    required: true,
                    message: '请选择系统环境',
                    trigger: 'change'
                }]
            }
        }
    },
    methods: {
        formatProjectJson() {
            this.projectJson = {
                "collectionName": this.projectCollectionName,
                "_id": this.projectId,
                "name": this.projectInfoForm.name,
                "author": this.projectInfoForm.author,
                "loginEnvId": this.projectInfoForm.loginEnvId,
                "supplyUsername": this.projectInfoForm.supplyUsername,
                "supplyPassword": this.projectInfoForm.supplyPassword,
                "hospUsername": this.projectInfoForm.hospUsername,
                "hospPassword": this.projectInfoForm.hospPassword,
                "runTime": this.projectInfoForm.runTime,
                "description": this.projectInfoForm.description,
                "list": this.list
            }
        },
        changeEnv() {
            var loginInfo = this.loginEnvList[this.projectInfoForm.loginIndex]
            this.projectInfoForm.loginEnvId = loginInfo["_id"]
            this.projectInfoForm.supplyUrl = loginInfo["supply"]["url"]
            this.projectInfoForm.supplyPath = loginInfo["supply"]["path"]
            this.projectInfoForm.hospUrl = loginInfo["hosp"]["url"]
            this.projectInfoForm.hospPath = loginInfo["hosp"]["path"]
        },
        isTime: function () {

        },
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.formatProjectJson()
                    console.log(this.projectJson)
                    this.commonJs.save(this.projectJson)
                        .then((res) => {
                            this.$emit('closeProjectWin')
                        })
                } else {
                    console.log('oops! there something wrong while submit, try again later!');
                    return false;
                }
            });

        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        },
        refresh() {
            this.reload()
        }
    },
    created() {
        // 加载所有系统环境
        this.commonJs.getList(this.loginCollectionName, '')
            .then((res) => {
                this.loginEnvList = res["data"]
            })
        if (this.projectId != '') {
            this.commonJs.getById(this.projectCollectionName, this.projectId)
                .then((res) => {
                    var projectInfo = res["data"]
                    this.projectInfoForm.name = projectInfo["name"]
                    this.projectInfoForm.author = projectInfo["author"]
                    this.projectInfoForm.loginEnvId = projectInfo["loginEnvId"]
                    this.projectInfoForm.supplyUsername = projectInfo["supplyUsername"]
                    this.projectInfoForm.supplyPassword = projectInfo["supplyPassword"]
                    this.projectInfoForm.hospUsername = projectInfo["hospUsername"]
                    this.projectInfoForm.hospPassword = projectInfo["hospPassword"]
                    this.projectInfoForm.runTime = projectInfo["runTime"]
                    if (this.projectInfoForm.runTime != '') {
                        this.projectInfoForm.isTime = true
                    } else {
                        this.projectInfoForm.isTime = false
                    }
                    this.projectInfoForm.description = projectInfo["description"]
                    this.list = projectInfo["list"]
                    if (projectInfo["loginEnvId"] != '') {
                        for (let index = 0; index < this.loginEnvList.length; index++) {
                            if (this.loginEnvList[index]["_id"] == projectInfo["loginEnvId"]) {
                                this.projectInfoForm.loginIndex = index
                                this.projectInfoForm.supplyUrl = this.loginEnvList[index]["supply"]["url"]
                                this.projectInfoForm.supplyPath = this.loginEnvList[index]["supply"]["path"]
                                this.projectInfoForm.hospUrl = this.loginEnvList[index]["hosp"]["url"]
                                this.projectInfoForm.hospPath = this.loginEnvList[index]["hosp"]["path"]
                            }

                        }

                    }
                })
        } else {

        }

    }
}
</script>
