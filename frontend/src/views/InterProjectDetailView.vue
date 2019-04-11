<template>
<div class="ProjectDetailView">
    <InterProjectDetail @interWindow="interShowFun" :projectCollectionName="projectCollectionName" :interCollectionName="interCollectionName" :loginEnvCollectionName="loginEnvCollectionName"/>
    <el-dialog :title="interType" :visible.sync="interShow" :before-close="reloadPage" width="50%">
        <InterDetailWindow :interId="interId" :projectId="projectId" @closeInterWindow="interHideFun" :projectCollectionName="projectCollectionName" :interCollectionName="interCollectionName"/>
    </el-dialog>
</div>
</template>

<script>
import InterProjectDetail from '@/components/InterProjectDetail.vue';
import InterDetailWindow from '@/components/InterDetailWindow.vue';

export default {
    name: 'ProjectDetailView',
    inject: ['reload'],
    components: {
        InterProjectDetail,
        InterDetailWindow,
    },
    data() {
        return {
            projectCollectionName:"interProject",
            interCollectionName:"inter",
            loginEnvCollectionName:"interLoginEnv",
            interShow: false,
            interType: '',
            interId: '',
            projectId: '',
        }
    },
    methods: {
        reloadPage: function () {
            this.reload()
        },
        interShowFun: function (interId, projectId) {
            this.interShow = true
            if (interId != "") {
                this.interType = "编辑"
                this.interId = interId
            } else {
                this.interType = "新建"
                this.interId = ''
            }
            this.projectId = projectId
        },
        interHideFun: function () {
            this.interShow = false
            this.reload()
        },
    }
}
</script>
