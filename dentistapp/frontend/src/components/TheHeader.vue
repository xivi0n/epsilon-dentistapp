<template>
    <header>
        <router-link to="/" class="router-link">
            <h1 class="logo">Dentist App</h1>
        </router-link>
        <nav>
            <router-link to="/" class="router-link">Pocetna</router-link>
            <router-link to="/o-nama" class="router-link">O nama</router-link>
            <router-link to="/usluge" class="router-link">Usluge</router-link>
        </nav>
        <nav v-if="logged_in != true">
            <router-link to="/login" class="router-link">
                <button class="btn dark-blue">Login</button>
            </router-link>
            <router-link to="/registracija" class="router-link">
                <button class="btn dark-blue">Registracija</button>
            </router-link>
        </nav>
       
        
    </header>
</template>


<script>
export default {
    name: 'TheHeader',
    props: {
        logged_in: {
            type: Boolean,
            default: false
        }
    }
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
        margin: 3px;
        color : #ececec;
        text-decoration: none;
    }

</style>