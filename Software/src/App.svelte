<script lang="ts">
  import { onMount } from "svelte";
  import { writable } from 'svelte/store';
  import Popup from './lib/Popup.svelte';
  import NavBar from "./lib/NavBar.svelte";
  import "./app.css";
  import 'leaflet/dist/leaflet.css';
  import L from 'leaflet';

  const problemExists = writable(false);
  const problemTitle = writable("");
  const problemMessage = writable("");

  const isOnline = writable(navigator.onLine);

  function checkConnection() {
    isOnline.set(navigator.onLine);
    if (!navigator.onLine) {
      problemTitle.set("Pas de connexion Internet");
      problemMessage.set("Veuillez vérifier votre connexion.");
      problemExists.set(true);
    }
  }

  window.addEventListener('online', checkConnection);
  window.addEventListener('offline', checkConnection);

  onMount(async () => {
    try {
      checkConnection();

      // paris location
      var map = L.map('map').setView([48.866667, 2.333333], 13);
      
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
            
    } catch (error) {
      if (error instanceof Error) {
        console.error("Une erreur s'est produite:", error);
        problemMessage.set(error.message);
        problemTitle.set("Erreur");
        problemExists.set(true);
      }
    }
  });
</script>

<svelte:head>
  <title>Mine Clearance</title>
</svelte:head>

<main class="container">
  {#if $problemExists}
    <Popup show={true} title={$problemTitle} message={$problemMessage}/>
  {/if}

  <div id="map"></div>

  <NavBar isOnline={true} />
</main>

<style>
:global(body, html) {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    background: black;
}

#map {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    z-index: 0;
}

:global(.leaflet-control-attribution) {
    display: none;
} 
</style>