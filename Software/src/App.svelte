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

      var map = L.map('map').setView([2.3473316760187686, 48.85460958306098], 25);

      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);

      L.marker([51.5, -0.09]).addTo(map)
        .bindPopup('A pretty CSS popup.<br> Easily customizable.')
        .openPopup();

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
#map {
    height: 100vh; /* ou une valeur spécifique en pixels */
    width: 100%;
}
</style>