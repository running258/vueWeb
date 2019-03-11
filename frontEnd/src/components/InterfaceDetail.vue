<template>
<div id="interfaceDetail">
    <el-container>
        <el-header>
            <loginEnv></loginEnv>
        </el-header>
        <el-main>
            <interForm></interForm>
        </el-main>
    </el-container>
</div>
</template>

<script>
import InterfaceDetailForm from "./InterfaceDetailForm.vue"
import InterfaceLoginEnv from "./InterfaceLoginEnv.vue"

export default {
    name:"interfaceDetail",
    components:{
        'interForm':InterfaceDetailForm,
        'loginEnv':InterfaceLoginEnv
    }
}
</script>

<style>
.el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
}

.el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
}

body>.el-container {
    margin-bottom: 40px;
}
</style>
