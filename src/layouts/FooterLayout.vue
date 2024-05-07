<template>
  <div class="footer q-px-xl q-pb-lg justify-end">
    <div class="row">
      <div class="col-7"></div>
      <div class="col-5 row justify-around"> <img :src="RSVLogo">
        <img :src="CPLogo">
        <img :src="RSUELogo">
      </div>

    </div>

  </div>
</template>

<script setup lang="ts">
import RSVLogo from "images/footer/rsv_logo.svg"
import CPLogo from "images/footer/cp_logo.svg"
import RSUELogo from "images/footer/rsue_logo.svg"
</script>