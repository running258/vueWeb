<template>
    <div id="VAView">
    {{VAResponse}}
        
    </div>
</template>

<script>
    export default {
        data(){
            return{
                VAResponse:''
            }
        },
        created() {
            this.axios.get("http://localhost:5000/getVA/"+this.$route.params.VAName)
            .then((res)=>{
                this.VAResponse = res["data"]
            })
        },
    }
</script>

