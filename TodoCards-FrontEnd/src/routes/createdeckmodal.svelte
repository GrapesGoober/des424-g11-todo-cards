<script>
    import * as APIs from "$lib"
    import Modal from "./modal.svelte"
    export let showModal = false, refresh
    let deckInfo = {
        deckName:           "",
        deckDescription:    ""
    }

    async function createDeck(){
        let status = await APIs.createDeck(deckInfo)
        if (status == true) {
            refresh()
            showModal = false
        }
    }
    function cancel() {
        showModal = false
    }
</script>

<Modal bind:showModal={showModal}>
    <div class="header">
        <button class="cancel_btn" on:click={cancel}><i class="fas fa-angle-left"></i></button>
        <h1>Create Deck</h1>
    </div>

    <div class="deck-name">
        <p class="deckinfo-txt">Deck Name</p>
        <input type="text" placeholder="Name" bind:value={deckInfo.deckName}>
    </div> 

    <div class="deck-description">
        <p class="deckinfo-txt">Description</p>
        <input type="text" placeholder="Description" bind:value={deckInfo.deckDescription}>
    </div>

    <div class="delete-submit">
        <button class="green-button bobbing-hover"  on:click={createDeck}>
            <i class="fas fa-check-circle"></i>
        </button>

    </div>

</Modal>

<style>
    p {
        margin: 0;
    }
    h1 {
        margin: 0;
    }
    input {
        width: 250px;
        padding: 4px;
        padding-left: 6px;
        border: solid;
        border-width: 1px;
        border-radius: 4px;
        border-color: rgb(156, 156, 156);
    }
    input:focus {
        box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.3);
    }
    .header, .delete-submit {
        display: flex;
        align-items: center;
    }
    .deck-name, .deck-description, .delete-submit {
        margin-left: 20px;
        margin-right: 20px;
        margin-bottom: 10px;
    }

    .header {
        margin: 10px;
    }

    .deckinfo-txt {
        margin-bottom: 4px;
    }

    .cancel_btn {
        font-size: 36px;
        background-color: white;
        border: none;
        padding-right: 15px;
        cursor: pointer;
    }
    .cancel_btn:active {
        color: rgb(77, 77, 77);
    }

    .delete-submit {
        justify-content: space-between;
        align-items: center;
    }
    .red-button {
        color: rgb(187, 0, 0);
        font-size: 20px;
        cursor: pointer;
        background-color: transparent;
        border: none;
    }
    .red-button:hover {
        color: rgb(229, 0, 0);
    }
    .green-button {
        color: green;
        font-size: 20px;
        cursor: pointer;
        background-color: transparent;
        border: none;
    }
    .green-button:hover {
        color: rgb(0, 194, 0);
    }
</style>
