<template>
    <TheHeader/>
    <div class="container bright">
        <h2>Zakazani pregledi</h2>
        <div :key="request.id" v-for="request in requests">
            <AppointmentRequest :request="request"/>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'
import AppointmentRequest from '@/components/AppointmentRequest.vue'

export default {
  name: 'NewRequests',
    components: {
        TheHeader,
        AppointmentRequest
    },
    data(){
        return {
            requests: []
        }
    },
    created(){
        this.requests = [
            {
                id: 1,
                name: "Pregled 1",
                info: "Informacije o podnosiocu 1",
                date: "DD/MM/YYYY",
                time: "HH:MM"
            },
            {
                id: 2,
                name: "Pregled 2",
                info: "Informacije o podnosiocu 2",
                date: "DD/MM/YYYY",
                time: "HH:MM"
            },
            {
                id: 3,
                name: "Pregled 3",
                info: "Informacije o podnosiocu 3",
                date: "DD/MM/YYYY",
                time: "HH:MM"
            }
            ,{
                id: 4,
                name: "Pregled 4",
                info: "Informacije o podnosiocu 4",
                date: "DD/MM/YYYY",
                time: "HH:MM"
            }
        ]
    }
}
</script>

<style scoped>
    
</style>