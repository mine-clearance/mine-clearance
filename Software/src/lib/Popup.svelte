<script>
  import { onMount } from "svelte";
  import { fly } from "svelte/transition";
  import { AlertTriangleIcon, XIcon } from 'svelte-feather-icons'
  import "../app.css";

  export let show = false;
  export let title = "title";
  export let message = "message";

  onMount(() => {
      setTimeout(() => {
          closePopup();
      }, 5000);
  });
  
  function closePopup() {
    show = false;
  }
</script>
  
{#if show}
  <div in:fly={{ y: 20, duration: 500 }} out:fly={{ y: -20, duration: 500 }}  class="fixed top-0 letf-0 bg-blue m-4 p-4 rounded">
      <div class="flex justify-between items-center">
        <div class="flex">
          <h3 class="text-lg font-bold text-red mr-4">{title}</h3>
          <div class="flex items-center">
            <AlertTriangleIcon size="22" class="text-red" />
          </div>
        </div>
        <button class="ml-4 rounded-full bg-blue-600 text-white p-1.5 leading-none" on:click={closePopup}>
          <XIcon size="22" />
        </button>
      </div>
      <p class="mt-2">{message}</p>
  </div>
{/if}

<style>
  div {
    z-index: 100;
  }
</style>