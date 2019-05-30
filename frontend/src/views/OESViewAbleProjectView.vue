<template>
<div class="OESViewAbleProjectView">
    <OESViewAbleProjectList :collectionName="collectionName" />
</div>
</template>

<script>
import OESViewAbleProjectList from '@/components/OESViewAbleProjectList.vue';

export default {
    name: 'OESViewAbleProjectView',
    components: {
        OESViewAbleProjectList
    },
    data() {
        return {
            collectionName:"oesViewAbleProject",
        }
    },
}
</script>
