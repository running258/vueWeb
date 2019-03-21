<template>
  <div class="LoginEnvView">
    <loginEnv/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import loginEnv from '@/components/LoginEnv.vue'; // @ is an alias to /src

@Component({
  components: {
    loginEnv
  },
})
export default class LoginEnvView extends Vue {}
</script>
