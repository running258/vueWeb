<template>
<div id="VAList">
    <div>{{vaProjectName}}/{{projectAuthor}}/{{projectDescription}}</div>
    <el-button type="primary" @click="showVADialog('new','','')">新建VA</el-button>
    <span>使用说明：调用VA时请使用  “http://192.168.96.28:90/+项目名称+/getVAResponse/+VA名称 </span>
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
            vaProjectName: '',
            projectAuthor: '',
            projectDescription: '',
            VAList: []
        }
    },
    methods: {
        showVADialog: function (type, VA_ID, VAName) {
            this.$emit('showVADialog', type, VA_ID, VAName, this.$route.query.vaProjectId)
        },
        deleteVA: function (VA_ID) {
            this.$confirm('删除为不可逆操作，确认删除吗')
                .then(_ => {
                    this.axios.get(global.backEndUrl + global.backEndPath["deleteProjectVA"], {
                            params: {
                                VA_ID: VA_ID,
                                projectId: this.$route.query.vaProjectId,
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
        this.axios.get(global.backEndUrl + global.backEndPath["getVAProjectsByProjectId"], {
                params: {
                    vaProjectId: this.$route.query.vaProjectId
                }
            })
            .then((response) => {
                var projectInfo = response["data"]
                this.vaProjectName = projectInfo["vaProjectName"]
                this.projectId = projectInfo["projectId"]
                this.projectAuthor = projectInfo["author"]
                this.projectDescription = projectInfo["description"]
            })
        this.axios.get(global.backEndUrl + global.backEndPath["getProjectVAList"], {
                params: {
                    vaProjectId: this.$route.query.vaProjectId
                }
            })
            .then((res) => {
                this.VAList = res["data"]
            })
    },
}
</script>
