<template>
    <div v-if="show_price == false" class="col-12 p-1">
        <div class="col-12 p-2 cell">
            {{service.opis}}
        </div>
    </div>
    <div v-if="show_price == true" class="col-lg-11 col-12 p-1">
        <div class="col-12 p-2 cell">
            {{service.opis}}
        </div>
    </div>
    <div v-if="show_price == true" class="col-lg-1 col-3 p-1">
            <div class="col-12 p-2 cell price">
            {{service.cena}}
        </div>
    </div>
</template>

<script>
export default {
    name: 'TheService',
    props: {
        service: Object,
        show_price: {
            default: true,
        }
    }
}
</script>

<style scoped>
    .cell {
        box-shadow: -4px 4px 25px rgba(0, 0, 0, 0.25);
		border-radius: 10px;
        text-align: center;
    }

    .price {
        background-color: #05284B;
        color: white;
    }
</style>