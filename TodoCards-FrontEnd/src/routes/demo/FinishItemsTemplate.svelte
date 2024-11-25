<script>
    import * as APIs from "$lib"

    let cardId = 1
    let finishCardResult = false
    async function finishCard(){
        finishCardResult = await APIs.finishCard(cardId, false)
    }
    let subcardId = 1
    let finishSubardResult = false
    async function finishSubcard(){
        finishSubardResult = await APIs.finishSubcard(subcardId, false)
    }
</script>

<p>finishCardResult = {finishCardResult}</p>
cardId <input type="text" bind:value={cardId}>
<input type="button" value="Finish Card!" on:click={finishCard}>

<p>finishSubardResult = {finishSubardResult}</p>
subcardId <input type="text" bind:value={subcardId}>
<input type="button" value="Finish Subcard!" on:click={finishSubcard}>