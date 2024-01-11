<script>
  import { ArrowUpIcon, ArrowDownIcon, MoveIcon, PenToolIcon } from 'svelte-feather-icons'

  export let isOnline = false;

  function downloadMaps() {
    // download les maps
  }
</script>

<nav class="fixed top-0 right-0 bg-blue bg-opacity-50 m-4 p-6 rounded">
  <h1 class="font-bold">Infos</h1>

  <div>
    <p>connection</p>
    {#if isOnline}
      <p>online</p>
    {:else}
      <p>offline</p>
    {/if}
  </div>

  <div>
    <div>Battery 90%</div>
    <div>Hauteur: 80m</div>
    <div>Vitesse: 22km</div>
    <div>Vent: 13km/h</div>
    <div>Temps de vol: 00:14</div>
  </div>
  <div class="overflow-auto h-48 my-2">
    {#each [1, 2, 3, 4, 5, 6, 7, 8, 9] as item}
      <div class="flex justify-between">
        <div>Mine {item}</div>
        <div>00:00:00</div>
      </div>
    {/each}
  </div>
  <div class="flex justify-evenly border-white mt-2 pt-2">
    {#if isOnline}
      <button class="py-2 px-4 rounded bg-" on:click={downloadMaps}
        >Download maps</button
      >
    {/if}
  </div>

  <div>
    <button class="bg-red-700 py-2 px-4 rounded">
        <ArrowUpIcon size="22" />
    </button>
    <button class="bg-red-700 py-2 px-4 rounded">
        <ArrowDownIcon size="22" />
    </button>
    <button class="bg-red-700 py-2 px-4 rounded">
        <MoveIcon size="22" />
    </button>
    <button class="bg-red-700 py-2 px-4 rounded">
        <PenToolIcon size="22" />
    </button>
  </div>
</nav>
