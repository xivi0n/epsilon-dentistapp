<template>
	<div class="container">
		<div class="row">
			<div class="col-12">
				<HelloWorld msg="Home" />
				<img alt="Vue logo" src="../assets/logo.svg" />
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
