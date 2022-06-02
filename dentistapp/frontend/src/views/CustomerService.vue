<template>
    <div class="container">
        <div class="row">
            <div v-if="tipK != 'stomatolog'" class="col-12">
                <form  class="form-size">
                    <h2>Korisnička podrška</h2>
                    <div class="form-group">
                        <label>Vrsta problema</label>
                        <select id="naslov" class="form-select mb-3 cell" aria-label="Vrsta problema">
                            <option value="Stomatološki problem" selected>Stomatološki problem</option>
                            <option value="Tehnicki problem">Tehnički problem</option>
                            <option value="Informacije">Informacije</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Email adresa</label>
                        <input id="email" type="email" class="form-control form-control-md cell" placeholder="email@something.com"/>
                    </div>
                    <div class="form-group">
                        <label>Opis problema</label>
                        <textarea id="opis" class="form-control cell" rows="4" placeholder="Opišite problem ..."></textarea>
                    </div>
                    <button v-on:click="posalji()" type="button" class="btn btn-primary w-100 my-3">Pošalji upit</button>
                </form>
            </div>
            <div v-else-if="questions.length > 0" class="col-12" >
                <div  class="row mx-2" :key="question.idP" v-for="question in questions" >
                    <div class="col-md-3 col-12 p-1">
                        <div class="cell p-2 h-100">
                            <p class="vrsta">{{question.naslov}}</p>
                        </div>
                    </div>
                    <div class="col-md-8 col-12 p-1">
                        <div class="cell p-2 h-100">
                            <p class="vrsta">{{question.opis}}</p>
                        </div>
                    </div>
                    <div class="col-md-1 col-12 p-1">
                        <button class="btn btn-primary" type="button" data-bs-toggle="collapse" :data-bs-target="'#id' + question.idP" aria-expanded="false" :aria-controls="question.idP">
                            Prikaži
                        </button>
                    </div>
                    <div class="collapse cell row p-3 drop" :id="'id' + question.idP">
                        <div class="col-md-10 col-12">
                            <textarea :id="'odgovor' + question.idP" class="form-control cell p-3" rows="6" placeholder="Napišite odgovor..."></textarea>
                        </div>
                        <div class="col-md-2 col-12">
                            <button v-on:click="odgovori(question)" class="btn btn-primary m-1" type="button">Pošalji</button>
                            <button v-on:click="otkazi(question)" class="btn btn-danger m-1" type="button">Obriši</button>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else>
                <div class="col-12 text-center my-3">
                    <h3>Nemate korisničkih pitanja!</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
    name: 'CustomerService',
    components: {
    },
    data() {
        return {
            tipK: "",
            questions: [],
            email: localStorage.getItem("email")
        }
    },
    mounted() {
        document.title = "Korisnička podrška"
        document.getElementById("email").value = this.email
        this.tipK = localStorage.getItem("tipK")
        if (this.tipK == 'stomatolog') {
            axios.get("http://localhost:8000/api/v1/pitanja/", {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                this.questions = response.data
            })
            // this.questions = [
            //     {
            //         idP: 1,
            //         naslov: "nesto neki naslov",
            //         opis: "neki opis nesto stvansf ifniaanf iasan sfnaisfu afna is a"
            //     },
            //     {
            //         idP: 2,
            //         naslov: "nesto neki naslov",
            //         opis: "neki opis nesto stvansf ifniaa\nn\n d asnod sansdnadi anis a\n adsniisa iia naisds a\n siadi sainidasui inasn\nf iasan sfnaisfu afna is a"
            //     },
            //     {
            //         idP: 3,
            //         naslov: "nesto neki naslov",
            //         opis: "neki opis nesto stvansf ifniaanf iasan sfnaisfu afna is a"
            //     },
            //     {
            //         idP: 4,
            //         naslov: "nesto neki naslov",
            //         opis: "neki opis nesto stvansf ifniaanf iasan sfnaisfu afna is a"
            //     }
            // ]
        }
    },
    methods: {
        posalji() {
            axios.post("http://localhost:8000/api/v1/novo-pitanje/", {
                naslov: document.getElementById("naslov").value,
                opis: document.getElementById("opis").value,
                email: document.getElementById("email").value
            }).then(response => {
                console.log(response)
                this.$router.go(0)
            })
        },
        odgovori(question) {
            axios.post("http://localhost:8000/api/v1/odgovori/", {
                naslov: question.naslov,
                odgovor: document.getElementById("odgovor" + question.idP).value,
                email: question.email
            }, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                console.log(response)
                this.otkazi(question)
                this.$router.go(0)
            })
        },
        otkazi(question) {
            axios.post("http://localhost:8000/api/v1/obrisi-pitanje/", {
                "idP": question.idP
            }, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                console.log(response)
                this.$router.go(0)
            })
            console.log(question)
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

    label {
        font-weight: 600;
        font-size: 20px;
        color: #05284B;
        padding: 10px;
    }

    h2 {
        text-align: center;
        font-weight: 700;
        font-size: 40px;
        color: #05284B;
    }

    input, textarea {
        color: #05284B;
    }

</style>