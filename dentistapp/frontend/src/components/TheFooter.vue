<template>
    <div class="footer my-auto pb-2">
        <h4> Copyright (c) 2022 DentistApp All rights reserved </h4>
    </div>
</template>

<script>
export default {
    name: 'TheFooter'
}
</script>

<style scoped>
    .footer {
        position: sticky;
        top: 100%;
        width: 100%;
        text-align: center;
        padding: 10px auto 0 auto;
        border-top: 2px solid #142d4c;
        background-color: #05284B;
        color: #FFFFFF;
        box-shadow: 0px -5px 10px -5px rgba(0,0,0,0.4);
    }
    
    h4 {
        margin-top: 15px;
        font-size: 15px;
        font-weight: 600;
    }
</style>