<template>
    <div class="container">
        <div class="row">
			<div class="col-12">
                <div class="row mb-2">
                    <h2>Moji zahtevi</h2>
                </div>
                <div class="col-12" v-if="tipK == 'stomatolog'">
                    <div class="row mx-2" :key="request.idZ" v-for="request in requests" >
                        <div class="col-md-7 col-12 p-1">
                            <div class="cell p-2 h-100">
                                <p class="vrsta">{{request.opis}}</p>
                            </div>
                        </div>
                        <div class="col-md-2 col-6 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{request.datumo}}</p>
                                <p class="m-auto">{{request.vremeo}}</p>
                            </div>
                        </div>
                        <div class="col-md-2 col-6 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{request.datumd}}</p>
                                <p class="m-auto">{{request.vremed}}</p>
                            </div>
                        </div>
                        <div class="col-md-1 col-12 p-1 d-flex justify-content-center align-items-center">
                            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" :data-bs-target="'#id' + request.idZ" aria-expanded="false" :aria-controls="request.idZ">
                                Prikaži
                            </button>
                        </div>
                        <div class="collapse" :id="'id' + request.idZ">
                            <div class="card card-body">
                                Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12" v-if="tipK == 'pacijent'">
                    <div class="row mx-2" :key="request.idZ" v-for="request in requests" >
                        <div class="col-md-7 col-12 p-1">
                            <div class="cell p-2 h-100">
                                <p class="vrsta">{{request.opis}}</p>
                            </div>
                        </div>
                        <div class="col-md-2 col-6 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{request.datumo}}</p>
                                <p class="m-auto">{{request.vremeo}}</p>
                            </div>
                        </div>
                        <div class="col-md-2 col-6 p-1">
                            <div class="p-2 cell text-center">
                                <p class="m-auto">{{request.datumd}}</p>
                                <p class="m-auto">{{request.vremed}}</p>
                            </div>
                        </div>
                        <div class="col-md-1 col-12 p-1 d-flex justify-content-center align-items-center">
                            <button class="btn btn-primary" type="button">Otkaži</button>
                        </div>
                    </div>
                </div>
            </div>
		</div>
    </div>
</template>

<script>
export default {
    name: 'MyAllRequests',
    components: {
    },
    data() {
        return {
            requests: [],
            tipK: 'pacijent'
        }
    },
    mounted() {
        this.tipK = localStorage.getItem('tipK')
        this.requests = [
            {
                "idZ": 1,
                "opis": "Neki opis",
                "dvod": "2022-05-21T10:10:00Z",
                "dvdo": "2022-05-21T15:16:00Z"
            },
            {
                "idZ": 2,
                "opis": "Neki opis",
                "dvod": "2022-05-21T11:10:00Z",
                "dvdo": "2022-05-21T15:13:00Z"
            },
            {
                "idZ": 3,
                "opis": "Neki opis",
                "dvod": "2022-05-21T12:10:00Z",
                "dvdo": "2022-05-21T15:13:00Z"
            },
            {
                "idZ": 4,
                "opis": "Neki opis",
                "dvod": "2022-05-21T15:10:00Z",
                "dvdo": "2022-05-21T17:13:00Z"
            },
            {
                "idZ": 5,
                "opis": "Neki opis",
                "dvod": "2022-05-21T09:10:00Z",
                "dvdo": "2022-05-21T15:13:00Z"
            },
            {
                "idZ": 6,
                "opis": "Neki opis",
                "dvod": "2022-05-21T11:10:00Z",
                "dvdo": "2022-05-21T16:13:00Z"
            }
        ]

        this.requests.forEach(e => {
            e.datumo = new Date(e.dvod).toISOString().slice(0,10);
            e.vremeo = new Date(e.dvod).toISOString().slice(11,16);
            e.datumd = new Date(e.dvdo).toISOString().slice(0,10);
            e.vremed = new Date(e.dvdo).toISOString().slice(11,16);
        });
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

    @media screen and (max-width: 768px){
        .btn-primary {
            width: 100%;
        }
    }

</style>