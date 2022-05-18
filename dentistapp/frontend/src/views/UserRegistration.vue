<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <form class="form-size" action="http://192.168.100.6:8000/registracija" method="post" id="reg-form">
                    <h2>Registruj se</h2>
                    <div class="row">
                        <div class="col-md-6 col-12">
                            <div class="form-group">
                                <label>Ime</label>
                                <input type="firstname" class="form-control form-control-md cell" placeholder="Ivan"/>
                            </div>
                        </div>
                        <div class="col-md-6 col-12">
                            <div class="form-group">
                                <label>Prezime</label>
                                <input type="lastname" class="form-control form-control-md cell" placeholder="Ivanovic"/>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Email adresa</label>
                        <input type="email" class="form-control form-control-md cell" placeholder="email@something.com"/>
                    </div>

                    <div class="form-group">
                        <label>JMBG</label>
                        <input type="text" pattern="^\s*?\d{13}(?:[-\s]\d{13})?\s*?$" class="form-control form-control-md cell" placeholder="1101001000011"/>
                    </div>

                    <div class="row">
                        <div class="col-md-6 col-12">
                            <div class="form-group">
                                <label>Lozinka</label>
                                <input type="password" class="form-control form-control-md cell" placeholder="********"/>
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
                        <select class="form-select mb-3 cell" aria-label="Default select example">
                            <option value="Pacijent" selected>Pacijent</option>
                            <option value="Stomatolog">Stomatolog</option>
                        </select>
                    </div>
                    <button type="submit" form="reg-form" value="Submit" class="btn btn-primary w-100 mb-3">Registruj se</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: 'RegistrationView',
    components: {
    },
    mounted() {
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