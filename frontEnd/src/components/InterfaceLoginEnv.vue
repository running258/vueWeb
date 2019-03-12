<template>
<div id="interfaceLoginEnv">
    <el-select v-model="env" slot="prepend" placeholder="请选择">
        <el-option label="staging" value="staging"></el-option>
        <el-option label="test" value="test"></el-option>
        <el-option label="demo" value="demo"></el-option>
    </el-select>
    <el-select v-model="sys" slot="prepend" placeholder="请选择">
        <el-option label="supply" value="supply"></el-option>
        <el-option label="hosp" value="hosp"></el-option>
    </el-select>
    <el-input v-model="loginUrl"></el-input>

</div>
</template>

<script>
export default {
    data() {
        return {
            env:"",
            loginUrl:""
        }
    },
    created() {
        var interName = this.$route.params.interName
        if (interName != '') {
            this.axios.get('http://localhost:5000/loginEnv/' + sys)
                .then((response) => {
                    this.interInfo = response["data"]
                    this.method = this.interInfo["method"]
                    this.path = this.interInfo["path"]
                    this.interName = this.interInfo["interName"]
                    this.description = this.interInfo["description"]
                    var header = this.interInfo["header"]
                    var headerInitFlag = true
                    var paramInitFlag = true
                    for (var key in header) {
                        if (headerInitFlag) {
                            this.headerList = [{
                                'header': key,
                                'value': JSON.stringify(header[key])
                            }]
                            headerInitFlag = false
                        } else {
                            this.headerList.push({
                                'header': key,
                                'value': JSON.stringify(header[key])
                            })
                        }
                    }
                    var params = this.interInfo["params"]
                    for (var key in params) {
                        if (paramInitFlag) {
                            this.payloadList = [{
                                'name': key,
                                'value': JSON.stringify(params[key])
                            }]
                            paramInitFlag = false
                        } else {
                            this.payloadList.push({
                                'name': key,
                                'value': JSON.stringify(params[key])
                            })
                        }
                    }

                })
        }
    }
}
</script>

<style>

</style>
