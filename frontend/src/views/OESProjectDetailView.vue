<template>
<div class="VAView">
    <OESProjectDetail @showDialog="showDialog"/>
    <el-dialog :visible.sync="dialogShow" :before-close="reloadPage" width="50%">
        <OESInterWindow :Inter_ID="Inter_ID" :InterName="InterName" :oesProjectId="oesProjectId" @closeDialog="reloadPage"/>
    </el-dialog>
</div>
</template>

<script>
import OESProjectDetail from '@/components/OESProjectDetail.vue';
import OESInterWindow from '@/components/OESInterWindow.vue';

export default {
    name: 'VAView',
    inject: ['reload'],
    components: {
        OESProjectDetail,
        OESInterWindow,
    },
    data() {
        return {
            dialogTitle:'',
            Inter_ID: '',
            InterName:'',
            oesProjectId: '',
            dialogShow: false,
        }
    },
    methods: {
        reloadPage: function () {
            this.dialogShow=false
            this.reload()
        },
        showDialog: function (Inter_ID,InterName,oesProjectId) {
            this.dialogShow = true
            this.Inter_ID=Inter_ID
            this.InterName=InterName
            this.oesProjectId=oesProjectId
        },
    }
}
</script>
