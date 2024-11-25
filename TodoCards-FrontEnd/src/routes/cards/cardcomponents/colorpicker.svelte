<script>
    let availableColors = [
        "PaleTurquoise",
        "lightgreen",
        "pink",
        "Thistle",
        "PaleGoldenRod",
        "Wheat"
    ]
    export let selectedColor = availableColors[0]
</script>

{#each availableColors as color}
    <button 
        class="color-button bobbing-hover" 
        style="color: {color};"
        on:click={()=>{selectedColor = color}}>
        <i class="fas fa-circle {color == selectedColor ? "selected-button" : ""}"></i>
    </button>
{/each}

<style>
    .color-button {
        background-color: transparent;
        border: none;
        border-radius: 50%;
        width: 20px;
        height: 20px;
        margin-left: 2px;
        font-size: large;
    }

    .selected-button {
        border: 2px solid grey;
        border-radius: 50%;
    }
</style>