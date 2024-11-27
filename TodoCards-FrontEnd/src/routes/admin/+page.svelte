<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";
    import Modal from "../modal.svelte"

    async function logout(){
        await APIs.logout()
        window.location.href = "/login";
    }

    let data
    async function getEverything() {
        data = await APIs.adminGetEverything()
    }
    onMount(getEverything)

    async function deleteDeck(deckId) {
        let status = await APIs.deleteDeck(deckId)
        if (status == true) {
            location.reload();
        }
    }

    async function revokeAccess(deckId, username) {
        let status = await APIs.removeAccess(deckId, username)
        if (status == true) {
            location.reload();
        }
    }

    async function banUser(username) {
        let status = await APIs.adminDeleteUser(username)
        if (status == true) {
            location.reload();
        }
    }

    function getUsersOfDeck(deck) {
        return data.accesslist.filter(access => access.deckId == deck.deckId)
    }

    let showingDeleteModal = false, deletingdeck
    async function showDeleteModal(deck) {
        showingDeleteModal = true
        deletingdeck = deck
    }

    let showingRevokeModal = false, revokingaccess, revokingdeckname
    async function showRevokeModal(access) {
        showingRevokeModal = true
        revokingaccess = access
        revokingdeckname = data.deckslist.filter(deck => deck.deckId == access.deckId)[0].deckName
    }

    let showingBanModal = false, banUsername
    async function showBanModal(username) {
        console.log(username)
        console.log(data.users)
        showingBanModal = true
        banUsername = username
    }

    function cancel() {
        showingDeleteModal = false
        showingRevokeModal = false
        showingBanModal = false
    }

</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
<link rel="apple-touch-icon" href="/custom_icon.png"/>

<h1>Hello Admin
<button class="fas fa-sign-out-alt user-btn" on:click={logout}></button>
</h1>

<Modal bind:showModal={showingDeleteModal}>
    <h2>Confirm delete deck</h2>
    <h3>Deck Name: {deletingdeck.deckName}</h3>
    <p> <b>Users:</b> 
        {#each getUsersOfDeck(deletingdeck) as access}
            <span>{access.username}, </span>
        {/each}
    </p>
    <button on:click={cancel}>
        <i class="fas fa-lg fa-times-circle "></i>
    </button>
    <button class="confirm-button"  on:click={()=>deleteDeck(deletingdeck.deckId)}>
        <i class="fas fa-lg fa-check-circle "></i>
    </button>
</Modal>

<Modal bind:showModal={showingRevokeModal}>
    <h2>Confirm Revoke Access</h2>
    <h3>User Name: {revokingaccess.username}</h3>
    <h3>Deck Name: {revokingdeckname}</h3>
    <button on:click={cancel}>
        <i class="fas fa-lg fa-times-circle "></i>
    </button>
    <button class="confirm-button" on:click={()=>revokeAccess(revokingaccess.deckId, revokingaccess.username)}>
        <i class="fas fa-lg fa-check-circle "></i>
    </button>
</Modal>

<Modal bind:showModal={showingBanModal}>
    <h2>Confirm Ban User</h2>
    <h3>User Name: {banUsername}</h3>
    
    <button on:click={cancel}>
        <i class="fas fa-lg fa-times-circle "></i>
    </button>
    <button class="confirm-button" on:click={()=>banUser(banUsername)}>
        <i class="fas fa-lg fa-check-circle "></i>
    </button>
</Modal>

{#if data}
    <h2>Decks</h2>
    {#each data.deckslist as deck}
        <div class="nested-div">
            <h3>{deck.deckName} <button class="bobbing-hover" on:click={()=>showDeleteModal(deck)}>
                <i class="fas fa-times"></i>
            </button></h3>
            <div class="nested-div">
                {#each getUsersOfDeck(deck) as access}
                    <span>{access.username} : {access.accessType}</span>
                    <button class="bobbing-hover" on:click={()=>showRevokeModal(access)}>
                        <i class="fas fa-times"></i>
                    </button>
                    <br>
                    <br>
                {/each}
            </div>
        </div>
    {/each}

    <h2>Users</h2>
    <div class="nested-div">
        {#each data.users as user}
            <span>{user}</span>
            <button class="bobbing-hover" on:click={()=>showBanModal(user)}>
                <i class="fas fa-times"></i>
            </button>
            <br>
            <br>
        {/each}
    </div>
{/if}

<style>
    @import "../style.css";
    h1 {
        margin: 0;
    }
    .confirm-button {
        position: relative;
        float: right;
    }
    .nested-div {
        margin: 1em 2em;
    }
    button {
        border: none;
        background-color: transparent;
    }
    .user-btn {
        font-size: xx-large;
        border: none;
        color: rgb(89, 89, 89);
        cursor: pointer;
        transition: 0.15s;
        background-color: white;
        position:relative;
        left: 40%;
    }

    .user-btn:hover {
        color: rgb(145, 145, 145);
    }
</style>
