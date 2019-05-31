<template>
<div id="oesMainPage">
     {{this.$route.query}}
    {{this.$store.state.oesViewAbleProjectId}}
    {{this.$store.state.setOESViewAbleProjectName}}

    <el-header>
        <MenuBar/>
    </el-header>
    <el-main>
        <router-view v-if="isRouterAlive"></router-view>
    </el-main>


</div>
</template>

<script>
import MenuBar from '@/components/oes/OESMenuBar.vue'

export default {
    name: 'oesMainPage',
    components: {
        MenuBar
    },
    provide () {
        return{
            reload: this.reload
        }
    },
    data () {
        return{
            isRouterAlive: true
        }
    },
    methods:{
        reload() {
            this.isRouterAlive = false
            this.$nextTick(function () {
                this.isRouterAlive = true
            })
        }
    },
    created() {

    },
}
</script>

<style>

</style>
