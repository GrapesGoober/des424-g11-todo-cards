<script>
    import * as APIs from "$lib"
    import Modal from "../../modal.svelte"
    import ColorPicker from "./colorpicker.svelte";
    import Datepicker from "./datepicker.svelte";
    export let showModal = false, deckId, refresh

    let today = new Date()
    let year = today.getFullYear()
    let month = String(today.getMonth() + 1).padStart(2, '0') // Month is zero-based, so we add 1 and pad with '0' if necessary
    let day = String(today.getDate()).padStart(2, '0')
    let todayString = `${year}-${month}-${day}`

    let cardInfo = {
        cardName:           "",
        cardDescription:    "",
        cardDue:            todayString,
        cardColor:          "",
    }

    async function createCard(){
        let status = await APIs.createCard(deckId, cardInfo)
        if (status == true) {
            await refresh()
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
        <h1>Create Card</h1>
    </div>


    <div class="deck-name">
        <p class="deckinfo-txt">Card Name</p>
        <input type="text" placeholder="Name" bind:value={cardInfo.cardName}>
    </div>


    <div class="deck-description">
        <p class="deckinfo-txt">Description</p>
        <input type="text" placeholder="Card Description" bind:value={cardInfo.cardDescription}>
    </div>


    <div class="deck-description">
        <p class="deckinfo-txt">Due date</p>
        <Datepicker bind:cardDue={cardInfo.cardDue}></Datepicker>
    </div>


    <div class="card-color">
        <p class="deckinfo-txt">Color</p>
        <ColorPicker bind:selectedColor={cardInfo.cardColor}></ColorPicker>
    </div>

    <br> <br>

    <div class="delete-submit">
        <button class="green-button bobbing-hover" on:click={createCard}>
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

    .card-color {
        display: flex;
        align-items: center;
        margin-left: 20px;
        margin-right: 20px;
        margin-top: 18px;
        margin-bottom: 10px;
    }

    .delete-submit {
        justify-content: space-between;
        align-items: center;
    }
    .green-button {
        color: green;
        font-size: 20px;
        cursor: pointer;
    }
    .green-button:hover {
        color: rgb(0, 194, 0);
    }

    button {
        background-color: transparent;
        border: none;
    }
</style>