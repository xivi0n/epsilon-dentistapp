<template>
    <div class="row">
        <div class="col-10 cell">
            {{service.name}}
        </div>
        <div class="col-1 cell-price">
            {{service.price}}
        </div>
    </div>
</template>

<script>
export default {
    name: 'TheService',
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
    .cell-price {
        background: #9fd3c7;
        margin: 5px;
    }
</style>