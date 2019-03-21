<template>
  <div class="ProjectView">
    <ProjectPage/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import ProjectPage from '@/components/ProjectPage.vue'; // @ is an alias to /src

@Component({
  components: {
    ProjectPage
  },
})
export default class ProjectView extends Vue {}
</script>
