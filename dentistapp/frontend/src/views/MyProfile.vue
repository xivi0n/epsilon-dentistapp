<template>
    <div class="container">
        <div class="row center">
            <div class="col-12 col-md-6">
                <div class="row">
                    <h2>Moj profil</h2>
                </div>
                <img class="cell" src="@/assets/pacijent-za-profil.jpg" alt="">
                <div class="form-group cell mt-2">
                    <input readonly type="firstname" class="form-control-plaintext pt-2" :placeholder="user.ime"/>
                    <hr class="">
                    <input readonly type="lastname" class="form-control-plaintext" :placeholder="user.prezime"/>
                    <hr class="">
                    <input readonly type="email" class="form-control-plaintext" :placeholder="user.email"/>
                    <hr class="">
                    <input readonly type="text" class="form-control-plaintext pb-2" :placeholder="user.matbroj"/>
                </div>
                <button class="btn btn-primary w-100 my-3">Izmeni podatke</button>
            </div>
            <div class="col-12 col-md-6">
                <div class="row">
                    <h2>Moji pregledi</h2>
                </div>
                <div class="col-12 appointments">
                    <div class="row" :key="appointment.id" v-for="appointment in appointments">
                        <div class="col-lg-8 col-12 p-1">
                            <div class="col-12 p-2 cell">
                                {{appointment.title}}
                            </div>
                        </div>
                        <div class="col-lg-4 col-6 p-1">
                            <div class="col-12 p-2 cell">
                                {{appointment.date}}
                            </div>
                        </div>
                        <div class="col-12">
                            <router-link to="/" class="router-link">
                                <button class="btn btn-primary btn-sm w-100 mb-2">Otkaži</button>
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
    name: 'AboutView',
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
            this.$router.push({ path: '/' })
        })

        this.appointments = [
            {
                id: 1,
                title: "Naslov pregleda",
                date: "12.1.2022."
            },
            {
                id: 2,
                title: "Naslov pregleda",
                date: "12.1.2022."
            },
            {
                id: 3,
                title: "Naslov pregleda",
                date: "12.1.2022."
            },
            {
                id: 4,
                title: "Naslov pregleda",
                date: "12.1.2022."
            },
            {
                id: 5,
                title: "Naslov pregleda",
                date: "12.1.2022."
            },
            {
                id: 6,
                title: "Naslov pregleda",
                date: "12.1.2022."
            }
        ]
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
        overflow: scroll;
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

    input::placeholder {
        font-weight: 400;
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