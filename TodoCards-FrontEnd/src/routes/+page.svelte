<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";
    import Deckslist from "./deckslist.svelte";

    async function logout(){
        await APIs.logout()
        window.location.href = "/login";
    }

    async function handleSharecode() {
        let searchParams = new URLSearchParams(window.location.search)
        let sharecode = searchParams.get("sharecode")
        if (sharecode != null) {
            let status = await APIs.recieveSharecode(sharecode)
            if (status.deckId) {
                window.location.replace(`/cards?deckId=${status.deckId}`)
            }
            else {
                window.location.replace("/")
                alert("Share code invalid (it probably expired)")
            }
        }
    }

    onMount(handleSharecode)
</script>

<!-- Font Awesome 5 Free -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
<link rel="apple-touch-icon" href="/custom_icon.png"/>
<!--This is the deckslist page (the home page)-->
<div class="header">
    <h1 class="todo-header">Todo</h1>
    <button class="bobbing-hover user-btn" on:click={logout}>
        <i class="fas fa-sign-out-alt"></i>
    </button>
</div>
<div>
    <Deckslist></Deckslist>
</div>



<style>
    @import "./style.css";
    h1 {
        margin: 0;
    }
    .header {
        margin-top: 20px;
        margin-left: 26px;
        width: 450px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .user-btn {
        font-size: xx-large;
        border: none;
        color: rgb(89, 89, 89);
        cursor: pointer;
        transition: 0.15s;
        background-color: white;
    }

    .user-btn:hover {
        color: rgb(145, 145, 145);
    }
</style>