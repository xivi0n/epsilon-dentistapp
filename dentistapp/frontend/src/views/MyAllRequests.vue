<template>
    <div class="container">
        <div class="row">
			<div class="col-12">
                <div class="row mb-2">
                    <h2>Moji zahtevi</h2>
                </div>
                <div class="col-12" v-if="tipK == 'stomatolog' && requests.length > 0">
                    <div class="row mx-2" :key="request.idZ" v-for="request in requests" >
                        <div class="col-md-7 col-12 p-1">
                            <div class="cell p-2 h-100">
                                <p class="vrsta">{{request.opis}}</p>
                            </div>
                        </div>
                        <div class="col-md-2 col-6 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{request.datum}}</p>
                                <p class="m-auto">{{request.vremeo}}</p>
                            </div>
                        </div>
                        <div class="col-md-2 col-6 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{request.datum}}</p>
                                <p class="m-auto">{{request.vremed}}</p>
                            </div>
                        </div>
                        <div class="col-md-1 col-12 p-1">
                            <button v-on:click="ucitaj(request)" class="btn btn-primary" type="button" data-bs-toggle="collapse" :data-bs-target="'#id' + request.idZ" aria-expanded="false" :aria-controls="request.idZ">
                                Prikaži
                            </button>
                        </div>
                        <div class="collapse cell row p-3 drop" :id="'id' + request.idZ">
                            <div class="col-md-4 offset-md-1 col-12">
                                <h4 class="m-auto mb-3">{{request.datum}}</h4>
                                <div class="row" :key="appo.idP" v-for="appo in request.zauzetiTermini" >
                                    <div class="col-6 text-center">
                                        <p class="m-auto">{{appo.vremeo}} - {{appo.vremed}}</p>
                                    </div>
                                    <div class="col-6 text-center">
                                        <p class="m-auto">{{appo.trajanje}} minuta <i class="fa-regular fa-clock"></i></p>
                                    </div>
                                    <hr class="">
                                </div>
                                <div class="row" v-if="request.zauzetiTermini && request.zauzetiTermini.length == 0">
                                    <div class="col-12 text-center my-3">
                                        <h6>Nemate zakazanih pregleda!</h6>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-4 offset-md-1">
                                <form class="form-group mb-2">
                                    <label>Vreme</label>
                                    <Datepicker v-model="time1" :startTime="minTime" :minTime="minTime" :maxTime="maxTime" minutesIncrement="15" timePicker noMinutesOverlay utc ></Datepicker>
                                </form>
                                <form class="form-group mb-2">
                                    <label>Trajanje</label>
                                    <Datepicker autoApply v-model="time2" :startTime="time2" minutesIncrement="15" timePicker noMinutesOverlay utc ></Datepicker>
                                </form>
                            </div>
                            <div class="col-md-2 col-12">
                                <button v-on:click="sacuvaj(request)" class="btn btn-primary m-1" type="button">Potvrdi</button>
                                <button v-on:click="otkazi(request.idZ)" class="btn btn-danger m-1" type="button">Obriši</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12" v-if="tipK == 'pacijent' && requests.length > 0">
                    <div class="row mx-2" :key="request.idZ" v-for="request in requests" >
                        <div class="col-md-7 col-12 p-1">
                            <div class="cell p-2 h-100">
                                <p class="vrsta">{{request.opis}}</p>
                            </div>
                        </div>
                        <div class="col-md-2 col-6 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{request.datum}}</p>
                                <p class="m-auto">{{request.vremeo}}</p>
                            </div>
                        </div>
                        <div class="col-md-2 col-6 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{request.datum}}</p>
                                <p class="m-auto">{{request.vremed}}</p>
                            </div>
                        </div>
                        <div class="col-md-1 col-12 p-1">
                            <button v-on:click="otkazi(request.idZ)" class="btn btn-danger" type="button">Otkaži</button>
                        </div>
                    </div>
                </div>
                <div v-if="requests.length == 0">
                    <div class="col-12 text-center my-3">
                        <h3>Nemate novih zahteva!</h3>
                    </div>
                </div>
            </div>
		</div>
    </div>
</template>

<script>
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import { ref } from 'vue';
import axios from 'axios';

export default {
    name: 'MyAllRequests',
    components: {
        Datepicker,
    },
    data() {
        return {
            requests: [],
            tipK: 'pacijent'
        }
    },
    setup() {
        const date = ref();
        const time1 = ref({ hours: 0, minutes: 0 });
        const time2 = ref({ hours: 0, minutes: 0 });
        const minTime = ref({ hours: 0, minutes: 0 });
        const maxTime = ref({ hours: 0, minutes: 0 });
        
        return {
            date,
            time1,
            time2,
            minTime,
            maxTime
        }
    },
    mounted() {
        document.title = "Svi moji zahtevi"
        this.tipK = localStorage.getItem('tipK')
        axios.get("http://localhost:8000/api/v1/moji-zahtevi/", {
        headers: {
            'Authorization': 'Token ' + localStorage.getItem("token")
        }}).then(response => {
            console.log(response)
            this.requests = response.data
            this.requests.forEach(e => {
                e.datum = this.formatDate(new Date(e.dvod).toISOString().slice(0,10))
                e.vremeo = new Date(e.dvod).toISOString().slice(11,16)
                e.vremed = new Date(e.dvdo).toISOString().slice(11,16)
            });
        })
    },
    methods: {
        otkazi(idZ) {
            axios.post("http://localhost:8000/api/v1/obrisi-zahtev/", {
                "idZ": idZ
            }, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                console.log(response)
                this.$router.go(0)   
            }).catch(error => {
                alert("Proveriti podatke!")
                console.log(error)
            })
        },
        sacuvaj(request) {
            console.log(request)
            let dv = new Date(request.dvod);
            dv.setUTCHours(this.time1.hours, this.time1.minutes, 0, 0)
            let trajanje = 60 * this.time2.hours + this.time2.minutes
            axios.post("http://localhost:8000/api/v1/zakazi-pregled/", {
                "idK": request.idK,
                "opis": request.opis,
                "dv": dv.toISOString(),
                "trajanje": trajanje
            }, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                this.otkazi(request.idZ)
                console.log(response)
            }).catch(error => {
                alert("Proveriti podatke!")
                console.log(error)
            })
        },
        ucitaj(request) {
            console.log(request)
            this.time1 = this.makeTime(request.vremeo)
            this.minTime = this.time1
            this.maxTime = this.makeTime(request.vremed)
            axios.get("http://localhost:8000/api/v1/zauzeti-termini/", {
            params: {
                "datum": request.dvod
            },
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                console.log(response)
                request.zauzetiTermini = response.data
                request.zauzetiTermini.forEach(e => {
                    let date = new Date(e.dv);
                    e.vremeo = date.toISOString().slice(11,16)
                    e.vremed = new Date(date.getTime() + parseInt(e.trajanje)*60000).toISOString().slice(11,16)
                })
            })
        },
        formatDate(str) {
            let arr = str.split("-").reverse()
            return arr.join('.')
        },
        makeTime(str) {
            let arr = str.split(":")
            return ref({ "hours": parseInt(arr[0]), "minutes": parseInt(arr[1])})
        }
    }

}
</script>

<style scoped>
    .cell {
        background: #FFFFFF;
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
    }

    h2 {
        text-align: center;
        font-weight: 700;
        font-size: 40px;
        color: #05284B;
    }

    p {
        font-weight: 400;
        color: #05284B;
    }

    p.vrsta {
        padding-left: 10px;
        padding-top: 10px;
    }

    .btn-primary, .btn:focus, .btn:active {
        background: #05284B;
        border: 1px solid #05284B;
        border-radius: 10px;
    }

    @media screen and (min-width: 1100px) {
        .container {
            max-width: 85%;
            margin: auto;
        }
    }

    h4 {
        font-weight: 600;
        font-size: 20px;
        color: #05284B;
        padding: 10px;
        text-align: center;
    }

    @media screen and (max-width: 800px) {
        .drop {
            width: 100%;
        }
    }

    @media screen and (min-width: 800px) {
        .drop {
            width: 80%;
        }
    }

    .btn-danger {
        border-radius: 10px;
    }

</style>