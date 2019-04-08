<template>
<div class="LoginEnvView">
    <loginEnv :collectionName="collectionName" />
</div>
</template>

<script>
import loginEnv from '@/components/LoginEnv.vue';

export default {
    name: 'LoginEnvView',
    components: {
        loginEnv
    },
    data() {
        return {
            collectionName:"interLoginEnv",
        }
    },
}
</script>
