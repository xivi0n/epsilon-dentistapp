<template>
    <header>
        <h1 class="logo">Dentist App</h1>
        <nav>
            <router-link to="/" class="router-link">Home</router-link> |
            <router-link to="/about" class="router-link">About</router-link>
        </nav>
        <button class="btn dark-blue">Register</button>
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
        padding: 0 20px 0 20px;
        background-color: #385170;
    }

    .logo {
        float: left;
        color: #ececec;
    }

    nav {
        float: right;
    }

    .router-link {
        color : #ececec;
        text-decoration: none;
    }

</style>