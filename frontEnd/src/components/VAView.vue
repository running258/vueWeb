<template>
    <div id="VAView">
    {{this.$route.params}}
        
    </div>
</template>

<script>
    export default {
        data(){
            return{
                
            }
        },
        created() {
            this.axios.get("http://localhost:5000/getVA/"+this.$route.params.VAName)
            .then((res)=>{
                console.log(res)
            })
        },
    }
</script>

