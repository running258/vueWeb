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
    },
    data() {
        return {
            VAFrom: {
                VAName: '',
                description: '',
                response: '',
            },
        };
    },
    methods: {
        closeDialog: function () {
            this.$emit('closeDialog')
        },
        save: function () {
            var VAInfo = {
                "VAName": this.VAFrom.VAName,
                "description": this.VAFrom.description,
                "response": this.VAFrom.response,
            }
            if (this.VA_ID == '' || this.VA_ID == null) {
                this.axios.post(global.backEndUrl + global.backEndPath["insertVA"], VAInfo)
                    .then((res) => {
                        this.closeDialog()
                    })
            } else {

            }
        },
    },
    created() {
        if (this.VAName != '' && this.VAName != null) {
            this.axios.get(global.backEndUrl + global.backEndPath["getVA"] + "/" + this.VAName)
                .then((res) => {
                    var VAinfo = res["data"]
                    this.VAFrom.VAName = VAinfo["VAName"]
                    this.VAFrom.description = VAinfo["description"]
                    this.VAFrom.response = JSON.stringify(VAinfo["response"])
                })
        }
    },
};
</script>
