<template>
<div id="OESInterWindow">
    <el-form :model="interForm" :rules="rules" ref="interForm" label-width="110px" class="interForm">
        <el-row>
            <el-col :span="11">
                <el-form-item label="接口名称" prop="interName">
                    <el-input placeholder="接口名称" v-model="interForm.interName"></el-input>
                </el-form-item>
            </el-col>
            <el-col :span="11">
                <el-form-item label="path" prop="path">
                    <el-input placeholder="path" v-model="interForm.path"></el-input>
                </el-form-item>
            </el-col>
        </el-row>
        <el-row>
            <el-form-item label="接口描述">
                <el-input type="textarea" :autosize="{ minRows: 1, maxRows: 4}" placeholder="描述" v-model="interForm.description"></el-input>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item label="raw" prop="raw">
                <el-input type="textarea" :autosize="{ minRows: 8}" placeholder="raw" v-model="interForm.raw"></el-input>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item label="response">
                <el-input type="textarea" :autosize="{ minRows: 5, maxRows: 30}" placeholder="response" v-model="interForm.response" :disabled="true"></el-input>
            </el-form-item>
        </el-row>
        <el-form-item>
            <el-button type="primary" @click="submitForm('interForm')">保存</el-button>
            <el-button type="primary" @click="run(oesProjectId,Inter_ID)">运行</el-button>
            <el-button @click="resetForm('interForm')">重置</el-button>
            <el-button @click="closeDialog">取消</el-button>
        </el-form-item>
    </el-form>

</div>
</template>

<script>
import global from '@/config/global'

export default {
    props: {
        Inter_ID: String,
        oesProjectId: String,
    },
    data() {
        return {
            interForm: {
                interName: '',
                description: '',
                path: '',
                raw: '',
                response: '',
            },
            rules: {
                interName: [{
                    required: true,
                    message: '请输入接口名称',
                    trigger: 'blur'
                }],
                path: [{
                    required: true,
                    message: '请输入path',
                    trigger: 'blur'
                }],
                raw: [{
                    required: true,
                    message: '请输入request',
                    trigger: 'blur'
                }]
            },
            interInfo: {}
        };
    },
    methods: {
        closeDialog: function () {
            this.$emit('closeDialog')
        },
        submitForm: function (formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.interInfo = {
                        "Inter_ID": this.Inter_ID,
                        "interName": this.interForm.interName,
                        "description": this.interForm.description,
                        "path": this.interForm.path,
                        "raw": JSON.parse(this.interForm.raw),
                        "oesProjectId": this.oesProjectId,
                    }
                    this.axios.post(global.backEndUrl + global.backEndPath["saveOESInter"], this.interInfo)
                        .then((res) => {
                            this.closeDialog()
                        })

                } else {
                    console.log('oops! there something wrong while submit, try again later!');
                    return false;
                }
            })
        },
        resetForm: function (formName) {
            this.$refs[formName].resetFields();
        },
        run: function (oesProjectId,Inter_ID) {
            this.axios.get(global.backEndUrl + global.backEndPath["runOESInter"], {
                    params: {
                        oesInterId: this.Inter_ID,
                        oesProjectId: this.oesProjectId
                    }
                })
                .then((res) => {
                    console.log(res)
                    this.interForm.response = res["data"]
                })
        },
    },
    created() {
        if (this.Inter_ID != '' && this.Inter_ID != null) {
            this.axios.get(global.backEndUrl + global.backEndPath["getOESInterById"], {
                    params: {
                        oesInterId: this.Inter_ID
                    }
                })
                .then((res) => {
                    this.interInfo = res["data"]
                    this.interForm.interName = this.interInfo["interName"]
                    this.interForm.path = this.interInfo["path"]
                    this.interForm.description = this.interInfo["description"]
                    this.interForm.raw = JSON.stringify(this.interInfo["raw"])
                })
        }
    },
};
</script>
