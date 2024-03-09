<script>
  import { ChevronUpIcon, ChevronDownIcon } from "svelte-feather-icons";
  import { afterUpdate } from "svelte";
  import { selectedMine } from "../store/store.js";

  export let id;
  export let status;
  export let type;
  export let location;
  export let distance;
  let expanded = false;
  let element;

  $: {
    if ($selectedMine?.id == id) {
      expanded = true;
    } else {
      expanded = false;
    }
    afterUpdate(() => {
      if (element) element.focus();
    });
  }

  function toggleExpand() {
    expanded = !expanded;
  }
</script>

<div
  class="p-4 max-w-sm bg-blue-800 rounded-lg border-gray-200 shadow-md"
  on:click={toggleExpand}
>
  <div class="flex justify-between items-center mb-2">
    <h5 class="text-xl font-bold leading-none text-white">Mine {id}</h5>
    {#if status === "arm"}
      <span class="text-white-500 bg-red-400 py-1 px-2 rounded-lg">Arm</span>
    {:else if status === "disarm"}
      <span class="text-white-500 bg-green-400 py-1 px-2 rounded-lg"
        >Disarm</span
      >
    {:else if status === "ongoing"}
      <span class="text-white-500 bg-orange-400 py-1 px-2 rounded-lg"
        >On going</span
      >
    {/if}
    <button class="text-white">
      {#if expanded}
        <ChevronUpIcon size="22" />
      {:else}
        <ChevronDownIcon size="22" />
      {/if}
    </button>
  </div>
  <div class={`flex items-center ${expanded ? "" : "hidden"}`}>
    <div class="text-sm text-white-400">
      <div>Type: {type}</div>
      <div>Location: {location}</div>
      <div>Distance: {distance}</div>
    </div>
  </div>
</div>
