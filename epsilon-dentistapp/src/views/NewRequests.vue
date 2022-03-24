<template>
    <TheHeader/>
    <div class="container">
        <h2>Novi zahtevi za stomatologa</h2>
        <div :key="request.id" v-for="request in requests">
            <TheRequest :request="request"/>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'
import TheRequest from '@/components/TheRequest.vue'

export default {
  name: 'NewRequests',
    components: {
        TheHeader,
        TheRequest
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
                name: "Zahtev za stomatologa 1 ime",
                info: "Informacije o podnosiocu 1"
            },
            {
                id: 2,
                name: "Zahtev za stomatologa 2 ime",
                info: "Informacije o podnosiocu 2"
            },
            {
                id: 3,
                name: "Zahtev za stomatologa 3 ime",
                info: "Informacije o podnosiocu 3"
            }
            ,{
                id: 4,
                name: "Zahtev za stomatologa 4 ime",
                info: "Informacije o podnosiocu 4"
            }
        ]
    }
}
</script>

<style scoped>
    
</style>