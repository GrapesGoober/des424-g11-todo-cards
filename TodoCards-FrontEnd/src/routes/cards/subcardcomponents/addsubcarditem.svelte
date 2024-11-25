<script>
    import * as APIs from "$lib"
    export let refresh, cardId, show

    let subcardinfo = {
        subcardName : ""
    }
    async function addSubcard() {
        let status = await APIs.createSubcard(cardId, subcardinfo)
        if (status == true) {
            await refresh()
            subcardinfo.subcardName = ""
            show = false
        }
    }

    async function cancel() {
        show = false
    }
</script>

{#if show}
<div class="wrapper">
    <input class="textbox" type="text" placeholder="subcard name" bind:value={subcardinfo.subcardName}>
    
    <button class="tick green bobbing-hover" on:click={addSubcard}>
        <i class="far fa-check-circle"></i>
    </button>

    <button class="tick red bobbing-hover" on:click={cancel}>
        <i class="far fa-times-circle"></i>
    </button>

</div>
{/if}


<style>
    .wrapper{
        margin-left: 1em;
        display: flex;
    }
    .textbox {
        align-items: center;
        padding-left: 10px;
        padding-bottom: 2px;
        border-radius: 4px;
        background-color: lightgrey;
        border: none;
    }
    .textbox:focus {
        box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.3);
    }
    .tick {
        font-size: x-large;
        border: none;
        background-color: transparent;
        position: relative;
    }

    .green {
        color: green;
    }
    .red {
        color: red;
    }
    
</style>