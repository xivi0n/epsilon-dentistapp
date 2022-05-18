<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <form class="form-size">
                    <h2>Prijavi se</h2>
                    <div class="form-group">
                        <label>Email adresa</label>
                        <input type="email" class="form-control form-control-md cell" placeholder="email@something.com"/>
                    </div>
                    <div class="form-group">
                        <label>Lozinka</label>
                        <input type="password" class="form-control form-control-md cell" placeholder="********"/>
                    </div>
                    <p class="mt-2 mb-4">
                        <router-link to="/" class="forgot-password">Zaboravljena lozinka ?</router-link>
                    </p>
                    <button type="submit" class="btn btn-primary w-100">Prijavi se</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: "UserLogin",
    components: {
    },
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