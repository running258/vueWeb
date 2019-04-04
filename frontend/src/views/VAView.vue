<template>
<div class="VAView">
    <VAList @showVADialog="showVADialog"/>
    <el-dialog :title="vaDialogTitle" :visible.sync="vaDialogShow" :before-close="reloadPage" width="50%">
        <VAWindow :VA_ID="VA_ID" :VAName="VAName" :projectId="projectId" @closeDialog="reloadPage"/>
    </el-dialog>
</div>
</template>

<script>
import VAList from '@/components/VAList.vue';
import VAWindow from '@/components/VAWindow.vue';

export default {
    name: 'VAView',
    inject: ['reload'],
    components: {
        VAList,
        VAWindow,
    },
    data() {
        return {
            vaDialogTitle:'',
            type:'',
            VA_ID: '',
            VAName: '',
            projectId: '',
            vaDialogShow: false,
        }
    },
    methods: {
        reloadPage: function () {
            this.vaDialogShow=false
            this.reload()
        },
        showVADialog: function (type,VA_ID,VAName,projectId) {
            this.vaDialogShow = true
            if(type==='new'){
                this.vaDialogTitle = '新建'
            }else if(type==='edit'){
                this.vaDialogTitle = '编辑'
            }
            this.VA_ID=VA_ID
            this.VAName=VAName
            this.projectId=projectId
        },
    }
}
</script>
