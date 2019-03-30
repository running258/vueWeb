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
            vaProjectJson: {},
            vaProjectInfoForm: {
                vaProjectName: '',
                author: '',
                description: "",
            },
            vaList:[],
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
        formatVAProjectJson() {
            this.vaProjectJson = {
                "vaProjectName": this.vaProjectInfoForm.vaProjectName,
                "author": this.vaProjectInfoForm.author,
                "description": this.vaProjectInfoForm.description,
                "vaList": this.vaList
            }
        },
        submitForm(formName, type) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    if (type == "new") {
                        this.formatVAProjectJson()
                        console.log(this.vaProjectJson)
                        this.axios.post(global.backEndUrl + global.backEndPath["insertVAProject"], this.vaProjectJson)
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
        }
    }
}
</script>
