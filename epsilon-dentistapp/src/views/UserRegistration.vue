<template>
    <TheHeader />
    <div class="container">
        <form class="form-size">
            <h2>Registruj se</h2>
            <div class="col-md-12 form-cols">
                <div class="form-group col-md-6" align="center">
                    <label>Ime</label>
                    <input type="firstName" class="form-control form-control-md custom-w" />
                </div>
                <div class="form-group col-md-6" align="center">
                    <label>Prezime</label>
                    <input type="lastName" class="form-control form-control-md custom-w" />
                </div>
            </div>
            <div class="form-group">
                <label>Maticni broj</label>
                <input type="number" class="form-control form-control-md" />
            </div>
            <div class="form-group">
                <label>Adresa</label>
                <input type="address" class="form-control form-control-md" />
            </div>
            <div class="form-group">
                <label>Email adresa</label>
                <input type="email" class="form-control form-control-md" />
            </div>
            <div class="form-group">
                <label>Lozinka</label>
                <input type="password" class="form-control form-control-md" />
            </div>
            <div class="form-group">
                <label>Ponovljena lozinka</label>
                <input type="password" class="form-control form-control-md" />
            </div>
            <div class="form-group">
                <label for="type">Odaberi tip profila:</label>
                <select class="form-select form-control" id="type">
                    <option>Pacijent</option>
                    <option>Stomatolog</option>
                </select>
            </div>
            <button type="submit" class="btn">Registruj se</button>
        </form>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'

export default {
    name: 'RegistrationView',
    components: {
        TheHeader
    }
}
</script>

<style scoped>
    .custom-w {
        width: 85%;
    }
    .form-size {
        max-width: 40%;
        margin:auto
    }
    .form-cols {
        display: flex;
        justify-content: space-between;
    }
</style>