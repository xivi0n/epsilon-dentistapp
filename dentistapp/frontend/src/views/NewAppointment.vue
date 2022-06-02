<template>
    <div class="container">
        <div class="row">
            <h2>Posašaljite zahtev za pregled</h2>
            <div class="col-md-6 col-12">
                <form class="form-group mb-2" id="form1">
                    <label>Izaberite stomatologa</label>
                    <select id="idS" class="form-select mb-3 cell" aria-label="Default select example">
                        <option value="1" selected>Bilo koji stomatolog</option>
                        <option :key="stomatolog.idK" v-for="stomatolog in stomatolozi" :value="stomatolog.idK">
                            {{stomatolog.ime + ' ' + stomatolog.prezime}}
                        </option>
                    </select>
                </form>
                <form class="form-group mb-2">
                    <label>Datum</label>
                    <div class="cell">
                        <Datepicker autoApply v-model="date" :enableTimePicker="false" utc ></Datepicker>
                    </div>
                </form>
                <form class="form-group mb-2">
                    <label>Slobodan sam od</label>
                    <div class="cell">
                        <Datepicker autoApply v-model="time1" :startTime="time1" minutesIncrement="15" timePicker noMinutesOverlay utc ></Datepicker>
                    </div>
                </form>
                <form class="form-group mb-2">
                    <label>do</label>
                    <div class="cell">
                        <Datepicker autoApply v-model="time2" :startTime="time2" minutesIncrement="15" timePicker noMinutesOverlay utc ></Datepicker>
                    </div>
                </form>
            </div>
            <div class="col-md-6 col-12">
                <div class="row">
                    <div class="form-group">
                        <!-- <label></label> -->
                        <textarea class="form-control cell p-3 mt-4" id="textArea" rows="10" placeholder="Opišite problem ..."></textarea>
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
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import { ref } from 'vue';
import axios from 'axios';

export default {
    name: 'NewAppointment',
    components: {
        Datepicker,
    },
    data() {
        return {
            stomatolozi: [],
        }
    },
    setup() {
        const date = ref(Date());
        const time1 = ref({ hours: 0, minutes: 0 });
        const time2 = ref({ hours: 0, minutes: 0 });
        
        return {
            date,
            time1,
            time2
        }
    },
    mounted() {
        document.title = "Zakažite pregled"
        axios.get("http://localhost:8000/api/v1/lista-stomatologa/", {
        headers: {
            'Authorization': 'Token ' + localStorage.getItem("token")
        }}).then(response => {
            this.stomatolozi = response.data
        }).catch(error => {
            console.log(error)
            this.$router.push("/404")
        })
    },
    methods: {
        posalji() {
            let e = document.getElementById("idS");
            let dvod = new Date(this.date);
            dvod.setUTCHours(this.time1.hours, this.time1.minutes, 0, 0)
            let dvdo = new Date(this.date);
            dvdo.setUTCHours(this.time2.hours, this.time2.minutes, 0, 0)

            axios.post("http://localhost:8000/api/v1/slanje-zahteva/", {
                "idS": e.options[e.selectedIndex].value,
                "dvod": dvod.toISOString(),
                "dvdo": dvdo.toISOString(),
                "opis": document.getElementById("textArea").value
            }, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem("token")
            }}).then(response => {
                this.$router.go(0)
                console.log(response)
            }).catch(error => {
                alert("Proveriti podatke!")
                console.log(error)
            })   
        }
    }
}
</script>

<style scoped>
    .center {
		width: 100%;
		padding-left: 10px;
		padding-right: 10px;
        background: transparent;
		text-align: center;
		display: flex;
		justify-content: center;
	}

    @media screen and (min-width: 950px) {
        .container {
            max-width: 85%;
            margin: auto;
        }
    }

    @media screen and (min-width: 1100px) {
        .container {
            max-width: 65%;
            margin: auto;
        }
        /* .btn-primary {
            width: 50%;
        } */
    }

    .cell {
        /* background: #FFFFFF; */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
    }

    .btn-primary, .btn:focus, .btn:active {
        background: #05284B;
        border: 1px solid #05284B;
        border-radius: 10px;
    }

    input {
        padding-top: 0px;
        padding-bottom: 0px;
        padding-left: 10px;
        padding-right: 10px;
        text-align: left;
    }

    h2 {
        text-align: center;
        font-weight: 700;
        font-size: 40px;
        color: #05284B;
    }

    label {
        font-weight: 600;
        color: #05284B;
        font-size: 20px;
        margin-bottom: 10px;
        margin-top: 10px;
    }
    
</style>