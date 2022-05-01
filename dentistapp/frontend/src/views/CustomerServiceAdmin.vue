<template>
    <TheHeader/>
    <div class="container">
        <h2>Novi zahtevi za korisnicku podrsku</h2>
        <div :key="request.id" v-for="request in requests">
            <SupportRequest :request="request"/>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import SupportRequest from '@/components/SupportRequest.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'CustomerServiceAdmin',
  components: {
    SupportRequest,
    TheHeader
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
                name: "Zahtev za podrsku 1",
                info: "Informacije o zahtevu 1"
            },
            {
                id: 2,
                name: "Zahtev za podrsku 2",
                info: "Informacije o zahtevu 2"
            },
            {
                id: 3,
                name: "Zahtev za podrsku 3",
                info: "Informacije o zahtevu 3"
            }
            ,{
                id: 4,
                name: "Zahtev za podrsku 4",
                info: "Informacije o zahtevu 4"
            }
        ]
    }
  
}
</script>

<style scoped>
    
</style>