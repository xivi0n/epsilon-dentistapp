<template>
    <div class="container">
        <div class="row text-center">
            <h2>Usluge i cene stomatoloske ordinacije</h2>
        </div>
        <div class="row service-row" :key="service.idU" v-for="service in services">
            <TheService :service="service"/>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import TheService from '@/components/TheService.vue'
import axios from 'axios'

export default {
    name: 'TheServices',
    components: {
        TheService
    },
    data() {
        return {
            services: []
        }
    },
    mounted() {
        document.title = "Naše usluge"
        this.getServices()
        // this.services = [
        //     {
        //         idU: 1,
        //         opis: "Usluga stomatoloske ordinacije 1",
        //         cena: 1234
        //     },
        //     {
        //         idU: 2,
        //         opis: "Usluga stomatoloske ordinacije 2",
        //         cena: 1234
        //     },
        //     {
        //         idU: 3,
        //         opis: "Usluga stomatoloske ordinacije 3",
        //         cena: 1234
        //     },
        //     {
        //         idU: 4,
        //         opis: "Usluga stomatoloske ordinacije 4",
        //         cena: 1234
        //     }
        // ]
    },
    methods: {
        getServices() {
            axios.get('http://localhost:8000/api/v1/sve-usluge/')
            .then(response => {
                this.services = response.data
                this.services.forEach(e => {
                    e.cena = Math.trunc(e.cena)
                })
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
    .service-row {
        width: 80%;
        display: flex;
        justify-content: center;
        margin: 0 auto;
    }

    h2 {
        margin-bottom: 20px;
		font-weight: 700;
		font-size: 40px;
        color: #05284B;
    }

</style>