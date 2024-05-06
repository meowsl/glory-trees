<template>
  <div class="q-pa-xl unit">
    <div
      ref="map"
      class="map"
    ></div>
    <p class="text-white text-subtitle2 q-mt-lg">какой-то текст про источники информации какой-то текст про источники
      информации
      какой-то текст
      про источники
      информациикакой-то текст про источники информациикакой-то текст про источники информации какой-то текст про
      источники информациикакой-то текст про источники информации</p>
    <div
      v-for="hero in heroes"
      :key="hero?.id"
    >
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import { useHero } from 'composables';
import { Hero } from 'models';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const { getHeroList } = useHero()

const map = ref(null);
const heroes = ref<Hero[]>([])

const getData = async () => {
  getHeroList().then((response) => {
    heroes.value = response.data
  })
}

onMounted(() => {
  getData()
  initMap()
})

function initMap() {
  console.log(heroes.value)
  const tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png')

  const mapInstance = L.map(map.value, {
    center: [56.847889, 60.612222],
    zoom: 4,
    layers: [tileLayer]
  });

}

</script>