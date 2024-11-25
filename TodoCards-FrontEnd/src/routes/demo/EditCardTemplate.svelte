<script>
    import * as APIs from "$lib"

    let status = false
    let cardInfo = {
        cardId:             1,
        cardName:           "Write introduction",
        cardDescription:    "200 words zuzu",
        cardDue:            "Tue, 17 Oct 2023 00:00:00 GMT",
        cardColor:          "lightblue",
    }
    async function editCard(){
        // recieve the result
        status = await APIs.editCard(cardInfo)
    }

</script>

status = {status} <br>
<input type="text" placeholder="cardId" bind:value={cardInfo.cardId}> <br>
<input type="text" placeholder="cardName" bind:value={cardInfo.cardName}> <br>
<input type="text" placeholder="cardDescription" bind:value={cardInfo.cardDescription}> <br>
<input type="text" placeholder="cardDue" bind:value={cardInfo.cardDue}> <br>
<input type="text" placeholder="cardColor" bind:value={cardInfo.cardColor}> <br>
<input type="button" value="submit" on:click={editCard}>