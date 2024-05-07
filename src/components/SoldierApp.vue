<template>
  <div class='soldier unit q-pa-lg'>
    <p class='soldier__title text-uppercase text-center'>
      Все они - чьи-то братья, отцы <br>
      или деды, с героическим именем 'Русский солдат'
    </p>
    <div class='soldier__img row justify-center q-mt-lg'>
      <img
        :src='BannerSoldier'
        class='soldier__img-image'
      >
    </div>
  </div>
</template>


<script setup lang="ts">
import BannerSoldier from "images/banner_soldier.svg"
</script>