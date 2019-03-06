<template>
<div id="app">
    <router-view></router-view>
</div>
</template>

<script>
export default {
    name: 'app',
    data() {
        return {}
    },
    methods: {
        aaaaa() {
            axios.get("http://127.0.0.1:5000").then(function (r) {
                alert(r.data)
            });
        }

    }
}
</script>

<style lang="scss">
 
</style>
