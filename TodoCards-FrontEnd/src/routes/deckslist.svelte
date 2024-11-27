<script>
    import Createdeckmodal from "./createdeckmodal.svelte";
    import * as APIs from "$lib"
	import { onMount } from 'svelte'
    import Deck from "./deck.svelte";
    
    // Send request to backend to query the cards for us
    let deckslist = []
    export async function getDeckslist(){
        deckslist = await APIs.getDeckslist()
    }
    onMount(getDeckslist)

    let isAdding = false
    let refreshCards

    function addDeck() {
        isAdding = true
    }
</script>

<div>
    {#each deckslist as deck}
        <Deck bind:deckinfo={deck}></Deck>
    {/each}
</div>

<div class="header">
    <button class="add-btn bobbing-hover" on:click={addDeck}>
        <i class="fas fa-plus-circle "></i>
    </button>
</div>

<Createdeckmodal
    bind:showModal={isAdding} 
    refresh={getDeckslist}>
</Createdeckmodal>

<style>
    
    .add-btn {
        font-size: xx-large;
        padding: 0;
        height: 40px;
        width: 40px;
        border: none;
        border-radius: 50%;
        color: green;
        transition: 0.15s;
        cursor: pointer;
        background-color: transparent;
    }
    .add-btn:hover {
        color: rgb(10, 170, 10);
    }
</style>