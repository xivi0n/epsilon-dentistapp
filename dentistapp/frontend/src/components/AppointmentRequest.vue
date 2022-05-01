<template>
    <div class="row">
        <div class="col-2 cell">
            {{request.name}}
        </div>
        <div class="col-3 cell-info">
            {{request.info}}
        </div>
        <div class="col-2 cell-info">
            {{request.date}}
        </div>
        <div class="col-1 cell-info">
            {{request.time}}
        </div>
        <div class="col-1 mx-2">
            <button class="btn btn-confirm">Potvrdi</button>
        </div>
        <div class="col-1 mx-2">
            <button class="btn btn-postpone">Odlozi</button>
        </div>
        <div class="col-1 mx-2">
            <button class="btn btn-decline">Otkazi</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'AppointmentRequest',
    props: {
        request: Object
    }
}
</script>

<style scoped>
    .cell {
        background: #9fd3c7;
        margin: 3px;
    }
    .cell-info {
        background: #9fd3c7;
        margin: 3px;
    }
    .cell-date {
        background: #9fd3c7;
        margin: 3px;
    }
    .cell-time {
        background: #9fd3c7;
        margin: 3px;
    }
    .btn-confirm {
        background: #77dd77;
    }
    .btn-postpone {
        color:darkgrey;
        background: #FDFD96;
    }
    .btn-decline {
        background: #ff6961;
    }
</style>