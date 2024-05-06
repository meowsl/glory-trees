<template>
  <q-page class="row items-center justify-evenly">
    <BannerApp />
    <CarouselApp />
    <AboutApp />
    <TreesMap />
    <SoldierApp />
    <!-- <TeamApp /> -->
  </q-page>
</template>

<script setup lang="ts">
import BannerApp from 'src/components/BannerApp.vue';
import CarouselApp from 'src/components/CarouselApp.vue';
import AboutApp from 'src/components/AboutApp.vue';
import TreesMap from 'src/components/TreesMap.vue';
import SoldierApp from 'src/components/SoldierApp.vue';
// import TeamApp from 'src/components/TeamApp.vue';
</script>
