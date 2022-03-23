<template>
  <TheHeader :logged_in="false"/>
  <div class="about container">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="About"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'AboutView',
  components: {
    HelloWorld,
    TheHeader
  }
}
</script>