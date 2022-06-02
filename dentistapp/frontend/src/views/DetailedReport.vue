<template>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6">
                <div class="row">
                    <h2>Izveštaj</h2>
                </div>
                <div class="row">
                    <div class="col-12">
                        <form class="form-group mb-2" id="form1">
                            <label>Vrsta izveštaja</label>
                            <input readonly type="text" class="form-control-plaintext cell mb-3" :value="report.vrsta"/>
                            <label>Datum</label>
                            <input readonly type="text" class="form-control-plaintext cell mb-3" :value="report.datum"/>
                        </form>

                        <label>Terapija</label>
                        <div v-if="report.terapija.length > 0" class="row pt-2 cell justify-content-center">
                            <div class="row" :key="med.idL" v-for="med in report.terapija">
                                <div class="col-8">
                                    <p class="m-auto">{{med.idL.opis}}</p>
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
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-6">
                <div class="row">
                    <div class="form-group">
                        <h2>Dijagnoza</h2>
                        <textarea readonly class="form-control cell p-3 mt-4" id="exampleFormControlTextarea1" rows="10" v-model="report.dijagnoza"></textarea>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'DetailedReport',
    props: {
        idI: {
            type: Number,
        }
    },
    data() {
        return {
            report: {
                "vrsta": "",
                "dijagnoza": "",
                "datum": "",
                "terapija": []
            }
        }
    },
    mounted() {
        document.title = "Detaljan izveštaj"
        axios.get("http://localhost:8000/api/v1/moji-izvestaji/" + this.$route.params.id, {
        headers: {
            'Authorization': 'Token ' + localStorage.getItem("token")
        }}).then(response => {
            this.report = response.data
            this.report.datum = this.formatDate(new Date(this.report.datum).toISOString().slice(0,10))
            console.log(response.data)
        }).catch(error => {
            console.log(error)
            this.$router.push({ path: '/404' })
        })
        console.log(this.report)
    },
    methods: {
        formatDate(str) {
            let arr = str.split("-").reverse()
            return arr.join('.')
        },
    }
}
</script>

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

    /* a {
        color: #0583D2!important;;
    } */

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
        background: #FFFFFF;
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

</style>