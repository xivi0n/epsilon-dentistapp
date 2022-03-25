<template>
    <div class="row">
        <div class="col-3 cell">
            {{request.name}}
        </div>
        <div class="col-5 cell-info">
            {{request.info}}
        </div>
        <div class="col-1 mx-2">
            <button class="btn btn-confirm">Potvrdi</button>
        </div>
        <div class="col-1 mx-2">
            <button class="btn btn-decline">Obrisi</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'TheRequest',
    props: {
        request: Object
    }
}
</script>

<style scoped>
    .cell {
        background: #9fd3c7;
        margin: 5px;
    }
    .cell-info {
        background: #9fd3c7;
        margin: 5px;
    }
    .btn-confirm {
        background: #77dd77;
    }
    .btn-decline {
        background: #ff6961;
    }
</style>