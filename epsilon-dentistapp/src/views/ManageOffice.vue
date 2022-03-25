<template>
    <TheHeader/>
    <div class="container bright">
        <h2>Uredi usluge</h2>
        <div :key="service.id" v-for="service in services">
            <ManageService :service="service"/>
        </div>
        <button class="btn">Dodaj uslugu</button>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'
import ManageService from '@/components/ManageService.vue'

export default {
  name: 'ManageOffice',
    components: {
        TheHeader,
        ManageService
    },
    data(){
        return {
            services: []
        }
    },
    created(){
        this.services = [
            {
                id: 1,
                name: "Usluga 1",
                info: 1234
            },
            {
                id: 2,
                name: "Usluga 2",
                info: 1234
            },
            {
                id: 3,
                name: "Usluga 3",
                info: 1234
            }
            ,{
                id: 4,
                name: "Usluga 4",
                info: 1234
            }
        ]
    }
}
</script>

<style scoped>
    
</style>