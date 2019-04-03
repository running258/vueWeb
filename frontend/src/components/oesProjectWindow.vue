<template>
<div id="OESProjectWindow">
    {{projectId}}
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
        <el-form-item label="url" prop="url">
            <el-input type="textarea" v-model="projectInfoForm.url"></el-input>
        </el-form-item>
        <el-row>
            <el-col :span="11">
                <el-form-item label="signature" prop="signature">
                    <el-input v-model="projectInfoForm.signature"></el-input>
                </el-form-item>
            </el-col>
            <el-col :span="11">
                <el-form-item label="hospId" prop="hospId">
                    <el-input v-model="projectInfoForm.hospId"></el-input>
                </el-form-item>
            </el-col>
        </el-row>
        <el-form-item label="项目描述" prop="description">
            <el-input type="textarea" v-model="projectInfoForm.description"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitForm('projectInfoForm',type)">确定</el-button>
            <el-button @click="resetForm('projectInfoForm')">重置</el-button>
            <el-button @click="close">取消</el-button>
        </el-form-item>
    </el-form>

</div>
</template>

<script>
import global from '@/config/global'

export default {
    props: ["type", "projectId"],
    data() {
        return {
            projectJson: {},
            projectInfoForm: {
                projectName: '',
                author: '',
                url: '',
                signature: '',
                hospId: '',
                description: "",
            },
            OESInterList: [],
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
                url: [{
                    required: true,
                    message: '请输入环境地址',
                    trigger: 'blur'
                }],
                signature: [{
                    required: true,
                    message: '请输入医院签名',
                    trigger: 'blur'
                }],
                hospId: [{
                    required: true,
                    message: '请输入医院ID',
                    trigger: 'blur'
                }]
            }
        }
    },
    methods: {
        formatProjectJson: function () {
            this.projectJson = {
                "projectName": this.projectInfoForm.projectName,
                "author": this.projectInfoForm.author,
                "url": this.projectInfoForm.url,
                "signature": this.projectInfoForm.signature,
                "hospId": this.projectInfoForm.hospId,
                "description": this.projectInfoForm.description,
                "OESInterList": this.OESInterList,
                "OES_ID": this.projectId,
            }
        },
        submitForm: function (formName, type) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.formatProjectJson()
                    this.axios.post(global.backEndUrl + global.backEndPath["saveOESProject"], this.projectJson)
                        .then((res) => {
                            this.$emit('closeProjectWin')
                        })

                } else {
                    console.log('oops! there something wrong while submit, try again later!');
                    return false;
                }
            });
        },
        close: function () {
            this.$emit('closeProjectWin')
        },
        resetForm: function (formName) {
            this.$refs[formName].resetFields();
        }
    },
    created() {
        if (this.type == 'edit') {
            this.axios.get(global.backEndUrl + global.backEndPath["getOESProjectById"], {
                    params: {
                        oesProjectId: this.projectId
                    }
                })
                .then((res) => {
                    var info = res["data"]
                    this.projectInfoForm.projectName = info["projectName"]
                    this.projectInfoForm.author = info["author"]
                    this.projectInfoForm.url = info["url"]
                    this.projectInfoForm.signature = info["signature"]
                    this.projectInfoForm.hospId = info["hospId"]
                    this.projectInfoForm.description = info["description"]
                    this.OESInterList = info["OESInterList"]
                })
        }
    },
}
</script>
