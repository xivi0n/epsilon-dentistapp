<template>
    <div id="page-wrapper">
        <TheHeader :logged_in=logged_in :displayName=displayName />
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
            logged_in: false,
            displayName: ""
        }
    },
    created() {
        this.logged_in = true
        this.displayName = "Mihailo Jovanovic"
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
