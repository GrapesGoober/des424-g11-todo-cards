<script>
    import * as APIs from "$lib"
    
    let deckslist = [] // output of the fetch goes into this list
    async function getDeckslist(){
        deckslist = await APIs.getDeckslist()
    }

</script>

deckslist = {JSON.stringify(deckslist)} <br>
<input type="button" value="get decks list!" on:click={getDeckslist}>