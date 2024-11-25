<script>
    export let colors = []
</script>
    <div class="icon-container">
        {#each colors as color, i}
            <div class="icon" style="
                background-color: {color};
                left: {i*5}px;
                z-index: {-i};
            "> </div>
        {/each  }
    </div>
    
<style>
    .icon-container {
        position: relative;
        left: 20px;
        top: -15px
    }
    .icon {
        width: 30px;
        height: 30px;
        border-radius: 4px;
        position: absolute;
        border: 1px solid white;
    }
</style>