import { writable } from "svelte/store";

export const mines = writable([
  {
    id: "1",
    status: "disarm",
    type: "Anti-personnel",
    location: { lat: 48.876288, lng: 2.333822 },
    distance: "100m",
  },
  {
    id: "2",
    status: "arm",
    type: "Anti-tank",
    location: { lat: 48.877417, lng: 2.368841 },
    distance: "200m",
  },
  {
    id: "3",
    status: "ongoing",
    type: "Anti-personnel",
    location: { lat: 48.887577, lng: 2.36824 },
    distance: "300m",
  },
]);

export const searchZone = writable([]);

export const selectedMine = writable(null);
