<template>
    <nav class="navbar navbar-expand-md">
        <div class="container-fluid">
            <router-link to="/" class="navbar-brand px-4 mx-0">
                <img src="@/assets/logo.svg" alt="logo">
            </router-link>
            <button id="toggler" class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <i class="fa-solid fa-angle-down"></i>
            </button>
            <div class="collapse navbar-collapse header-items" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link to="/" class="nav-link router-link px-2">Početna</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/o-nama" class="nav-link router-link px-2">O nama</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/usluge" class="nav-link router-link px-2">Usluge</router-link>
                    </li>
                </ul>
                <div v-if="logged_in != true" class="">
                    <router-link to="/login" class="router-link">
                        <button type="button" class="btn btn-primary dark-blue">Login</button>
                    </router-link>
                    <router-link to="/registracija" class="router-link">
                        <button type="button" class="btn btn-primary dark-blue">Registracija</button>
                    </router-link>
                </div>
            </div>
        </div>
    </nav>
</template>


<script>
export default {
    name: 'TheHeader',
    props: {
        logged_in: {
            type: Boolean,
            default: false
        }
    },
    mounted() {
        let fa = document.createElement('script')
        fa.setAttribute('src', 'https://kit.fontawesome.com/69d212019d.js')
        fa.setAttribute('crossorigin', 'anonymous')
        document.head.appendChild(fa)

        let links = document.getElementsByClassName("router-link")
        let toggler = document.getElementById("toggler")
        console.log(links)
        for (const link of links) {
            link.onclick = function() {
                if (toggler.getAttribute("aria-expanded") == "true")
                    toggler.click()
            }
        }
    },
    methods: {
    }
}
</script>

<style scoped>
    * {
        font-style: normal;
        font-family: 'Open Sans', sans-serif;
        margin: 0;
        padding: 0;
    }

    .header-items {
        display: flex;
        justify-content: space-between;
    }

    .header-btn {
        display: flex;
        justify-content: flex-end;
        align-content: center;
        text-align: center;
        align-items: center;
    }

    .router-link {
        margin: 0px;
        padding-left: 10px;
        padding-right: 10px;
        color : #05284B;
        font-weight: 600;
        text-decoration: none;
        font-size: 18px;
        line-height: 25px;
    }

    .btn-primary, .btn:focus, .btn:active {
        background: #05284B;
        outline: none;
        box-shadow: none;
        border: none;
    }

</style>