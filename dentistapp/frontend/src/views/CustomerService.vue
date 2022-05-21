<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <form class="form-size">
                    <h2>Korisnička podrška</h2>
                    <div class="form-group">
                        <label>Vrsta problema</label>
                        <select class="form-select mb-3 cell" aria-label="Vrsta problema">
                            <option value="Stomatolog" selected>Stomatološki problem</option>
                            <option value="Tehnicki problem">Tehnički problem</option>
                            <option value="Informacije">Informacije</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Email adresa</label>
                        <input type="email" class="form-control form-control-md cell" placeholder="email@something.com"/>
                    </div>
                    <div class="form-group">
                        <label>Naslov</label>
                        <input type="text" class="form-control form-control-md cell" placeholder="Postoji problem ..."/>
                    </div>
                    <div class="form-group">
                        <label>Opis problema</label>
                        <textarea class="form-control cell" id="exampleFormControlTextarea1" rows="4" placeholder="Opišite problem ..."></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary w-100 my-3">Pošalji upit</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'CustomerService',
  components: {
  }
}
</script>

<style scoped>
    .btn-primary, .btn:focus, .btn:active {
        background: #05284B;
        border: 1px solid #05284B;
        border-radius: 10px;
    }

    .cell {
        /* background: #FFFFFF; */
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
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

    input, textarea {
        color: #05284B;
    }

</style>