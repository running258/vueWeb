<template>
<div class="VAProjectView">
    <VAProjectList @showWin="changeWin"/>
    <el-dialog :title="titleName" :visible.sync="projectShow" :before-close="reloadPage" width="50%">
        <VAProjectWindow :type="windowType" @closeProjectWin="projectWinHide"/>
    </el-dialog>
</div>
</template>

<script>
import VAProjectList from '@/components/VAProjectList.vue';
import VAProjectWindow from '@/components/VAProjectWindow.vue';

export default {
    name: 'VAProjectView',
    inject: ['reload'],
    components: {
        VAProjectList,
        VAProjectWindow,
    },
    data() {
        return {
            projectShow: false,
            windowType: '',
            titleName:'',
            interShow: false,
            interType:'',
            interId:'',
        }
    },
    methods: {
        reloadPage: function () {
            this.reload()
        },
        changeWin: function (type) {
            this.projectShow = true
            this.windowType = type
            if(type == "new"){
                this.titleName = "新建VA项目"
            }else if(type == "edit"){
                this.titleName = "编辑VA项目"
            }
        },
        projectWinHide:function(){
            this.projectShow = false
            this.reload()
        },
        
    }
}
</script>
