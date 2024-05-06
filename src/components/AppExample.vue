<template>
  <div
    ref="map"
    class="map"
  ></div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const map = ref(null);

onMounted(() => {
  initMap();
});

function initMap() {
  const tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

  const mapInstance = L.map(map.value, {
    center: [56.847889, 60.612222], // Координаты центра России
    zoom: 4,
    layers: [tileLayer]
  });

  const customMarker = L.marker([56.847889, 60.612222]).addTo(mapInstance);
}
</script>

<style scoped>
.map {
  width: 100%;
  height: 90vh;
}
</style>
