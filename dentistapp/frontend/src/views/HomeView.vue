<template>
	<div class="container">
		<div class="row">
			<div class="col-12">
				<img alt="Vue logo" src="../assets/logo.png" />
				<HelloWorld msg="Home" />
			</div>
		</div>
	</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
	name: "HomeView",
	components: {
		HelloWorld,
	},
};
</script>
