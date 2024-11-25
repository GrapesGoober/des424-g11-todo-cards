<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";
	import Card from './cardcomponents/card.svelte'
    import EditdeckModal from "./deckcomponents/editdeckmodal.svelte";
    import Createcardmodal from "./cardcomponents/createcardmodal.svelte";

    // Send request to backend to query the cards for us
    let cardslist = []
    let deckinfo
    let formattedDeckDue = ""
    async function getCardslistAndDeckInfo(){
        // get the cardslist
        let searchParams = new URLSearchParams(window.location.search)
        let deckId = searchParams.get("deckId")
        cardslist = await APIs.getCardslist(deckId)

        // also get the deck info to display as well
        let deckslist = await APIs.getDeckslist()
        deckinfo = deckslist.find(deck => deck.deckId == deckId)

        if (deckinfo == null) {
            window.location.href = "/"
        }
        
        if (deckinfo.nearestDue != "") {
            let cardDue_dateObj = new Date(deckinfo.nearestDue)
            formattedDeckDue = new Intl.DateTimeFormat('en-US', {
                weekday: 'short',
                day: 'numeric',
                month: 'short'
            }).format(cardDue_dateObj);
        }
    }
    onMount(getCardslistAndDeckInfo)
    
    let isEditing = false
    async function showEditDeckModal(){
        isEditing = true
    }

    let isAdding = false
    async function showAddCardModal() {
        isAdding = true
    }

    
</script>

<!-- Font Awesome 5 Free -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
<link rel="apple-touch-icon" href="/custom_icon.png"/>


{#if deckinfo}
    <EditdeckModal
        bind:showModal={isEditing} 
        deckInfo={deckinfo}
        refresh={getCardslistAndDeckInfo}>
    </EditdeckModal>

    <Createcardmodal
        bind:showModal={isAdding} 
        bind:deckId={deckinfo.deckId}
        refresh={getCardslistAndDeckInfo}>
    </Createcardmodal>

    <h1>
        <a href="/">
            <i class="fas fa-angle-left"></i>
        </a>
        {deckinfo.deckName}
        {#if deckinfo.editable}
            <button class="edit-button bobbing-hover" on:click={showEditDeckModal}>
                <i class="fas fa-edit"></i>
            </button>
        {/if}
        
    </h1>
    
    {#if formattedDeckDue != ""}
        <p><b>Nearest Due Date</b> {formattedDeckDue}</p>
    {/if}
    <p>{deckinfo.deckDescription}</p>

    <div>
        {#each cardslist as card}
            <Card bind:cardinfo={card} bind:editable={deckinfo.editable} refresh={getCardslistAndDeckInfo}></Card>
        {/each}
    </div>

    {#if deckinfo.editable}
    <button class="add-btn bobbing-hover" on:click={showAddCardModal}>
        <i class="fas fa-plus-circle "></i>
    </button>
    {/if}

{/if}

<style>
    @import "../style.css";

    a {
        color: black;
    }
    .edit-button {
        left: 10px;
    }
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