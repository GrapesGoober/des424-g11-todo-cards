<script>
    import * as APIs from "$lib"

    let status = false
    let deckInfo = {
        deckId:             1,
        deckName:           "Write introduction",
        deckDescription:    "200 words zuzu"
    }
    async function editDeck(){
        // recieve the result
        status = await APIs.editDeck(deckInfo)
    }

</script>

status = {status} <br>
<input type="text" placeholder="deckId" bind:value={deckInfo.deckId}> <br>
<input type="text" placeholder="deckName" bind:value={deckInfo.deckName}> <br>
<input type="text" placeholder="deckDescription" bind:value={deckInfo.deckDescription}> <br>
<input type="button" value="submit" on:click={editDeck}>
