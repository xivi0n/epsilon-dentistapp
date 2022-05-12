<template>
    <TheHeader/>
    <router-view/>
    <TheFooter/>
</template>


<script>
import TheFooter from '@/components/TheFooter.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
    name: 'App',
    components: {
        TheFooter,
        TheHeader
    }
}
</script>

<style>
    /* font-family: 'Open Sans', sans-serif; */

    * {
        margin: 0;
        padding: 0;
        font-family: 'Open Sans', sans-serif;
    }

    body {
        background: #E5E5E5;
    }

    .container {
        margin-bottom: 20px;
        margin-top: 20px;
    }

    .bright { 
        background: #ececec; 
    }

    .bright-green { 
        background: #9fd3c7; 
    }

    .bright-blue { 
        background: #385170; 
    }

    .dark-blue { 
        background: #142d4c; 
    }
</style>
