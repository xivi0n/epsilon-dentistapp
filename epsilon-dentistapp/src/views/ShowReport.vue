<template>
    <TheHeader/>
    <div class="container bright" align="center">
        <label>Maticni broj</label>
        <input type="number" class="form-control form-control-md"/>
        <div :key="report.id" v-for="report in reports">
            <TheReport :report="report"/>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'
import TheReport from '@/components/TheReport.vue'

export default {
    name: 'ShowReport',
    components: {
        TheHeader,
        TheReport
    },
    data() {
        return {
            reports: []
        }
    },
    created() {
        this.reports = [
            {
                id: 1,
                therapy: "Terapija 1",
                diagnosis: "Dijagnoza 1"
            },
            {
                id: 2,
                therapy: "Terapija 2",
                diagnosis: "Dijagnoza 2"
            },
            {
                id: 3,
                therapy: "Terapija 3",
                diagnosis: "Dijagnoza 3"
            },
            {
                id: 4,
                therapy: "Terapija 4",
                diagnosis: "Dijagnoza 4"
            }
        ]
    }
}
</script>

<style scoped>
    
</style>