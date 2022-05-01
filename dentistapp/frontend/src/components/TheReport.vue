<template>
    <div class="row">
         <div class="col-1 cell-diagnosis">
            {{report.id}}
        </div>
        <div class="col-7 cell">
            {{report.therapy}}
        </div>
        <div class="col-2 cell-diagnosis">
            {{report.diagnosis}}
        </div>
        <div class="col-1">
            <button class="btn">Prikazi</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'TheService',
    props: {
        report: Object
    }
}
</script>

<style scoped>
    .cell {
        background: #9fd3c7;
        margin: 5px;
    }
    .cell-diagnosis {
        background: #9fd3c7;
        margin: 5px;
    }
</style>