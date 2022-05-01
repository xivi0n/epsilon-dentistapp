<template>
    <div class="row">
        <div class="col-3 cell">
            {{review.name}}
        </div>
        <div class="col-7 cell-num">
            {{review.info}}
        </div>
        <div class="col-1 cell-num">
            {{review.num}}
        </div>
    </div>
</template>

<script>
export default {
    name: 'TheReview',
    props: {
        review: Object
    }
}
</script>

<style scoped>
    .cell {
        background: #9fd3c7;
        margin: 5px;
    }
    .cell-num {
        background: #9fd3c7;
        margin: 5px;
    }
</style>