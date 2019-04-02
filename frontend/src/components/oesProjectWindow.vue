<template>
<div id="ProjectWindow">
    <el-form :model="projectInfoForm" :rules="rules" ref="projectInfoForm" label-width="110px" class="projectInfoForm">
        <el-row>
            <el-col :span="11">
                <el-form-item label="项目名称" prop="projectName">
                    <el-input v-model="projectInfoForm.projectName"></el-input>
                </el-form-item>
            </el-col>
            <el-col :span="11">
                <el-form-item label="创建人" prop="author">
                    <el-input v-model="projectInfoForm.author"></el-input>
                </el-form-item>
            </el-col>
        </el-row>
        <el-form-item label="网关地址">
            <el-col :span="11">
                <el-form-item prop="url">
                    <el-input v-model="projectInfoForm.url" :disabled="true"></el-input>
                </el-form-item>
            </el-col>
        </el-form-item>
        <el-form-item label="描述" prop="description">
            <el-input type="textarea" v-model="projectInfoForm.description"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitForm('projectInfoForm',type)">确定</el-button>
            <el-button @click="resetForm('projectInfoForm')">重置</el-button>
        </el-form-item>
    </el-form>

</div>
</template>

<script>
import global from '@/config/global'

export default {
    props: ["type"],
    data() {
        return {
            loginEnvList: [],
            projectJson: {},
            projectInfoForm: {
                projectName: '',
                author: '',
                loginIndex: '',
                env: '',
                supplyUrl: '',
                supplyPath: '',
                hospUrl: '',
                hospPath: '',
                supplyUsername: '',
                supplyPassword: '',
                hospUsername: '',
                hospPassword: '',
                description: "",
            },
            rules: {
                projectName: [{
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
                "projectName": this.projectInfoForm.projectName,
                "author": this.projectInfoForm.author,
                "env": this.projectInfoForm.env,
                "supplyUsername": this.projectInfoForm.supplyUsername,
                "supplyPassword": this.projectInfoForm.supplyPassword,
                "hospUsername": this.projectInfoForm.hospUsername,
                "hospPassword": this.projectInfoForm.hospPassword,
                "description": this.projectInfoForm.description,
                "interfaces": []
            }
        },
        changeEnv() {
            var loginInfo = this.loginEnvList[this.projectInfoForm.loginIndex]
            this.projectInfoForm.env = loginInfo["env"]
            this.projectInfoForm.supplyUrl = loginInfo["supply"]["url"]
            this.projectInfoForm.supplyPath = loginInfo["supply"]["path"]
            this.projectInfoForm.hospUrl = loginInfo["hosp"]["url"]
            this.projectInfoForm.hospPath = loginInfo["hosp"]["path"]
        },
        submitForm(formName, type) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    if (type == "new") {
                        this.formatProjectJson()
                        this.axios.post(global.backEndUrl + global.backEndPath["insertNewProject"], this.projectJson)
                            .then((res) => {
                                this.$emit('closeProjectWin')
                            })
                    }
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
        this.axios.get(global.backEndUrl + global.backEndPath["getAllLoginEnv"])
            .then((res) => {
                this.loginEnvList = res["data"]
            })
    }
}
</script>
