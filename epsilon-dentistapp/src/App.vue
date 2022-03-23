<template>
  <TheHeader/>
  <div class="container">
    <router-view/>
  </div>
  <TheFooter/>
</template>


<script>
import TheFooter from '@/components/TheFooter.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'App',
  components: {
    TheHeader,
    TheFooter
  }
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  .container {
    max-width: 1000px;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    /* border: 1px solid steelblue; */
    padding: 30px;
    border-radius: 5px;
    align-items: center;
    text-align: center;
  }


  body {
    font-family: 'Poppins', sans-serif;
  }

  .btn {
    display: inline-block;
    background: #000;
    color: #fff;
    border: none;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 15px;
    font-family: inherit;
  }

  .btn:focus {
    outline: none;
  }

  .btn:active {
    transform: scale(0.98);
  }

  .btn-block {
    display: block;
    width: 100%;
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
