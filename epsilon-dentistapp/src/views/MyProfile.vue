<template>
    <TheHeader/>
    <div class="registration container">
        <img alt="Vue logo" src="../assets/logo.png">
        <HelloWorld msg="MyProfile"/>
    </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'MyProfile',
  components: {
    HelloWorld,
    TheHeader
  }
}
</script>

<style scoped>
    
</style>