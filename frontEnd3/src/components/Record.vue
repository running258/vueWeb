<template>
    <div id="Record">
        <el-select v-model="sys" slot="prepend" placeholder="请选择">
                <el-option label="staging" value="staging"></el-option>
                <el-option label="test" value="test"></el-option>
                <el-option label="demo" value="demo"></el-option>
        </el-select>
        <el-input v-model="http"></el-input>
        <el-button @click="hereWeGo()">Here We Go</el-button>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                sys:'staging',
                http:'https://vhsupply.staging.viewchain.net'
            }
        },
        methods: {
            hereWeGo(){
                var runEnv = {"sys":this.sys,"http":this.http}
                this.axios.post("http://localhost:5000/Record",runEnv)
                .then((res)=>{
                    console.log(res)
                })
            }
        },
    }
</script>

