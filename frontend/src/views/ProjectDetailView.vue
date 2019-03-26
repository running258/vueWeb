<template>
<div class="ProjectDetailView">
    <ProjectDetail @interWindow="interShowFun" />
    <el-dialog :title="interType" :visible.sync="interShow" width="50%">
        <InterDetailWindow :interId="interId" :projectName="projectName" @closeInterWindow="interHideFun"/>
    </el-dialog>
</div>
</template>

<script>
import ProjectDetail from '@/components/ProjectDetail.vue';
import InterDetailWindow from '@/components/InterDetailWindow.vue';

export default {
    name: 'ProjectDetailView',
    inject: ['reload'],
    components: {
        ProjectDetail,
        InterDetailWindow,
    },
    data() {
        return {
            interShow: false,
            interType: '',
            interId: '',
            projectName: '',
        }
    },
    methods: {
        interShowFun: function (interId, projectName) {
            this.interShow = true
            if (interId != "") {
                this.interType = "编辑"
                this.interId = interId
            } else {
                this.interType = "新建"
                this.interId = ''
            }
            this.projectName = projectName
        },
        interHideFun: function () {
            this.interShow = false
            this.reload()
        },
    }
}
</script>
