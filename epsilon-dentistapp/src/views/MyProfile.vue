<template>
    <TheHeader/>
    <div class="container bright">
        <h2>Moj profil</h2>
        <img alt="slika pacijenta" style="width: 20%;max-height: 100%; margin:5px" src="../assets/pacijent-za-profil.jpg">
        <ul class="">
                    <li class="list-group-item d-flex justify-content-between align-items-center bright-green">
                        Ime
                        <span style="color:#ececec">Ivana</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center bright-green">
                        Prezime
                        <span style="color:#ececec">Ivanic</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center bright-green">
                        Maticni broj
                        <span style="color:#ececec">12345678912345</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between  bright-green">
                        Informacije
                        <span style="color:#ececec">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum est nibh, condimentum ac pulvinar ac, ullamcorper id tortor. Nulla a sodales nulla. Morbi in iaculis lorem, non ultrices tellus. Fusce.</span>
                    </li>        
            </ul>
          <button type="submit" class="btn" style="background:#FDFD96; color:darkgrey;">Prikazi prethodne izvestaje</button>  
          <button type="submit" class="btn">Izmeni profil</button>  
    </div>
</template>
<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'AboutView',
  components: {
    TheHeader
  }
}
</script>

<style>
.white-text {
    display: flex;
    justify-content: space-around;
}
</style>