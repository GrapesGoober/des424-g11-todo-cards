<script>
    export let cardDue
    let today = new Date()
    let year = today.getFullYear()
    let month = String(today.getMonth() + 1).padStart(2, '0') // Month is zero-based, so we add 1 and pad with '0' if necessary
    let day = String(today.getDate()).padStart(2, '0')
    let todayString = `${year}-${month}-${day}`

    let formattedDate
    $ : {
        let cardDue_dateObj = new Date(cardDue)
        formattedDate = new Intl.DateTimeFormat('en-US', {
            weekday: 'short',
            day: 'numeric',
            month: 'short'
        }).format(cardDue_dateObj);
    }

</script>

<span>Select Date: {formattedDate}</span> <br>
<input type="date" id="datepicker" min={todayString} bind:value={cardDue}>