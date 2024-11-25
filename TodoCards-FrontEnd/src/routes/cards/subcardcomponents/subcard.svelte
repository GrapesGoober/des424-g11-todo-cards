<script>
    import * as APIs from "$lib"
	import { clickOutside } from './clickOutside.js';

    export let subcardinfo, refresh, editable
    let isSelected = false, isEditing = false, currentlyEditingSubcard
    
    async function finishSubcard() {
        // need to do editable check since the check buttons still exist for view-only
        if (editable == true) {
            let status = await APIs.finishSubcard(subcardinfo.subcardId, subcardinfo.subcardIsFinished)
            if (status == true) {
                await refresh()
            }
        }
    }

    async function deleteSubcard() {
        let status = await APIs.deleteSubcard(subcardinfo.subcardId)
        if (status == true) {
            await refresh()
        }
    }

    async function editSubcard() {
        let status = await APIs.editSubcard(currentlyEditingSubcard)
        if (status == true) {
            await refresh()
            isSelected = false
            isEditing = false
        }
    }

    function editMode() {
        isEditing = true
        isSelected = false
        // deep copying the object to remove the binding & reference sematics shinanigans
        currentlyEditingSubcard = JSON.parse(JSON.stringify(subcardinfo))
    }

    function selectSubcard() {
        if (!isEditing && editable) {
            isSelected = !isSelected
        }
    }
    
</script>


<button 
    class="wrapper {isSelected ? "selected" : ""}" 
    on:click={selectSubcard}
    use:clickOutside on:click_outside={()=>{isSelected = false, isEditing = false}}>

    {#if subcardinfo.subcardIsFinished}
        <button class="tick {editable ? "bobbing-hover" : ""}" on:click={finishSubcard}>
            <i class="fas fa-check-square fa-lg grey"></i>
        </button>
        <span class="grey">
            {subcardinfo.subcardName}
        </span>
        {#if editable && isSelected}
            <button class="tick selected-icon bobbing-hover" on:click={deleteSubcard}>
                <i class="fas fa-trash-alt grey"></i>
            </button>
        {/if}
    {:else}
    
        {#if !isEditing}
            <button class="tick {editable ? "bobbing-hover" : ""}" on:click={finishSubcard}>
                <i class="far fa-square fa-lg"></i>
            </button>
            <span>
                {subcardinfo.subcardName}
            </span>
            {#if editable && isSelected}
                <button class="tick selected-icon bobbing-hover" on:click={editMode}>
                    <i class="fas fa-edit grey"></i>
                </button>
            {/if}
        {:else}
            <input class="textbox" type="text" placeholder="subcard name" bind:value={currentlyEditingSubcard.subcardName}>
            <button class="tick-circle green bobbing-hover" on:click={editSubcard}>
                <i class="far fa-check-circle"></i>
            </button>
        {/if}
    {/if}
</button>


<style>

    .wrapper{
        display: block;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        margin-left: 1em;
        width: 20em;
        border: none;
        background-color: transparent;
        text-align: left;
    }
    .selected {
        border: 1px solid black;
    }
    .tick {
        padding: 10px;
        background-color: transparent;
        border: none;
    }

    .grey {
        color: grey;
    }
    
    .selected-icon {
        position: absolute;
        left: 24em;        
    }
    
    .textbox {
        padding: 10px;
        background-color: lightgrey;
        border: none;
    }

    .tick-circle {
        font-size: x-large;
        border: none;
        background-color: transparent;
        position: relative;
    }

    .green {
        color: green;
    }
</style>