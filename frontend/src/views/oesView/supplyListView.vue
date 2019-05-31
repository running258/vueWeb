<template>
<div class="supplyListView">
    <supplyList/>
</div>
</template>

<script>
import supplyList from '@/components/oes/supplyList.vue';

export default {
    name: 'supplyListView',
    inject: ['reload'],
    components: {
        supplyList,
    },
    data() {
        return {
            // interProject:"interProject",
            // interLoginEnv:"interLoginEnv",
            // projectShow: false,
            // projectId:'',

            // interShow: false,
            // interId:'',
            // name:'',
        }
    },
    methods: {
        // reloadPage: function () {
        //     this.reload()
        // },
        // projectWin: function (projectId) {
        //     this.projectShow = true
        //     this.projectId = projectId
        // },
        // closeProjectWin:function(){
        //     this.projectShow = false
        //     this.reload()
        // },
        // interShowFun:function(interId,name){
        //     this.interShow = true
        //     if(interId!=""){
        //         this.interId = interId
        //         this.name = name
        //     }
        // },
        
    }
}
</script>
