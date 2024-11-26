<script>
    import CardTemplate from "./CardTemplate.svelte";
    import DeckTemplate from "./DeckTemplate.svelte";
    import PingTemplate from "./PingTemplate.svelte";
    import UserTemplate from "./UserTemplate.svelte";
    import FinishItemsTemplate from "./FinishItemsTemplate.svelte";
    import EditCardTemplate from "./EditCardTemplate.svelte";
    import EditDeckTemplate from "./EditDeckTemplate.svelte";
    import EditSubcardTemplate from "./EditSubcardTemplate.svelte";
    import SharecodeTemplate from "./SharecodeTemplate.svelte";
</script>
<link rel="apple-touch-icon" href="/custom_icon.png"/>
<h1>This is a demo for the APIs</h1>

<h2>Try pinging the server</h2>
<PingTemplate></PingTemplate>

<h2>Log in first</h2>
<UserTemplate></UserTemplate>
<h2>Get items (as list)</h2>
<DeckTemplate></DeckTemplate> <br>
<CardTemplate></CardTemplate>

<h2>Finish items</h2>
<FinishItemsTemplate></FinishItemsTemplate>

<h2>Edit some Items</h2>
<h3>Some editing card</h3>
<EditCardTemplate></EditCardTemplate>
<h3>Some editing deck</h3>
<EditDeckTemplate></EditDeckTemplate>
<h3>Some editing subcard</h3>
<EditSubcardTemplate></EditSubcardTemplate>

<h2>Share items</h2>
<SharecodeTemplate></SharecodeTemplate>