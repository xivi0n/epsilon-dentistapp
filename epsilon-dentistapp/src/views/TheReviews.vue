<template>
    <TheHeader/>
    <div class="container">
        <h2>Iskustva i ocene</h2>
        <div :key="review.id" v-for="review in reviews">
            <TheReview :review="review"/>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import TheReview from '@/components/TheReview.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
    name: 'TheReviews',
    components: {
        TheHeader,
        TheReview
    },
    data() {
        return {
            reviews: []
        }
    },
    created() {
        this.reviews = [
            {
                id: 1,
                name: "Ime i prezime 1",
                info: "Opis 1",
                num: 4
            },
            {
                id: 2,
                name: "Ime i prezime 2",
                info: "Opis 2",
                num: 3
            },
            {
                id: 3,
                name: "Ime i prezime 3",
                info: "Opis 3",
                num: 1
            },
            {
                id: 4,
                name: "Ime i prezime 4",
                info: "Opis 4",
                num: 5
            }
        ]
    }
}
</script>

<style scoped>
    
</style>