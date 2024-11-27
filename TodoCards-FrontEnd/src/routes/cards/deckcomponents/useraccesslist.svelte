<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";

    export let deckId, usersToRemove = []
    let access = {}
    async function getAccessList() {
        access = await APIs.getAccessList(deckId)
    }
    function pushUserToRemove(username) {
        if (access.edit) access.edit = access.edit.filter(item => item !== username);
        if (access.view) access.view = access.view.filter(item => item !== username);
        usersToRemove.push(username)
    }
    onMount(getAccessList)

</script>

{#if access}
    
    {#if access.edit}
        <div class="editor-viewer-section"> <!--this part doesn't appear if you don't have other editors-->
            <div>Editor: </div>
            {#each access.edit as editorName}
                <div class="editor-viewer-name">
                    <p class="shared-user">{editorName}</p>
                    <button class="user-delete bobbing-hover" on:click={() => pushUserToRemove(editorName)}>
                        <i class="fas fa-times"></i>
                    </button>
                </div>
            {/each}
        </div>
    {/if}

    {#if access.view}
        <div class="editor-viewer-section"> <!--this part doesn't appear if you don't have other viewer-->
            <div>Viewer: </div>
            {#each access.view as viewerName}
                <div class="editor-viewer-name">
                    <p class="shared-user">{viewerName}</p>
                    <button class="user-delete bobbing-hover" on:click={() => pushUserToRemove(viewerName)}>
                        <i class="fas fa-times"></i>
                    </button>
                </div>
            {/each}
        </div>
    {/if}
{/if}


<style>
    p {
        margin: 0;
    }
    .editor-viewer-section, .editor-viewer-name {
        display: flex;
        align-items: center;
    }
    .editor-viewer-section {
        margin-left: 20px;
        margin-right: 20px;
        margin-bottom: 10px;
    }

    .editor-viewer-name {
        background-color: rgb(110, 110, 255);
        color: white;
        border-radius: 15px;
        margin-left: 4px;
        padding-left: 8px;
        padding-right: 8px;
        padding-top: 3px;
        padding-bottom: 3px;
        align-items: center;
        text-align: center;
    }
    .shared-user {
        font-size: 14px;
    }
    .user-delete {
        color: white;
        background-color: rgb(110, 110, 255);
        border: none;
        font-weight: bold;
        padding: 0;
        margin-left: 5px;
        cursor: pointer;
    }

</style>