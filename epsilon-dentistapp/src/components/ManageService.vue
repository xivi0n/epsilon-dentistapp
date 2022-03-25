<template>
    <div class="row">
        <div class="col-8 cell">
            {{service.name}}
        </div>
        <div class="col-1 cell-info">
            {{service.info}}
        </div>
        <div class="col-1 mx-2">
            <button class="btn btn-confirm">Uredi</button>
        </div>
        <div class="col-1 mx-2">
            <button class="btn btn-decline">Obrisi</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ManageService',
    props: {
        service: Object
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