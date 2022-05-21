<template>
    <div class="container">
        <div class="row center">
            <div class="col-12 col-md-6">
                <div class="row">
                    <h2>Moj profil</h2>
                </div>
                <img class="cell" src="@/assets/pacijent-za-profil.jpg" alt="">
                <form class="form-group cell mt-2" id="form1">
                    <input readonly type="firstname" class="form-control-plaintext pt-2" :placeholder="user.ime"/>
                    <hr class="">
                    <input readonly type="lastname" class="form-control-plaintext" :placeholder="user.prezime"/>
                    <hr class="">
                    <input readonly type="email" class="form-control-plaintext" :placeholder="user.email"/>
                    <hr class="">
                    <input readonly type="text" class="form-control-plaintext pb-2" :placeholder="user.matbroj"/>
                </form>
                <button id="izmeni-btn" v-on:click="izmeni()" class="btn btn-primary w-100 my-3">Izmeni podatke</button>
            </div>
            <div class="col-12 col-md-6">
                <div class="row">
                    <h2>Moji pregledi</h2>
                </div>
                <div class="col-12 appointments" v-if="appointments.length > 0">
                    <div class="row" :key="appointment.id" v-for="appointment in appointments">
                        <div class="col-12 p-1">
                            <div class="col-12 p-2 cell">
                                {{appointment.opis}}
                            </div>
                        </div>
                        <div class="col-6 p-1">
                            <div class="col-12 p-2 cell">
                                {{appointment.datum}}
                            </div>
                        </div>
                        <div class="col-4 p-1">
                            <div class="col-12 p-2 cell">
                                {{appointment.vreme}}
                            </div>
                        </div>
                        <div class="col-2 p-1">
                            <div class="col-12 p-2 cell">
                                {{appointment.trajanje}}
                            </div>
                        </div>
                        <div class="col-12">
                            <router-link to="/" class="router-link">
                                <button class="btn btn-primary btn-sm w-100 mb-2">Otkaži</button>
                            </router-link>
                        </div>
                    </div>
                </div>
                <div v-else class="my-3">
                    <h3>Nemate zakazanih pregleda!</h3>
                    <h4>Proverite zahteve <router-link to="/moji-zahtevi" class="router-link">ovde</router-link></h4>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
// @ is an alias to /src
import axios from 'axios'

export default {
    name: 'MyProfile',
    components: {
    },
    data() {
        return {
            user: {
                logged_in: false,
                displayName: ""
            },
            appointments: [],
        }
    },
    mounted() {
        axios.get("http://localhost:8000/api/v1/moj-profil/", {
        headers: {
            'Authorization': 'Token ' + localStorage.getItem("token")
        }}).then(response => {
            this.user = response.data
        }).catch(error => {
            console.log(error)
            this.$router.push({ path: '/404' })
        })

        this.appointments = [
            {
                "idP": 1,
                "opis": "Neki pregled",
                "dv": "2022-05-21T15:18:05Z",
                "trajanje": 30
            },
            {
                "idP": 2,
                "opis": "Neki pregled",
                "dv": "2022-05-21T15:18:05Z",
                "trajanje": 30
            },
            {
                "idP": 3,
                "opis": "Neki pregled",
                "dv": "2022-05-21T15:18:05Z",
                "trajanje": 30
            },
            {
                "idP": 4,
                "opis": "Neki pregled",
                "dv": "2022-05-21T15:18:05Z",
                "trajanje": 30
            },
            {
                "idP": 5,
                "opis": "Neki pregled",
                "dv": "2022-05-21T15:18:05Z",
                "trajanje": 30
            },
            {
                "idP": 6,
                "opis": "Neki pregled",
                "dv": "2022-05-21T15:18:05Z",
                "trajanje": 30
            }
        ]

        this.appointments.forEach(e => {
            e.datum = new Date(e.dv).toISOString().slice(0,10);
            e.vreme = new Date(e.dv).toISOString().slice(11,16);
        });
        let inputs = document.getElementById("form1").elements
        for (const el of inputs) {
            el.style.fontWeight = "600"
        }
    },
    methods: {
        izmeni() {
            let btn = document.getElementById("izmeni-btn")
            let inputs = document.getElementById("form1").elements
            console.log(inputs)
            for (const el of inputs) {
                if (el.hasAttribute("readonly") && el.type != "email") {
                    el.style.fontWeight = "400"
                    el.toggleAttribute("readonly")
                }
            }
            if (btn.textContent === "Potvrdi") {
                var ime = inputs[0].value
                if (ime === "")
                    ime = inputs[0].getAttribute("placeholder")
                else {
                    inputs[0].value = ""
                    inputs[0].setAttribute("placeholder", ime)
                }

                var prezime = inputs[1].value
                if (prezime === "")
                    prezime = inputs[1].getAttribute("placeholder")
                else {
                    inputs[1].value = ""
                    inputs[1].setAttribute("placeholder", prezime)
                }
                var matbroj = inputs[3].value
                if (matbroj === "")
                    matbroj = inputs[3].getAttribute("placeholder")
                else {
                    inputs[3].value = ""
                    inputs[3].setAttribute("placeholder", matbroj)
                }

                axios.put("http://localhost:8000/api/v1/moj-profil/", {
                    "ime": ime,
                    "email": inputs[2].getAttribute("placeholder"),
                    "prezime": prezime,
                    "matbroj": matbroj
                }, {
                headers: {
                    'Authorization': 'Token ' + localStorage.getItem("token")
                }}).then(response => {
                    btn.textContent = "Izmeni podatke"
                    for (const el of inputs) {
                        if (!el.hasAttribute("readonly")) {
                            el.style.fontWeight = "600"
                            el.toggleAttribute("readonly")
                        }
                    }

                    let user = {
                        "displayName": ime + " " + prezime,
                        "logged_in": true
                    }
                    localStorage.setItem("displayName", user.displayName)
                    localStorage.setItem("logged_in", user.logged_in)
                    this.emitter.emit("login-changed", user)

                    console.log(response)
                }).catch(error => {
                    alert("Proveriti podatke!")
                    console.log(error)
                })
            } else {
                btn.textContent = "Potvrdi"
            }
        }
    }
}
</script>

<style scoped>
    hr {
        margin-top: 5px;
        margin-bottom: 5px;
        border-color: #05284B;
        background: #05284B;
        height: 3px;
    }

    .appointments {
        overflow-x: hidden;
        overflow-y: scroll;
        padding: 30px;
        max-height: 500px;
        position: relative;
    }

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
    
    img {
        max-height: 300px;
    }

    .cell {
        background: #FFFFFF;
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
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

    .form-control-plaintext {
        border: none;
        border-color: none;
        outline: none;
        color: none;
        background-color: none;
        cursor: default;
    }

    .router-link {
        text-decoration: none;
    }

    ::-webkit-scrollbar-track {
        /* -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
        background-color: #F5F5F5;
    }

    ::-webkit-scrollbar {
        width: 12px;
        background-color: #F5F5F5;
    }

    ::-webkit-scrollbar-thumb {
        border-radius: 10px;
        /* -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3); */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
        background-color: #05284B;
    }

</style>