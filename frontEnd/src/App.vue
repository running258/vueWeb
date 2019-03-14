<template>
<div id="app">
    <el-container>
        <el-aside width="200px" height="100%">
          <MenuBar></MenuBar>
        </el-aside>
        <el-main>
            <router-view></router-view>
        </el-main>
    </el-container>
    
    
</div>
</template>

<script>
import MenuBar from './components/MenuBar'
import Project from './components/Project'

export default {
    name: 'app',
    data() {
        return {}
    },
    components:{
        'MenuBar':MenuBar,
        'Project':Project
    }
}
</script>

<style lang="scss">
 
</style>
