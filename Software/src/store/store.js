import { writable } from "svelte/store";

export const drone = writable({
  status: {
    wake: true,
    connection: "connected",
  },
  infos: {
    battery: 80,
    speed: 10,
    altitude: 20,
    distance: 100,
    location: { lat: 48.864716, lng: 2.349014 },
  }
})

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
    status: "disarm",
    type: "Anti-tank",
    location: { lat: 48.861288, lng: 2.350872 },
    distance: "200m",
  },
  {
    id: "3",
    status: "ongoing",
    type: "Anti-personnel",
    location: { lat: 48.887577, lng: 2.36824 },
    distance: "300m",
  },
  {
    id: "4",
    status: "disarm",
    type: "Anti-personnel",
    location: { lat: 49.876288, lng: 2.333822 },
    distance: "100m",
  },
  {
    id: "5",
    status: "disarm",
    type: "Anti-tank",
    location: { lat: 48.853524, lng: 2.369111 },
    distance: "200m",
  },
  {
    id: "6",
    status: "ongoing",
    type: "Anti-personnel",
    location: { lat: 48.877417, lng: 2.368841 },
    distance: "300m",
  },
  {
    id: "12",
    status: "disarm",
    type: "Anti-personnel",
    location: { lat: 48.895748, lng: 2.236584 },
    distance: "300m",
  },
]);

export const searchZone = writable([]);

export const selectedMine = writable(null);
