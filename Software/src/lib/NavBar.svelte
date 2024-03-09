<script>
  import {
    ArrowUpIcon,
    ArrowDownIcon,
    DeleteIcon,
    PenToolIcon,
  } from "svelte-feather-icons";
  import Mine from "./Mine.svelte";
  import { mines } from "../store/store.js";

  export let isOnline = false;
  export let startDrawing;
  export let deleteDrawings;

  function downloadMaps() {
    // download les maps
  }
</script>

<nav class="fixed top-0 right-0 bg-blue m-4 p-6 rounded">
  <h1 class="font-bold text-indigo-500">Infos</h1>

  <div class="text-left">
    <p>connection</p>
    {#if isOnline}
      <p>online</p>
    {:else}
      <p>offline</p>
    {/if}
  </div>

  <div class="text-left">
    <div>Battery 90%</div>
    <div>Hauteur: 80m</div>
    <div>Vitesse: 22km</div>
    <div>Vent: 13km/h</div>
    <div>Temps de vol: 00:14</div>
  </div>

  <div class="overflow-auto h-80 my-4">
    {#each $mines as mine}
      <Mine {...mine} />
    {/each}
  </div>

  <div class="flex justify-evenly border-white my-4 pt-2">
    {#if isOnline}
      <button class="py-2 px-4 rounded bg-cyan-900" on:click={downloadMaps}
        >Download maps</button
      >
    {/if}
  </div>

  <div class="mt-6">
    <button class="bg-red-700 py-2 px-4 rounded">
      <ArrowUpIcon size="22" />
    </button>
    <button class="bg-red-700 py-2 px-4 rounded">
      <ArrowDownIcon size="22" />
    </button>
    <button class="bg-red-700 py-2 px-4 rounded" on:click={startDrawing}>
      <PenToolIcon size="22" />
    </button>
    <button class="bg-red-700 py-2 px-4 rounded" on:click={deleteDrawings}>
      <DeleteIcon size="22" />
    </button>
  </div>
</nav>
