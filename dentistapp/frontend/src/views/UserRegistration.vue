<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <form class="form-size" id="reg-form">
                    <h2>Registruj se</h2>
                    <div class="row">
                        <div class="col-md-6 col-12">
                            <div class="form-group">
                                <label>Ime</label>
                                <input id="ime" type="firstname" name="ime" class="form-control form-control-md cell" placeholder="Ivan"/>
                            </div>
                        </div>
                        <div class="col-md-6 col-12">
                            <div class="form-group">
                                <label>Prezime</label>
                                <input id="prezime" type="lastname" name="prezime" class="form-control form-control-md cell" placeholder="Ivanovic"/>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Email adresa</label>
                        <input id="email" type="email" name="email" class="form-control form-control-md cell" placeholder="email@something.com"/>
                    </div>

                    <div class="form-group">
                        <label>JMBG</label>
                        <input id="matbroj" type="text" name="matbroj" pattern="^\s*?\d{13}(?:[-\s]\d{13})?\s*?$" class="form-control form-control-md cell" placeholder="1101001000011"/>
                    </div>

                    <div class="row">
                        <div class="col-md-6 col-12">
                            <div class="form-group">
                                <label>Lozinka</label>
                                <input id="password" type="password" name="password" class="form-control form-control-md cell" placeholder="********"/>
                            </div>
                        </div>
                        <div class="col-md-6 col-12">
                            <div class="form-group">
                                <label>Ponovi lozinku</label>
                                <input type="password" class="form-control form-control-md cell" placeholder="********"/>
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Tip naloga</label>
                        <select id="tipK" class="form-select mb-3 cell" aria-label="Default select example">
                            <option value="pacijent" selected>Pacijent</option>
                            <option value="stomatolog">Stomatolog</option>
                        </select>
                    </div>
                    <button v-on:click="register()" type="button" class="btn btn-primary w-100 mb-3">Registruj se</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
    name: 'RegistrationView',
    components: {
    },
    mounted() {
    },
    methods: {
        register() {
            let e = document.getElementById("tipK");
            let ime = document.getElementById("ime").value
            let prezime = document.getElementById("prezime").value
            let email = document.getElementById("email").value
            axios.post("http://localhost:8000/api/v1/registracija/",
            {
                "ime": ime,
                "prezime": prezime,
                "email": email,
                "matbroj": document.getElementById("matbroj").value,
                "password": document.getElementById("password").value,
                "tipK": e.options[e.selectedIndex].value
            })
            .then(response => {
                console.log(response);
                if (response.data["email"][0] == "korisnik with this email already exists.")
                    alert("Postoji korisnik sa zadatom email adresom")
                else
                    this.$router.push({ path: '/' })
            })
        }
    }
}
</script>

<style scoped>
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

    @media screen and (min-width: 1000px) {
        .form-size {
            max-width: 40%;
            margin: auto;
        }   
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

    input {
        color: #05284B;
    }
</style>