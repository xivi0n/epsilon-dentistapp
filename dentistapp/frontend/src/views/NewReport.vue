<template>
    <TheHeader/>
    <div class="container bright">
        <form class="form-size">    
            <h2>Nov izvestaj</h2>  
            <div class="form-group">
                <label for="type">Odaberi tip:</label>
                <select class="form-select form-control" id="type">
                    <option>Pregled</option>
                    <option>Konzervativna stomatologija</option>
                    <option>Estetska stomatologija</option>
                    <option>Operacija</option>
                </select>
            </div>
            <div class="form-group">
                <label>Maticni broj</label>
                <input type="number" class="form-control form-control-md" />
            </div>
            <div class="form-group">
                <label>Terapija</label>
                <div class="input-group mb-3">
                    <input type="text" class="form-control">
                        <div class="input-group-append">
                            <span class="input-group-text" id="basic-addon2">Dodaj</span>
                        </div>
                </div>
            </div>
            
            <ul class="list-group form-cols">
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        Lek1
                        <span class="badge badge-primary badge-pill">2x dnevno</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        Lek2
                        <span class="badge badge-primary badge-pill">1x dnevno</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        Lek3
                        <span class="badge badge-primary badge-pill">2x dnevno</span>
                    </li>
            </ul>
            <div class="form-group">
                <label for="diagnosis">Dijagnoza</label>
                <textarea class="form-control" id="diagnosis" rows="2"></textarea>
            </div>
            <button type="submit" class="btn">Sacuvaj</button>
        </form>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'

export default {
    name: 'NewReport',
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
        align-items: center;
    }
    .list-group-item{
        width: 80%;
    }
    .badge-primary {
        background: #385170;
    }
</style>