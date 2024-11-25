<script>

    import * as APIs from "$lib"

    let count = 0
    async function do_ping() {
        count = await APIs.ping()
    }

</script>

number of pings = {count} <br>
<input type="button" value="ping me!" on:click={do_ping}>