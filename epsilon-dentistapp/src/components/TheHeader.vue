<template>
    <header>
        <h1 class="logo">Dentist App</h1>
        <nav>
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
        </nav>
    </header>
</template>


<script>
export default {
    name: 'TheHeader'
}
</script>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0 20px 20px 20px;
    }

    .logo {
        float: left;
    }

    nav {
        float: right;
    }

</style>