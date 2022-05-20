<template>
    <div class="container">
        <div class="row justify-content-center align-items-center text-center my-5">
            <h1 class="my-2">Error 404</h1>
            <h2>Izgleda da ste zalutali, vratite se na početnu stranicu <router-link to="/" class="">ovde</router-link></h2>
        </div>
    </div>
</template>

<script>
export default {
    name: 'The404Error',
}
</script>

<style scoped>

    * {
        color: #05284B;
    }

    h1 {
        font-size: 40px;
        font-weight: 600;
    }

    h2 {
        font-size: 25px;
        font-weight: 400;
    }

</style>