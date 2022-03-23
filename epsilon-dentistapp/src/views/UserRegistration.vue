<template>
    <TheHeader/>
    <div class="registration container">
        <img alt="Vue logo" src="../assets/logo.png">
        <HelloWorld msg="Registration"/>
        <h1>bilo sta</h1>
    </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'RegistrationView',
  components: {
    HelloWorld,
    TheHeader
  }
}
</script>

<style scoped>
    
</style>