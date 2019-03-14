<template>
<div id="Project">

    <el-row>
        <el-col :span="12"></el-col>
        <el-col :span="12">
            <div class="grid-content bg-purple-light"></div>
        </el-col>
    </el-row>
    <el-button type="primary" @click="dialogVisible = true">新建项目</el-button>
    <el-card class="box-card" v-for="(project,index) in allProjects" :key="index">
        <div slot="header" class="clearfix">
            <router-link :to="'/ProjectDetail/'+project.projectName"><span>{{project.projectName}}</span></router-link> <span class="authorAndDes">{{project.author}}/{{project.description}}</span>
        </div>
        <div v-for="(inter,index) in project.interfaces" :key="index">
            <router-link :to="'/project/'+project.projectName+'/InterfaceDetail/'+inter.interId">{{inter.interName}}</router-link>
        </div>
    </el-card>

    <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
        <span>项目名称</span>
        <el-input v-model="newProjectName" placeholder="项目名称"></el-input>
        <el-input v-model="author" placeholder="项目名称"></el-input>
        <el-input type="textarea" v-model="description" placeholder="描述"></el-input>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="saveNewProject()">确 定</el-button>
        </span>
    </el-dialog>

</div>
</template>

<script>
export default {
    name: "Project",
    data() {
        return {
            author: "",
            description: "",
            allProjects: [],
            restaurants: [],
            state4: '',
            timeout: null,
            dialogVisible: false,
            accessRadio: 0,
            newProjectName: '',
            projectJson: {}
        }
    },
    methods: {
        handleClose(done) {
            this.$confirm('确认关闭？')
                .then(_ => {
                    done();
                })
                .catch(_ => {});
        },
        saveNewProject() {
            this.formatProjectJson()
            console.log(this.projectJson)
            this.axios.post("http://localhost:5000/insertNewProject", this.projectJson)
                .then((res) => {
                    console.log(res)
                })
        },
        formatProjectJson() {
            this.projectJson = {
                "projectName": this.newProjectName,
                "author": this.author,
                "description": this.description,
                "interfaces": []
            }
        }
    },
    created() {
        // 加载所有项目
        this.axios.get('http://localhost:5000/getProjects')
            .then((response) => {
                this.allProjects = response["data"]
            })
    }
}
</script>

<style lang="scss">
    .authorAndDes{
        font-style: italic,
    }
</style>
