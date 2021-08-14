# `box-sizing`

<div class="box content-box">
    <div class="child"></div>
</div>
<br/>
<div class="box border-box">
    <div class="child"></div>
</div>
<style>
    .box {
        height: 100px;
        width: 100px;
        border: 10px solid grey;
    }
    .content-box {
        box-sizing: content-box;
    }
    .border-box {
        box-sizing: border-box;
    }
</style>
