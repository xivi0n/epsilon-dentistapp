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
        if (localStorage.getItem("tipK") === null)
            localStorage.setItem("tipK", "")
        if (localStorage.getItem("email") === null)
            localStorage.setItem("email", "")
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

    ::-webkit-scrollbar-track {
        /* -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
        background-color: #F5F5F5;
    }

    ::-webkit-scrollbar {
        width: 12px;
        background-color: #F5F5F5;
    }

    ::-webkit-scrollbar-thumb {
        border-radius: 10px;
        /* -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3); */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        background-color: #05284B;
    }
    
    .carousel__item {
		min-height: 250px;
		font-size: 20px;
		border-radius: 4px;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.carousel__prev,
	.carousel__next {
		box-sizing: content-box;
		border: 5px solid white;
		background-color:#05284B !important;
	}

    .carousel__pagination-button--active{
        background-color:#05284B !important;
    }

    .carousel__pagination-button {
        background-color: #0583D2;
    }
</style>
