<template>
<div id="InterDetailWindow">
    <el-form :model="VAFrom" ref="VAFrom" label-width="110px" class="VAFrom">
        <el-row>
            <el-form-item label="VA名称">
                <el-input placeholder="VA名称" class="VA" v-model="VAFrom.VAName"></el-input>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item label="VA描述">
                <el-input type="textarea" :autosize="{ minRows: 1, maxRows: 4}" placeholder="描述" v-model="VAFrom.description"></el-input>
            </el-form-item>
        </el-row>
        <el-row>
            <el-form-item label="返回结果">
                <el-input type="textarea" :autosize="{ minRows: 5, maxRows: 30}" placeholder="返回结果" v-model="VAFrom.response"></el-input>
            </el-form-item>
        </el-row>
        <el-form-item>
            <el-button type="primary" @click="save()">保存</el-button>
            <el-button @click="closeDialog">取消</el-button>
        </el-form-item>
    </el-form>

</div>
</template>

<script>
import global from '@/config/global'

export default {
    props: {
        VA_ID: String,
        VAName: String,
        projectId: String,
    },
    data() {
        return {
            VAFrom: {
                VAName: '',
                description: '',
                response: '',
            },
            VAInfo:{}
        };
    },
    methods: {
        closeDialog: function () {
            this.$emit('closeDialog')
        },
        save: function () {
            this.VAInfo = {
                "VA_ID": this.VA_ID,
                "VAName": this.VAFrom.VAName,
                "description": this.VAFrom.description,
                "response": JSON.parse(this.VAFrom.response),
            }
            if (this.VA_ID == '' || this.VA_ID == null) {
                this.VAInfo["projectId"] = this.projectId
                this.axios.post(global.backEndUrl + global.backEndPath["insertVA"], this.VAInfo)
                    .then((res) => {
                        this.closeDialog()
                    })
            } else {
                this.VAInfo["VA_ID"] = this.VA_ID
                this.axios.post(global.backEndUrl + global.backEndPath["updateProjectVA"],this.VAInfo)
                    .then((res) => {
                        this.closeDialog()
                    })
            }
        },
    },
    created() {
        if (this.VA_ID != '' && this.VA_ID != null) {
            this.axios.get(global.backEndUrl + global.backEndPath["getProjectVA"] + "/" + this.VA_ID)
                .then((res) => {
                    this.VAinfo = res["data"]
                    this.VAFrom.VAName = this.VAinfo["VAName"]
                    this.VAFrom.description = this.VAinfo["description"]
                    this.VAFrom.response = JSON.stringify(this.VAinfo["response"])
                })
        }
    },
};
</script>
