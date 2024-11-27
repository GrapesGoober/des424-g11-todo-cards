<script>
    import * as APIs from "$lib"

    let deckId = 1
    let sharecode = ""
    async function getSharecode(){
        sharecode = await APIs.getSharecode(deckId)
    }
    let inputCode = ""
    let recieveCodeResult = false
    async function recieveShareCode(){
        recieveCodeResult = await APIs.recieveSharecode(deckId)
    }
</script>

<p>sharecode = {sharecode}</p>
<input type="button" value="get share code!" on:click={getSharecode}>
<p>recieveCodeResult = {recieveCodeResult}</p>
enter code = <input type="text" bind:value={inputCode}> <br>
<input type="button" value="Recieve share code!" on:click={recieveShareCode}>