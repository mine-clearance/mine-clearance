<script lang="ts">
  import Popup from './lib/Popup.svelte';
  import "./app.css";
</script>

<main class="container">
  <h1>Welcome to Tauri!</h1>

  <div class="row">
    <a href="https://svelte.dev" target="_blank">
      <img src="/svelte.svg" class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>

  <Popup show={true} title={"Danger"} message={"Altitude basse veuillez reprendre le contrôle"}/>

</main>

<style>
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00);
  }
</style>