<template>
    <TheHeader/>
    <div class="container">
        <h2>Usluge i cene stomatoloske ordinacije</h2>
        <div :key="service.id" v-for="service in services">
            <TheService :service="service"/>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'
import TheService from '@/components/TheService.vue'

export default {
    name: 'TheServices',
    components: {
        TheHeader,
        TheService
    },
    data() {
        return {
            services: []
        }
    },
    created() {
        this.services = [
            {
                id: 1,
                name: "Usluga stomatoloske ordinacije 1",
                price: 1234
            },
            {
                id: 2,
                name: "Usluga stomatoloske ordinacije 2",
                price: 1234
            },
            {
                id: 3,
                name: "Usluga stomatoloske ordinacije 3",
                price: 1234
            },
            {
                id: 4,
                name: "Usluga stomatoloske ordinacije 4",
                price: 1234
            }
        ]
    }
}
</script>

<style scoped>
    
</style>