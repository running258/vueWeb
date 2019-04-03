<template>
<div class="VAProjectView">
    <OESProjectList @showWin="changeWin"/>
    <el-dialog :title="titleName" :visible.sync="projectShow" :before-close="reloadPage" width="50%">
        <OESProjectWindow :type="windowType" :projectId="projectId" @closeProjectWin="projectWinHide"/>
    </el-dialog>
</div>
</template>

<script>
import OESProjectList from '@/components/OESProjectList.vue';
import OESProjectWindow from '@/components/OESProjectWindow.vue';

export default {
    name: 'VAProjectView',
    inject: ['reload'],
    components: {
        OESProjectList,
        OESProjectWindow,
    },
    data() {
        return {
            projectShow: false,
            projectId: '',
            windowType: '',
            titleName:'',
        }
    },
    methods: {
        reloadPage: function () {
            this.reload()
        },
        changeWin: function (type,projectId) {
            this.projectShow = true
            this.windowType = type
            if(type == "new"){
                this.titleName = "新建项目"
            }else if(type == "edit"){
                this.titleName = "编辑项目"
                this.projectId = projectId
            }
        },
        projectWinHide:function(){
            this.projectShow = false
            this.reload()
        },
        
    }
}
</script>
