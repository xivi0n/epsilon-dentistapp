<template>
	<div class="container">
		<div class="row">
			<div class="col-12">
                <div class="row mb-2">
                    <h2>Moji izveštaji</h2>
                </div>
                <div class="col-12 reports">
                    <div class="row mx-2" :key="report.id" v-for="report in reports">
                        <div class="col-lg-9 col-md-8 col-12 p-1">
                            <div class="p-2 cell">
                                {{report.vrsta}}
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-2 col-4 p-1">
                            <div class="p-2 cell text-center">
                                {{report.datum}}
                            </div>
                        </div>
                        <div class="col-lg-1 col-md-2 col-12 p-1">
                            <router-link to="/" class="router-link">
                                <button class="btn btn-primary text-center mb-2">Prikaži</button>
                            </router-link>
                        </div>
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
        }
    },
    mounted() {
        axios.get("http://localhost:8000/api/v1/moji-izvestaji/", {
        headers: {
            'Authorization': 'Token ' + localStorage.getItem("token")
        }}).then(response => {
            this.reports = response.data
            this.reports.forEach(e => {
                e.datum = new Date(e.datum).toISOString().slice(0,10);
            });
            console.log(response.data)
        }).catch(error => {
            console.log(error)
            this.$router.push({ path: '/404' })
        })

        // this.reports = [
        //                 {
        //         id: 1,
        //         title: "Naslov izvestaja",
        //         date: "12.1.2022."
        //     },
        //     {
        //         id: 2,
        //         title: "Naslov izvestaja",
        //         date: "12.1.2022."
        //     },
        //     {
        //         id: 3,
        //         title: "Naslov izvestaja",
        //         date: "12.1.2022."
        //     },
        //     {
        //         id: 4,
        //         title: "Naslov izvestaja",
        //         date: "12.1.2022."
        //     },
        //     {
        //         id: 5,
        //         title: "Naslov izvestaja",
        //         date: "12.1.2022."
        //     },
        //     {
        //         id: 6,
        //         title: "Naslov izvestaja",
        //         date: "12.1.2022."
        //     }
        // ]
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