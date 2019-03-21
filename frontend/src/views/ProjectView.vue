<template>
<div class="ProjectView">
    <ProjectList />
    {{dialogVisible}}
    <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" @showWin="showWindow">
        <ProjectWindow />
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
            dialogVisible: false
        }
    },
    methods: {
        showWindow:function(data) {
            console.log(data)
            this.dialogVisible = true
            console.log("11111111")
        }
    },
}

// https://segmentfault.com/a/1190000011744210?utm_source=tuicool&utm_medium=referral
// https://www.cnblogs.com/peko/p/7465191.html

</script>
