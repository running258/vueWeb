<template>
<div>
    <p>{{ msg }}</p>
</div>
</template>

<script>
export default {
    name: 'Ping',
    data() {
        return {
            msg: 'Hello!',
        };
    },
    mounted() {
        this.axios.get('http://localhost:5000/ping', {
                "aa": 'bb'
            })
            .then((response) => {
                console.log(response)
                console.log(response.data.main)
                this.msg = response
            })
    }
}
</script>
