<template>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6">
                <div class="row">
                    <h2>Napiši <a>novi</a> izveštaj</h2>
                </div>
                <div class="row">
                    <div class="col-12">
                        <form class="form-group mb-2" id="form1">
                            <label>Vrsta izveštaja</label>
                            <!-- <select id="idU" class="form-select mb-3 cell" aria-label="Default select example">
                                <option selected>Odaberi uslugu</option>
                                <option :key="service.idU" v-for="service in services" :value="service.opis">
                                    {{service.opis}}
                                </option>
                            </select> -->
                            <div class="col-12 cell">
                                <v-select placeholder="Odaberite uslugu" :options="services" label="opis" v-model="service"></v-select>
                            </div>
                        </form>

                        <form class="form-group mb-2">
                            <label>Datum</label>
                            <input id="datum" type="text" class="form-control-plaintext cell mb-3" value="report.datum"/>
                        </form>

                        <form class="form-group mb-2">
                            <label>Dodaj lek</label>
                            <div class="row px-2">
                                <div class="col-12 cell">
                                    <v-select id="mySelect" placeholder="Dodajte lek" :options="medications" label="opis" v-model="selected"></v-select>
                                </div>
                            </div>
                        </form>
                        <form class="form-group mb-2" v-if="selected">
                            <div class="row">
                                <div class="col-4 offset-2">
                                    <input id="kol" type="text" class="form-control cell" placeholder="3x 2"/>
                                </div>
                                <div class="col-6">
                                    <button type="button" v-on:click="dodaj()" class="btn btn-primary">Dodaj</button>
                                </div>
                            </div>
                        </form>

                        <form class="form-group mb-2 p-2">
                            <label>Terapija</label>
                            <div v-if="therapy.length > 0" class="row pt-2 cell justify-content-center">
                                <div class="row" :key="med.idL" v-for="med in therapy">
                                    <div class="col-8">
                                        <p class="m-auto">{{med.opis}}</p>
                                    </div>
                                    <div class="col-4">
                                        <p class="text-right m-auto">{{med.kolicina}} <i class="fa-solid fa-pen-to-square"></i></p>
                                    </div>
                                    <hr class="">
                                </div>
                            </div>
                            <div v-else class="row cell justify-content-center">
                                <div class="col-12">
                                    <p class="m-auto">Nema terapije :)</p>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-6">
                <div class="row">
                        <form class="form-group mt-5">
                            <label>JMBG</label>
                            <input id="matbroj" type="text" name="matbroj" pattern="^\s*?\d{13}(?:[-\s]\d{13})?\s*?$" class="form-control form-control-md cell" placeholder="1101001000011"/>
                        </form>
                    <div class="form-group">
                        <label>Dijagnoza</label>
                        <textarea id="dijagnoza" class="form-control cell p-3" rows="6" placeholder="Napišite dijagnozu..."></textarea>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12">
                        <button v-on:click="posalji()" type="button" class="btn btn-primary w-100 my-3">Pošalji</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import "vue-select/dist/vue-select.css"
import vSelect from "vue-select"
import { ref } from 'vue';

export default {
    name: 'NewReport',
    components: {
        vSelect,
    },
    data() {
        return {
            therapy: [],
            services: [],
            medications: [],
        }
    },
    setup() {
        const selected = ref()
        const service = ref()
        
        return {
            selected,
            service
        }
    },
    mounted() {
        this.therapy = []
        this.getServices()
        this.getMedications()
        this.getAppInfo()
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
        },
        getMedications() {
            axios.get("http://localhost:8000/api/v1/svi-lekovi/", {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                this.medications = response.data
                console.log(this.medications)
            }).catch(error => {
                console.log(error)
                this.$router.push({ path: '/404' })
            })
        },
        getAppInfo() {
            axios.get("http://localhost:8000/api/v1/pregled/" + this.$route.params.id, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                document.getElementById("datum").value = this.formatDate(response.data[0].dv.slice(0,10))
                axios.get("http://localhost:8000/api/v1/korisnik/" + response.data[0].idK, {
                headers: {
                    'Authorization': 'Token ' + localStorage.getItem("token")
                }}).then(response => {
                    document.getElementById("matbroj").value = response.data.matbroj;
                })
            })
        },
        dodaj() {
            console.log(this.selected)
            let kol = document.getElementById("kol")
            if (kol.value === "")
                alert("Unesite količinu!")
            else {
                this.therapy.push({
                    "idL": this.selected.idL,
                    "opis": this.selected.opis,
                    "kolicina": document.getElementById("kol").value
                })
                this.selected = undefined
            }
        },
        posalji() {
            if (!this.service) {
                alert("Odaberite uslugu!")
            } else {
                axios.post("http://localhost:8000/api/v1/nov-izvestaj/", {
                    "matbroj": document.getElementById("matbroj").value,
                    "vrsta": this.service.opis,
                    "terapija": this.therapy,
                    "dijagnoza": document.getElementById("dijagnoza").value,
                    "datum": new Date(this.makeISODate(document.getElementById("datum").value)).toISOString()
                }, {
                headers: {
                    'Authorization': 'Token ' + localStorage.getItem("token")
                }}).then(response => {
                    console.log(response)
                    this.otkazi(this.$route.params.id)
                }).catch(error => {
                    console.log(error)
                })
            }
        },
        formatDate(str) {
            let arr = str.split("-").reverse()
            return arr.join('.')
        },
        makeISODate(str) {
            let arr = str.replace(" ", "").split(".")
            return arr.reverse().join('-')
        },
        otkazi(idP) {
            axios.post("http://localhost:8000/api/v1/otkazi-pregled/", {
                "idP": idP
            }, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                console.log(response)
                this.$router.push({ path: '/moj-profil', replace: true })
            }).catch(error => {
                alert("Proveriti podatke!")
                console.log(error)
            })
        }
    }
}
</script>


<style>
    :root {
        --vs-border-color: transparent;
    }

</style>

<style scoped>
    .row {
        margin-top: 10px;
        margin-bottom: 10px;
    }

    h2 {
        font-weight: 600;
        font-size: 30px;
        color: #05284B;
    }

    a {
        color: #0583D2!important;;
    }

    .text-right {
        text-align: right;
    }
    
    p {
        padding: 10px;
    }

    label {
        font-weight: 400;
        color: #05284B;
        font-size: 20px;
        margin-bottom: 10px;
        margin-top: 10px;
    }

    .cell {
        /* background: #FFFFFF; */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
    }

    input {
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 15px;
        padding-right: 10px;
        text-align: left;
    }

    .form-control-plaintext {
        border: none;
        border-color: none;
        outline: none;
        color: none;
        background-color: none;
        cursor: default;
    }

    .btn-primary, .btn:focus, .btn:active {
        background: #05284B;
        border: 1px solid #05284B;
        border-radius: 10px;
    }

</style>