<script>
    import * as APIs from "$lib"
    import Subcardlist from "../subcardcomponents/subcardlist.svelte";
    import EditcardModal from "./editcardmodal.svelte";
    export let cardinfo, refresh, editable
    
    let showDescription = false
    async function finishCard() {
        if (editable == true) {
            let status = await APIs.finishCard(cardinfo.cardId, cardinfo.cardIsFinished)
            if (status == true) {
                refresh()
            }
        }
    }
    let isEditing = false
    let currentlyEditingCard
    function showEdit(cardinfo) {
        // deep copying the object to remove the binding & reference sematics shinanigans
        currentlyEditingCard = JSON.parse(JSON.stringify(cardinfo))
        isEditing = true
    }
    

    let formattedDate
    $ : {
        let cardDue_dateObj = new Date(cardinfo.cardDue)
        formattedDate = new Intl.DateTimeFormat('en-US', {
        weekday: 'short',
        day: 'numeric',
        month: 'short'
    }).format(cardDue_dateObj);
    }

</script>

{#if isEditing}
<EditcardModal 
    bind:showModal={isEditing} 
    bind:cardInfo={currentlyEditingCard}
    refresh={refresh}>
</EditcardModal>
{/if}

<div class="wrapper">

    <div class="card" style="background-color: {cardinfo.cardIsFinished ? "lightgrey" : cardinfo.cardColor};">
        <button class="tick {editable ? "bobbing-hover" : ""}" on:click={finishCard}>
            {#if cardinfo.cardIsFinished}
                <i class="fas fa-check-square fa-lg isFinished"></i>
            {:else}
                <i class="far fa-square fa-lg"></i>
            {/if}
        </button>

        <button class="title {cardinfo.cardIsFinished ? "isFinished" : ""}" on:click={()=>{showDescription = !showDescription}}>
            {cardinfo.cardName}
        </button>

        {#if showDescription && editable}
        <button class="edit-button bobbing-hover" on:click={()=>{showEdit(cardinfo)}}>
            <i class="fas fa-edit"></i>
        </button>
        {/if}
    </div>
    
    {#if showDescription}
        <div class="description-box">
            <!-- <i class="fas fa-spinner fa-pulse"></i> <br> -->
            <div>
                <p> Due {formattedDate} </p>
                <p>{cardinfo.cardDescription} </p>
            </div>
            <Subcardlist 
                bind:cardId={cardinfo.cardId} 
                bind:editable={editable} 
                refresh={refresh}>
            </Subcardlist>
        </div>
    {/if}
</div>


<style>
    .wrapper{
        padding: 10px;
        width: 20em;
    }
    .card {
        border-radius: 10px;
        border: none;
        display: flex;
        width: 100%;
    }
    .title {
        background-color: transparent;
        font-size: large;
        text-align: left;
        border: none;
        width: 16em;
        height: 100%;
        padding: 10px;
    }
    .tick {
        padding-left: 20px;
        background-color: transparent;
        border: none;
    }

    .description-box {
        font-size: small;
        width: 20em;
        padding-left: 15px;
    }

    .isFinished {
        color: grey;
    }

    .edit-button {
        left: -10px;
    }
</style>