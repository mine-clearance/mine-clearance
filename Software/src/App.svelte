<script lang="ts">
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import Popup from "./lib/Popup.svelte";
  import NavBar from "./lib/NavBar.svelte";
  import "./app.css";
  import "leaflet/dist/leaflet.css";
  import "leaflet-draw/dist/leaflet.draw.css";
  import "leaflet-extra-markers/dist/css/leaflet.extra-markers.min.css";
  import L from "leaflet";
  import "leaflet-draw";
  import "leaflet-extra-markers";

  import { drone, mines, searchZone, selectedMine } from "./store/store.js";

  // Popup error state
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

  window.addEventListener("online", checkConnection);
  window.addEventListener("offline", checkConnection);

  let map;
  let droneMarker = null;
  let drawnItems = new L.FeatureGroup();
  let drawControl;
  let coor;
  let listOfCoor = [
    { lat: 48.866667, lng: 2.333333 },
    { lat: 48.8566, lng: 2.3522 },
    { lat: 48.8567, lng: 2.3518 },
  ];

  // Functions for drawing management
  function startDrawing() {
    new L.Draw.Polygon(map, drawControl.options.draw.polygon).enable();
  }

  function deleteDrawings() {
    drawnItems.clearLayers();
  }

  onMount(() => {
    try {
      setInterval(() => {
        $drone.infos.location.lat += Math.random() * 0.001;
        $drone.infos.location.lng += Math.random() * 0.001;
      }, 1000);

      checkConnection();

      // Initialize map
      map = L.map("map").setView([48.866667, 2.333333], 13);
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);
      map.addLayer(drawnItems);

      drawControl = new L.Control.Draw({
        edit: { featureGroup: drawnItems },
        draw: {
          polygon: true,
          polyline: false,
          rectangle: true,
          circle: false,
          marker: false,
        },
      });
      map.addControl(drawControl);

      map.on(L.Draw.Event.CREATED, function (event) {
        var layer = event.layer;
        drawnItems.addLayer(layer);
        searchZone.set(layer.getLatLngs());
      });

      // Initialize drone marker
      droneMarker = L.marker(
        [$drone.infos.location.lat, $drone.infos.location.lng],
        {
          icon: L.ExtraMarkers.icon({
            icon: "fa-drone",
            markerColor: "blue",
          }),
        }
      ).addTo(map);

      $mines.forEach((mine, index) => {
        let marker = L.marker([mine.location.lat, mine.location.lng], {
          icon: L.ExtraMarkers.icon({
            icon: "fa-number",
            number: mine.id,
            markerColor:
              mine.status === "arm"
                ? "red"
                : mine.status === "disarm"
                  ? "green"
                  : "orange",
          }),
        }).addTo(map);
        marker.on("click", () => {
          selectedMine.set(mine);
          console.log($selectedMine);
        });
      });
    } catch (error) {
      console.error("Une erreur s'est produite:", error);
      problemMessage.set(error.message);
      problemTitle.set("Erreur");
      problemExists.set(true);
    }
  });

  // update the drone position
  $: if ($drone && droneMarker) {
    const newLatLng = new L.LatLng(
      $drone.infos.location.lat,
      $drone.infos.location.lng
    );
    droneMarker.setLatLng(newLatLng);
    // // To follow the drone
    // map.setView(newLatLng);
  }
</script>

<svelte:head>
  <title>Mine Clearance</title>
</svelte:head>

<main class="container">
  {#if $problemExists}
    <Popup show={true} title={$problemTitle} message={$problemMessage} />
  {/if}

  <div id="map"></div>

  <NavBar isOnline={true} {startDrawing} {deleteDrawings} />
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

  :global(.leaflet-marker-pane > *) {
  -webkit-transition: transform .3s linear;
  -moz-transition: transform .3s linear;
  -o-transition: transform .3s linear;
  -ms-transition: transform .3s linear;
  transition: transform .3s linear;
  }
</style>
