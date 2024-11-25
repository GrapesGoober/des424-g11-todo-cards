<script>
    import * as APIs from "$lib"
  import { fade } from "svelte/transition";
    export let deckId
    let accessType, sharecode, isCopied = false

    async function getSharecode() {
        sharecode = await APIs.getSharecode(deckId, accessType)
        sharecode = `${window.location.origin}?sharecode=${sharecode}`
    }

    function copy() {
        navigator.clipboard.writeText(sharecode)
        .then(() => {
            isCopied = true
            setTimeout(()=> isCopied=false, 3000)
        })
    }
</script>


<div class="share-section"> <!--share section-->
    <i class="fas fa-user-plus fa-2xs share-icon"></i>
    <div class="share-icon">share</div>
    <div>
        <select class="share-combobx" id="myComboBox" name="myComboBox" bind:value={accessType}>
            <option value="edit">Editor</option>
            <option value="view">Viewer</option>
        </select>

        <button class="bobbing-hover" on:click={getSharecode}>
            <i class="fas fa-share-square"></i>
            <span>Generate Code</span>
        </button>
    </div>
</div>

<!--link section will appear when you choose an option in share section-->
{#if sharecode}
    <div class="link-section">
        <div>Link</div>
        <textarea cols="30" rows="2" readonly>{sharecode}</textarea>
        
        <button class="bobbing-hover" on:click={copy}>
            <i class="far fa-copy fa-xs copy-icon"></i>
        </button>

        {#if isCopied}
        <div class="copy-wrapper">
            <span class="copied-display" out:fade>
                Copied!
            </span>
        </div>
        {/if}
    </div>
    <p class="link-txt">This link will be expired in 3 minutes</p>
{/if}


<style>
    p {
        margin: 0;
    }
    button {
        background-color: transparent;
        border: none;
    }
    .share-section, .link-section, .link-code {
        display: flex;
        align-items: center;
    }
    .share-section, .link-section, .link-txt {
        margin-left: 20px;
        margin-right: 20px;
        margin-bottom: 10px;
    }
    .share-section {
        margin-bottom: 20px;
    }
    .share-icon {
        margin-right: 5px;
    }
    .share-combobx {
        padding: 3px;
        padding-left: 6px;
        border: solid;
        border-width: 1px;
        border-radius: 4px;
        border-color: rgb(156, 156, 156);
    }
    
    .link-code {
        width: 200px;
        justify-content: space-between;
        align-items: center;
        margin-left: 10px;

        padding: 3px;
        padding-left: 6px;
        padding-right: 6px;
        border: solid;
        border-width: 1px;
        border-radius: 4px;
    }
    .copy-icon {
        color: black;
        padding: 0;
        border: none;
        background-color: white;
        font-size: 15px;
        cursor: pointer;
    }
    .copy-icon:active {
        color: rgb(84, 84, 84);
    }
    .link-txt {
        color: red;
        font-size: 12px;
        margin-bottom: 25px;
    }
    .copy-wrapper {
        position: relative;

    }
    .copied-display{ 
        position: absolute;
        top: 10px;
        left: -20px;
        font-size: small;
    }
</style>