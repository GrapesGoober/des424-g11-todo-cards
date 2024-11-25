<script>
    
    import * as APIs from "$lib"
    
    let deckId = "1" // the input requires a deckid
    let cardslist = [] // output of the fetch goes into this list
    async function getCardslist(){
        cardslist = await APIs.getCardslist(deckId)
    }

    let cardId = "1" // the input requires a deckid
    let subcardslist = [] // output of the fetch goes into this list
    async function getSubcardslist(){
        subcardslist = await APIs.getSubcardslist(cardId)
    }

</script>


cardslist = {JSON.stringify(cardslist)} <br>
deckId = <input type="text" bind:value={deckId}>
<input type="button" value="get cards list!" on:click={getCardslist}> <br><br>

subcardslist = {JSON.stringify(subcardslist)} <br>
cardId = <input type="text" bind:value={cardId}>
<input type="button" value="get subcards list!" on:click={getSubcardslist}>