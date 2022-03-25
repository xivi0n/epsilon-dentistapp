<template>
    <TheHeader />
    <div class="container bright">
        <form class="form-size">
            <h2>Prijavi se</h2>
            <div class="form-group">
                <label>Email adresa</label>
                <input type="email" class="form-control form-control-lg" />
            </div>
            <div class="form-group">
                <label>Lozinka</label>
                <input type="password" class="form-control form-control-lg" />
            </div>
            <button type="submit" class="btn">Prijavi se</button>
            <p class="forgot-password text-right mt-2 mb-4">
                <router-link to="/">Zaboravljena lozinka ?</router-link>
            </p>
        </form>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from "@/components/TheHeader.vue";

export default {
    name: "UserLogin",
    components: {
        TheHeader
    },
};
</script>

<style scoped>
    .form-size {
        max-width: 40%;
        margin:auto
    }

    .forgot-password,
    .forgot-password a {
        text-align: right;
        font-size: 13px;
        padding-top: 10px;
        color: #7a7a7a;
        margin: 0;
    }
    .forgot-password a {
        color: #142d4c;
    }

</style>