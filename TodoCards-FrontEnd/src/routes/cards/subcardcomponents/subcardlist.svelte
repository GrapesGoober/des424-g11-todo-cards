<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";
    import Addsubcarditem from "./addsubcarditem.svelte";
    import Subcard from "./subcard.svelte";
    export let cardId, refresh, editable
    let subcardslist = []
    async function getSubcardslist() {
        await refresh()
        subcardslist = await APIs.getSubcardslist(cardId)
    }
    onMount(getSubcardslist)

    let isAddSubcard = false
    function showAddSubcard() {
        isAddSubcard = true
    }
</script>


{#each subcardslist as subcard}
    <Subcard bind:subcardinfo={subcard} bind:editable={editable} refresh={getSubcardslist}></Subcard>
{/each}

<Addsubcarditem
    bind:cardId={cardId}
    bind:show={isAddSubcard}
    refresh={getSubcardslist}>
</Addsubcarditem>

{#if editable && !isAddSubcard}
    <button class="add-subcard-button bobbing-hover" on:click={showAddSubcard}>
        <i class="fas fa-plus"></i> <span>Add Subcard</span>
    </button>
{/if}


<style>
    .add-subcard-button {
        background-color: transparent;
        border: none;
        margin: 5px;
    }

    .add-subcard-button:hover {
        color: gray;
    }
</style>