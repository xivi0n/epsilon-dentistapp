<template>
    <TheHeader/>
    <div class="registration container">
        <img alt="Vue logo" src="../assets/logo.png">
        <HelloWorld msg="New Appointment"/>
    </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'NewAppointment',
  components: {
    HelloWorld,
    TheHeader
  }
}
</script>

<style scoped>
    
</style>