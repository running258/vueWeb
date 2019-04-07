<template>
<div class="ProjectView">
    <InterProjectList @projectWin="projectWin" @interWindow="interShowFun" :collectionName="interProject"/>
    <el-dialog :visible.sync="projectShow" :before-close="reloadPage" width="50%">
        <InterProjectWindow @closeProjectWin="closeProjectWin"/>
    </el-dialog>
    <!-- <el-dialog :title="interType" :visible.sync="interShow" :before-close="reloadPage" width="50%">
        <InterDetailWindow :interId="interId" :projectName="projectName" :interType="interType"/>
    </el-dialog> -->
</div>
</template>

<script>
import InterProjectList from '@/components/InterProjectList.vue';
import InterProjectWindow from '@/components/InterProjectWindow.vue';
// import InterDetailWindow from '@/components/InterDetailWindow.vue';

export default {
    name: 'ProjectView',
    inject: ['reload'],
    components: {
        InterProjectList,
        InterProjectWindow,
        // InterDetailWindow
    },
    data() {
        return {
            interProject:"interProject",
            projectShow: false,
            interShow: false,
            interType:'',
            interId:'',
            projectName:'',
            projectId:''
        }
    },
    methods: {
        reloadPage: function () {
            this.reload()
        },
        projectWin: function (projectId) {
            this.projectShow = true
            this.projectId = projectId
        },
        closeProjectWin:function(){
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
