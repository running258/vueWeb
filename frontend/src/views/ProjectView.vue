<template>
<div class="ProjectView">
    <ProjectList @showWin="changeWin" />
    <el-dialog :title="titleName" :visible.sync="dialogVisible" width="50%">
        <ProjectWindow :type="windowType"/>
    </el-dialog>
</div>
</template>

<script>
import ProjectList from '@/components/ProjectList.vue';
import ProjectWindow from '@/components/ProjectWindow.vue';

export default {
    name: 'ProjectView',
    components: {
        ProjectList,
        ProjectWindow
    },
    data() {
        return {
            dialogVisible: false,
            windowType: '',
            titleName:''
        }
    },
    methods: {
        changeWin: function (type) {
            this.dialogVisible = true
            this.windowType = type
            if(type == "new"){
                this.titleName = "新建项目"
            }else if(type == "edit"){
                this.titleName = "编辑项目"
            }
        }
    }
}
</script>
