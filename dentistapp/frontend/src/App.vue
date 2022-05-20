<template>
    <div id="page-wrapper">
        <TheHeader/>
        <router-view/>
        <TheFooter/>
    </div>  
</template>


<script>
import TheFooter from '@/components/TheFooter.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
    name: 'App',
    components: {
        TheFooter,
        TheHeader
    },
    data() {
        return {
        }
    },
    mounted() {
        if (localStorage.getItem("token") === null)
            localStorage.setItem("token", "")
        if (localStorage.getItem("displayName") === null)
            localStorage.setItem("displayName", "")
        if (localStorage.getItem("logged_in") === null)
            localStorage.setItem("logged_in", false)
    }
}
</script>

<style>
    /* font-family: 'Open Sans', sans-serif; */

    * {
        /* margin: 0;
        padding: 0; */
        font-family: 'Open Sans', sans-serif;
    }

    #page-wrapper {
        position: relative;
        min-height: 100vh;
    }

    body {
        background: #E5E5E5;
    }

    .container {
        display: flex;
        flex-direction: column;
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
