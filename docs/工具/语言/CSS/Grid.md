# Grid

<div class="grid">
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
</div>
<style>
    .grid {
        display: grid;
        gap: 10px;
        /*grid-auto-flow: column dense;*/
        /*grid-auto-columns: min-content;*/
    }
    .box {
        background: lightgray;
        height: 100px;
        width: 100px;
    }
</style>
