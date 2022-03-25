<template>
    <TheHeader/>
    <div class="container">
      <form class="form-size">    
            <h2>Korisnicka podrska</h2>  
            <div class="form-group">
                <label for="type">Odaberi tip:</label>
                <select class="form-select form-control" id="type">
                    <option>Tehnicka podrska</option>
                    <option>Prijava greske</option>
                    <option>Opste pitanje</option>
                </select>
            </div>
            <div class="form-group">
                <label>E-mail adresa</label>
                <input type="text" class="form-control form-control-md" />
            </div>
            
            
            <div class="form-group">
                <label for="diagnosis">Zahtev</label>
                <textarea class="form-control" id="customer-support" rows="2"></textarea>
            </div>
            <button type="submit" class="btn">Posalji</button>
        </form>  
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'CustomerService',
  components: {
    TheHeader
  }
}
</script>

<style scoped>
    
</style>