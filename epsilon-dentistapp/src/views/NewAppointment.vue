<template>
    <TheHeader/>
    <div class="container bright">
        <form class="form-size">    
            <h2>Zakazivanje pregleda</h2>  
            <div class="form-group">
                <label for="type">Odaberi sotomatologa:</label>
                <select class="form-select form-control" id="type">
                    <option>Stomatolog 1</option>
                    <option>Stomatolog 2</option>
                    <option>Stomatolog 3</option>
                    <option>Stomatolog 4</option>
                </select>
            </div>
            <div class="form-group">
                <label>Datum:</label>
                <input type="date" class="form-control form-control-md" />
            </div>
            <div class="form-group">
                <label>Vreme:</label>
                <input type="time" class="form-control form-control-md" />
            </div>
            
            <ul class="list-group form-cols">
                    <li class="list-group-item align-items-center"  style="background-color:#ff6961">
                        Termin je zauzet
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center" style="background-color:#77dd77">
                        Slobodan je termin ranije:
                        <span class="badge badge-primary badge-pill">HH:MM</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center" style="background-color:#77dd77">
                        Slobodan je termin kasnije:
                        <span class="badge badge-primary badge-pill">HH:MM</span>
                    </li>
            </ul>
            <!-- Ovde bi mogli da postavljamo pitanja i tako olaksamo stomatologu posao, mozemo i da se konsultujemo sa nekim sa stomatologije sta je najbolje da tu napisemo -->
            <div class="form-group">
                <label for="diagnosis">Opis tegoba</label>
                <textarea class="form-control" id="opis-tegoba" rows="2"></textarea>
            </div>
            <button type="submit" class="btn">Zakazi</button>
        </form>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'NewAppointment',
  components: {
    TheHeader
  }
}
</script>

<style scoped>
    
</style>