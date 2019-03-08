<template>
<div id="projectDetails">

    {{interInfo}}

    <div style="margin-top: 15px;">
        <!-- <el-input placeholder="请输入接口地址" v-model="url" class="input-with-select" > -->
        <el-select v-model="method" slot="prepend" placeholder="请选择">
            <el-option label="GET" value="GET"></el-option>
            <el-option label="POST" value="POST"></el-option>
            <el-option label="PUT" value="PUT"></el-option>
        </el-select>
        <!-- </el-input> -->
    </div>
    <div>
        <el-row v-for="(header, index) in headerList" :key="index">
            <el-input placeholder="header" class="headerParams" v-model="header.header"></el-input>
            <el-input placeholder="value" class="headerValues" v-model="header.value"></el-input>
            <i class="el-icon-circle-plus" @click="addHeader()"></i>
            <i class="el-icon-remove" @click="removeHeader(index)" v-if="headerLength!=0"></i>
        </el-row>
    </div>

    <div v-if="method!='GET' && method!=''">
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="payload" name="payload">payload</el-tab-pane>
            <el-tab-pane label="raw" name="raw">raw</el-tab-pane>
        </el-tabs>
        <div v-if="activeName=='payload'">
            <el-row v-for="(payload, index) in payloadList" :key="index">
                <el-input placeholder="name" class="payloadName" v-model="payload.name"></el-input>
                <el-input placeholder="value" class="payloadValues" v-model="payload.value"></el-input>
                <i class="el-icon-circle-plus" @click="addPayload()"></i>
                <i class="el-icon-remove" @click="removePayload(index)" v-if="payLoadLength!=0"></i>
            </el-row>
        </div>
        <div v-if="activeName=='raw'">
            <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="请输入内容" v-model="rawarea">
            </el-input>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            interInfo:[],
            interName:'',
            description:'',
            activeName: 'payload',
            path: '',
            method: '',
            headerList: [{
                'header': '',
                'value': '',
            }],
            headerLength: 0,
            payloadList: [{ 
                'name': '',
                'value': ''
            }],
            payLoadLength: 0,
            rawarea: ''
        };
    },
    methods: {
        addHeader() {
            this.headerLength++
            this.headerList.push({
                'header': '',
                'value': '',
            });
        },
        removeHeader(index) {
            this.headerLength--
            this.headerList.splice(index, 1)
        },
        addPayload() {
            this.payLoadLength++
            this.payloadList.push({
                'name': '',
                'value': '',
            });
        },
        removePayload(index) {
            this.payLoadLength--
            this.payloadList.splice(index, 1)
        },
        handleClick(tab, event) {}

    },
    created() {
        var interName = this.$route.params.interName
        if (interName!='') {
            this.axios.get('http://localhost:5000/interInfo/'+interName)
            .then((response) => {
                this.interInfo = response["data"]
                this.method = this.interInfo["method"]
                this.path = this.interInfo["path"]
                this.interName = this.interInfo["interName"]
                this.description = this.interInfo["description"]
                var header = this.interInfo["header"]
                for (var key in header) {
                    if (this.headerLength==0) {
                        this.headerList = [{'header':key,'value':header[key]}]
                    }
                    else{
                        this.headerList.push({'header':key,'value':header[key]})
                    }
                    this.headerLength++
                }
                var params = this.interInfo["params"]
                for (var key in params) {
                    if (this.payLoadLength==0) {
                        this.payloadList = [{'name':key,'value':header[key]}]
                    }
                    else{
                        this.payloadList.push({'name':key,'value':params[key]})
                    }
                    this.payLoadLength++
                }

            })
        } else {
            console.log("**********null")
        }
    },
    mounted() {}
};
</script>

<style>
.headerParams {
    width: 400px;
}

.headerValues {
    width: 400px;
}

.payloadName {
    width: 400px;
}

.payloadValues {
    width: 400px;
}
</style>
