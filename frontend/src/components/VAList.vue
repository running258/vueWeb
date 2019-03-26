<template>
<div id="VAList">
    <el-button type="primary" @click="showVADialog('new','','')">新建VA</el-button>
    <el-card class="box-card" v-for="(va,index) in VAList" :key="index">
        <div>
            <span>VA名称：</span>
            <span>{{va.VAName}}</span>
        </div>
        <div>
            <span>VA说明：</span>
            <span>{{va.description}}</span>
        </div>
        <hr style="border:1px double #e8e8e8" />
        <div>
            <span>返回结果：</span><br>
            <span>{{va.response}}</span>
        </div>
        <el-button @click="showVADialog('edit',va._id,va.VAName)">编辑</el-button>
        <el-button @click="deleteVA(va._id)">删除</el-button>
    </el-card>
</div>
</template>

<script>
import global from '@/config/global'

export default {
    name: "VAList",
    inject: ['reload'],
    data() {
        return {
            VAList: []
        }
    },
    methods: {
        showVADialog: function (type,VA_ID,VAName) {
            this.$emit('showVADialog',type,VA_ID,VAName)
        },
        deleteVA: function (VA_ID) {
            this.$confirm('删除为不可逆操作，确认删除吗')
                .then(_ => {
                    this.axios.post(global.backEndUrl + global.backEndPath["deleteVA"], VA_ID)
                        .then((res) => {
                            this.reload()
                        })
                    done();
                })
                .catch(_ => {

                });
        },
    },
    created() {
        this.axios.get(global.backEndUrl + global.backEndPath["VAList"])
            .then((res) => {
                this.VAList = res["data"]
            })
    },
}
</script>
