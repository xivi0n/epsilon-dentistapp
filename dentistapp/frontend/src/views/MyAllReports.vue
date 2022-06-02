<template>
	<div class="container">
		<div class="row">
			<div class="col-12">
                <div class="row mb-2">
                    <h2>Moji izveštaji</h2>
                </div>
                <div v-if="reports.length > 0" class="col-12 reports">
                    <div class="row mx-2" :key="report.idI" v-for="report in reports">
                        <div class="col-lg-7 col-md-5 col-12 p-1">
                            <div class="p-2 cell">
                                <p class="m-auto vrsta">{{report.vrsta}}</p>
                            </div>
                        </div>
                        <div v-if="tipK == 'stomatolog'" class="col-lg-2 col-md-3 col-8 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto vrsta">{{report.matbroj}}</p>
                            </div>
                        </div>
                        <div v-if="tipK == 'pacijent'" class="col-lg-2 col-md-3 col-8 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto vrsta">{{report.ime}} {{report.prezime}}</p>
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-2 col-4 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{report.datum}}</p>
                            </div>
                        </div>
                        <div class="col-lg-1 col-md-2 col-12 p-1">
                            <router-link :to="'/moji-izvestaji/izvestaj/' + report.idI" class="router-link">
                                <button class="btn btn-primary text-center mb-2">Prikaži</button>
                            </router-link>
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
	</div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
	name: "MyAllReports",
	components: {
	},
    data() {
        return {
            reports: [],
            tipK: ""
        }
    },
    mounted() {
        document.title = "Svi moji izveštaji"
        this.tipK = localStorage.getItem("tipK")
        axios.get("http://localhost:8000/api/v1/moji-izvestaji/", {
        headers: {
            'Authorization': 'Token ' + localStorage.getItem("token")
        }}).then(response => {
            this.reports = response.data
            this.reports.forEach(e => {
                e.datum = this.formatDate(new Date(e.datum).toISOString().slice(0,10))
            });
            console.log(response.data)
        }).catch(error => {
            console.log(error)
            this.$router.push({ path: '/404' })
        })
    },
    methods: {
        formatDate(str) {
            let arr = str.split("-").reverse()
            return arr.join('.')
        }
    }
};
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

    @media screen and (max-width: 768px){
        .btn-primary {
            width: 100%;
        }
    }


</style>