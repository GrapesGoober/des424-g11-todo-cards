<script>
    import * as APIs from "$lib"

    let status = false
    let subcardInfo = {
        subcardId:      1,
        subcardName:    "Write introduction",
    }
    async function editSubcard(){
        // recieve the result
        status = await APIs.editSubcard(subcardInfo)
    }

</script>

status = {status} <br>
<input type="text" placeholder="subcardId" bind:value={subcardInfo.subcardId}> <br>
<input type="text" placeholder="subcardName" bind:value={subcardInfo.subcardName}> <br>
<input type="button" value="submit" on:click={editSubcard}>