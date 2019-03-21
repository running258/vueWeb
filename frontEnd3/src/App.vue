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

export default {
    name: 'app',
    data() {
        return {}
    },
    components:{
        'MenuBar':MenuBar
    }
}
</script>

<style lang="scss">
 
</style>
