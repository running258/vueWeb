<template>
<div class="ProjectView">
    <InterProjectList @projectWin="projectWin" @interWindow="interShowFun" :projectCollectionName="interProject"/>
    <el-dialog :visible.sync="projectShow" :before-close="reloadPage" width="50%">
        <InterProjectWindow @closeProjectWin="closeProjectWin" :loginCollectionName="interLoginEnv" :projectCollectionName="interProject" :projectId="projectId"/>
    </el-dialog>
    <!-- <el-dialog :visible.sync="interShow" :before-close="reloadPage" width="50%">
        <InterDetailWindow :interId="interId" :name="name"/>
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
            interLoginEnv:"interLoginEnv",
            projectShow: false,
            projectId:'',

            interShow: false,
            interId:'',
            name:'',
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
        interShowFun:function(interId,name){
            this.interShow = true
            if(interId!=""){
                this.interId = interId
                this.name = name
            }
        },
        
    }
}
</script>
