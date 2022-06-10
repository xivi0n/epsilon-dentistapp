<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <form class="form-size">
                    <h2>Prijavi se</h2>
                    <div class="form-group">
                        <label>Email adresa</label>
                        <input type="email" id="username" class="form-control form-control-md cell" placeholder="email@something.com"/>
                    </div>
                    <div class="form-group">
                        <label>Lozinka</label>
                        <input type="password" id="password" class="form-control form-control-md cell" placeholder="********"/>
                    </div>
                    <p class="mt-2 mb-4">
                        <!-- <router-link to="/" class="forgot-password">Zaboravljena lozinka ?</router-link> -->
                    </p>
                    <button id="submit-btn" type="button" v-on:click="login()" class="btn btn-primary w-100">Prijavi se</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
    name: "UserLogin",
    components: {
    },
    mounted() {
        document.title = "Prijavljivanje"
        document.getElementById("password")
        .addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("submit-btn").click();
        }
        });
    },
    methods: {
        login() {
            axios.post("http://localhost:8000/api/v1/login/",
            {
                "username": document.getElementById("username").value,
                "password": document.getElementById("password").value
            })
            .then(response => {
                axios.get("http://localhost:8000/api/v1/moj-profil/",{
                headers: {
                    'Authorization': 'Token ' + response.data.token
                }}).then(response => {
                    let user = {
                        logged_in: true,
                        displayName: "",
                        tipK: "",
                        email: ""
                    }
                    user.displayName = response.data["ime"] + " " + response.data["prezime"]
                    user.tipK = response.data["tipK"]
                    user.email = response.data["email"]

                    localStorage.setItem("displayName", user.displayName)
                    localStorage.setItem("logged_in", user.logged_in)
                    localStorage.setItem("tipK", response.data.tipK)
                    localStorage.setItem("email", response.data.email)

                    this.emitter.emit("login-changed", user)
                    this.$router.push({ path: '/moj-profil' })
                }).catch(error => {
                    console.log(error)
                })
                localStorage.setItem("token", response.data.token)
            }).catch(error => {
                console.log(error)
                localStorage.setItem("token", "")
                localStorage.setItem("displayName", "")
                localStorage.setItem("logged_in", false)
                alert("Proveriti podatke!")

                this.emitter.emit('login-changed', {
                    logged_in: false,
                    displayName: "",
                    tipK: ""
                });
            })
        },  
    }
};
</script>

<style scoped>

    .form-group {
        margin-top: 10px;
        margin-bottom: 10px;
    }

    @media screen and (min-width: 600px) {
        .form-size {
            max-width: 40%;
            margin:auto
        }   
    }

    .forgot-password {
        text-align: left;
        text-decoration: none;
        font-weight: 400;
        font-size: 15px;
        padding-top: 10px;
        color: #05284B;
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

</style>