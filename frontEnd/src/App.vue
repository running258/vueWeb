<template>
<div id="app">
    <el-container>
        <el-aside width="200px" height="100%">
            <MenuBar></MenuBar>
        </el-aside>
        <el-main>
            <router-view v-if="isRouterAlive"></router-view>
        </el-main>
    </el-container>
</div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue'

export default {
    name: 'app',
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
    }
}
</script>

<style>

</style>
