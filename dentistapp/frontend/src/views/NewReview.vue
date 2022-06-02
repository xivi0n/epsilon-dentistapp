<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <form class="form-size">
                    <h2>Ocenite nas</h2>
                    <div class="form-group pb-2">
                        <label class="">Unesite ocenu</label>
                        <vue3starRatings class="m-0 p-0" v-on:click="update()" :key="componentKey" v-model="rating" :showControl="false"/>
                    </div>
                    <div class="form-group">
                        <label>Opišite Vaše iskustvo</label>
                        <textarea id="opis" class="form-control cell" rows="5" placeholder="Dodajte komentar ..."></textarea>
                    </div>
                    <button v-on:click="posalji()" type="button" class="btn btn-primary w-100 my-3">Dodaj ocenu</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import vue3starRatings from "vue3-star-ratings"
import axios from 'axios'

export default {
    name: "NewReview",
	components: {
		vue3starRatings,
	},
    data() {
        return {
            rating: 3,
            componentKey: 0
        }
    },
    methods: {
        update() {
            this.rating = Math.trunc(this.rating) + 1
            this.componentKey += 1;
        },
        posalji() {
            axios.post("http://localhost:8000/api/v1/nova-ocena/", {
                "opis": document.getElementById("opis").value,
                "ocena": this.rating
            }, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                console.log(response)
                this.$router.push({ path: '/', replace: true })
            }).catch(error => {
                alert("Proveriti podatke!")
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
    .btn-primary, .btn:focus, .btn:active {
        background: #05284B;
        border: 1px solid #05284B;
        border-radius: 10px;
    }

    .cell {
        /* background: #FFFFFF; */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
    }

    @media screen and (min-width: 1000px) {
        .form-size {
            max-width: 40%;
            margin: auto;
        }   
    }

    @media screen and (max-width: 1000px) {
        .form-size {
            max-width: 50%;
            margin: auto;
        }   
    }

    @media screen and (max-width: 768px) {
        .form-size {
            max-width: 100%;
            margin: auto;
        }   
    }

    label {
        font-weight: 600;
        font-size: 20px;
        color: #05284B;
        padding: 10px;
    }

    h2 {
        text-align: center;
        font-weight: 600;
        font-size: 40px;
        color: #05284B;
    }

    input, textarea {
        color: #05284B;
    }
</style>
