<template>
<div id="Project">
    <!-- <el-card class="box-card" v-for="(project,index) in projects" :key="index">
        <div slot="header" class="clearfix">
            <router-link :to="'/ProjectDetails/'+index"><span>{{project.projectName}}</span></router-link>
        </div>
        <div v-for="o in 4" :key="o" class="text item">
            {{'列表内容 ' + o }}
        </div>
    </el-card> -->

    <!-- <el-row>
        <el-col :span="12"></el-col>
        <el-col :span="12">
            <div class="grid-content bg-purple-light"></div>
        </el-col>
    </el-row>
    <el-autocomplete v-model="state4" :fetch-suggestions="querySearchAsync" placeholder="项目名称查询" @select="handleSelect" clearable></el-autocomplete>
    <el-button type="primary" @click="dialogVisible = true">新建项目</el-button> -->
    <!--  -->
    <el-card class="box-card" v-for="(project,index) in allProjects" :key="index">
        <div slot="header" class="clearfix">
            <router-link :to="'/ProjectDetails/'+index"><span>{{project.projectName}}</span></router-link>  <span>{{project.author}}/{{project.description}}</span>
        </div>
        <div v-for="(inter,index) in project.interfaces" :key="index"><router-link :to="'/InterfaceDetail/'+inter.interName">{{inter.interName}}</router-link></div>
    </el-card>

    <!-- <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
        <span>项目名称</span>
        <el-input v-model="newProjectName" placeholder="项目名称"></el-input>
        <el-radio-group v-model="accessRadio">
            <el-radio :label="0">公开</el-radio>
            <el-radio :label="1">私有</el-radio>
        </el-radio-group>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="saveNewProject()">确 定</el-button>
        </span>
    </el-dialog> -->

</div>
</template>

<script>
export default {
    name: "Project",
    data() {
        return {
            allProjects:[],     //全部项目
            restaurants: [],
            state4: '',
            timeout: null,
            dialogVisible: false,
            accessRadio: 0,
            newProjectName: ''
        }
    },
    methods: {
        // loadAll() {
        //     return [{
        //             "value": "三全鲜食（北新泾店）",
        //             "address": "长宁区新渔路144号"
        //         },
        //         {
        //             "value": "Hot honey 首尔炸鸡（仙霞路）",
        //             "address": "上海市长宁区淞虹路661号"
        //         }
        //     ];
        // },
        // querySearchAsync(queryString, cb) {
        //     var restaurants = this.restaurants;
        //     var results = queryString ? restaurants.filter(this.createStateFilter(queryString)) : restaurants;
        //     clearTimeout(this.timeout);
        //     this.timeout = setTimeout(() => {
        //         cb(results);
        //     }, 3000 * Math.random());
        // },
        // createStateFilter(queryString) {
        //     return (state) => {
        //         return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        //     };
        // },
        // handleSelect(item) {
        //     console.log(item);
        // },
        // handleClose(done) {
        //     this.$confirm('确认关闭？')
        //         .then(_ => {
        //             done();
        //         })
        //         .catch(_ => {});
        // },
        saveNewProject() {
            this.projects.push({
                "projectName": this.newProjectName
            })
            this.dialogVisible = false
        }
    },
    created() {
        // this.restaurants = this.loadAll();
        // 加载所有项目
        this.axios.get('http://localhost:5000/projects')
            .then((response) => {
                this.allProjects = response["data"]
            })
    }
}
</script>

<style lang="scss">

</style>
