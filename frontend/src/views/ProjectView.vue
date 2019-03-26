<template>
<div class="ProjectView">
    <ProjectList @showWin="changeWin" @interWindow="interShowFun"/>
    <el-dialog :title="titleName" :visible.sync="projectShow" width="50%">
        <ProjectWindow :type="windowType" @closeProjectWin="projectWinHide"/>
    </el-dialog>
    <el-dialog :title="interType" :visible.sync="interShow" width="50%">
        <InterDetailWindow :interId="interId" :projectName="projectName" :interType="interType"/>
    </el-dialog>
</div>
</template>

<script>
import ProjectList from '@/components/ProjectList.vue';
import ProjectWindow from '@/components/ProjectWindow.vue';
import InterDetailWindow from '@/components/InterDetailWindow.vue';

export default {
    name: 'ProjectView',
    inject: ['reload'],
    components: {
        ProjectList,
        ProjectWindow,
        InterDetailWindow
    },
    data() {
        return {
            projectShow: false,
            windowType: '',
            titleName:'',
            interShow: false,
            interType:'',
            interId:'',
            projectName:'',
        }
    },
    methods: {
        changeWin: function (type) {
            this.projectShow = true
            this.windowType = type
            if(type == "new"){
                this.titleName = "新建项目"
            }else if(type == "edit"){
                this.titleName = "编辑项目"
            }
        },
        projectWinHide:function(){
            this.projectShow = false
            this.reload()
        },
        interShowFun:function(interId,projectName){
            this.interShow = true
            if(interId!=""){
                this.interType = "查看"
                this.interId = interId
                this.projectName = projectName
            }
        },
        
    }
}
</script>
