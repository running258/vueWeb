<template>
<div id="ProjectWindow">
    <el-form :model="vaProjectInfoForm" :rules="rules" ref="vaProjectInfoForm" label-width="110px" class="vaProjectInfoForm">
        <el-row>
            <el-col :span="11">
                <el-form-item label="项目名称" prop="vaProjectName">
                    <el-input v-model="vaProjectInfoForm.vaProjectName"></el-input>
                </el-form-item>
            </el-col>
            <el-col :span="11">
                <el-form-item label="创建人" prop="author">
                    <el-input v-model="vaProjectInfoForm.author"></el-input>
                </el-form-item>
            </el-col>
        </el-row>
        <el-form-item label="项目描述" prop="description">
            <el-input type="textarea" v-model="vaProjectInfoForm.description"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitForm('vaProjectInfoForm',type)">确定</el-button>
            <el-button @click="resetForm('vaProjectInfoForm')">重置</el-button>
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
            vaProjectJson: {},
            vaProjectInfoForm: {
                vaProjectName: '',
                author: '',
                description: "",
            },
            vaList: [],
            rules: {
                vaProjectName: [{
                    required: true,
                    message: '请输入项目名称',
                    trigger: 'blur'
                }],
                author: [{
                    required: true,
                    message: '请输入创建人',
                    trigger: 'blur'
                }]
            }
        }
    },
    methods: {
        formatVAProjectJson:function() {
            this.vaProjectJson = {
                "collectionName": "vaProject",
                "vaProjectName": this.vaProjectInfoForm.vaProjectName,
                "author": this.vaProjectInfoForm.author,
                "description": this.vaProjectInfoForm.description,
                "vaList": this.vaList
            }
        },
        submitForm:function(formName, type) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    if (type == "new") {
                        this.formatVAProjectJson()
                        this.axios.post(global.backEndUrl + global.backEndPath["insertVAProject"], this.vaProjectJson)
                            .then((res) => {
                                this.$emit('closeProjectWin')
                            })
                    } else if (type == 'edit') {
                        this.formatVAProjectJson()
                        this.vaProjectJson["_id"] = this.projectId
                        this.axios.post(global.backEndUrl + global.backEndPath["updateVAProject"], this.vaProjectJson)
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
        close: function () {
            this.$emit('closeProjectWin')
        },
        resetForm:function(formName) {
            this.$refs[formName].resetFields();
        }
    },
    created() {
        if (this.type == 'edit') {
            this.axios.get(global.backEndUrl + global.backEndPath["getVAProjectsByProjectId"], {
                params: {
                    vaProjectId: this.projectId
                }
            })
            .then((res)=>{
                var info = res["data"]
                this.vaProjectInfoForm.vaProjectName = info["vaProjectName"]
                this.vaProjectInfoForm.author = info["author"]
                this.vaProjectInfoForm.description = info["description"]
                this.vaList = info["vaList"]
            })
        }
    },
}
</script>
