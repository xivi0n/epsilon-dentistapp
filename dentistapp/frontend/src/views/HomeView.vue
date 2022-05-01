<template>
    <TheHeader/>
	<div class="home container">
		<img alt="Vue logo" src="../assets/logo.png">
		<HelloWorld msg="Home"/>
	</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    TheHeader
  }
}
</script>
