<script>
    export let showModal = false

</script>

{#if showModal}
    <div class="modal-backdrop">
        <div class="modal-box">
            <slot></slot>
        </div>
    </div>
{/if}

<style>
    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1;
    }

    .modal-box {
        background-color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        z-index: 2;
    }
</style>