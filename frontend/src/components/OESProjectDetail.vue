<template>
<div id="OESProjectDetail">
    <div>{{projectName}}/{{projectAuthor}}/{{url}}/{{projectDescription}}</div>
    <el-button type="primary" @click="showDialog('','',oesProjectId)">新建VA</el-button>
    <el-card class="box-card" v-for="(inter,index) in OESInterList" :key="index">
        <div>
            <span>接口名称：</span>
            <span>{{inter.interName}}</span>
        </div>
        <div>
            <span>接口说明：</span>
            <span>{{inter.description}}</span>
        </div>
        <hr style="border:1px double #e8e8e8" />
        <div>
            <span>返回结果：</span><br>
            <span>{{inter.response}}</span>
        </div>
        <el-button @click="showDialog(inter._id,inter.InterName,oesProjectId)">编辑</el-button>
        <el-button @click="deleteVA(inter._id,oesProjectId)">删除</el-button>
    </el-card>
</div>
</template>

<script>
import global from '@/config/global'

export default {
    name: "OESProjectDetail",
    inject: ['reload'],
    data() {
        return {
            projectName: '',
            projectAuthor: '',
            url: '',
            projectDescription: '',
            oesProjectId: this.$route.query.projectId,
            OESInterList: []
        }
    },
    methods: {
        showDialog: function (Inter_ID,InterName, oesProjectId) {
            this.$emit('showDialog', Inter_ID,InterName, oesProjectId)
        },
        deleteVA: function (Inter_ID, oesProjectId) {
            this.$confirm('删除为不可逆操作，确认删除吗')
                .then(_ => {
                    this.axios.get(global.backEndUrl + global.backEndPath["deleteOESProjectInter"], {
                            params: {
                                oesInterId: Inter_ID,
                                oesProjectId: oesProjectId,
                            }
                        })
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
        this.axios.get(global.backEndUrl + global.backEndPath["getOESProjectById"], {
                params: {
                    oesProjectId: this.$route.query.projectId
                }
            })
            .then((response) => {
                var projectInfo = response["data"]
                this.projectName = projectInfo["projectName"]
                this.projectAuthor = projectInfo["author"]
                this.url = projectInfo["url"]
                this.projectDescription = projectInfo["description"]
            })
        this.axios.get(global.backEndUrl + global.backEndPath["getOESProjectInterList"], {
                params: {
                    oesProjectId: this.$route.query.projectId
                }
            })
            .then((res) => {
                this.OESInterList = res["data"]
            })
    },
}
</script>
