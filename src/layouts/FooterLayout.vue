<template>
  <div class="footer q-px-0 q-px-md-xl q-py-lg justify-end">
    <div class="row">
      <div class="col-none col-md-7"></div>
      <div class="col-12 col-md-5 row justify-around">
        <a
          href="https://rsv.ru"
          target="_blank"
        >
          <img :src="RSVLogo">
        </a>
        <a
          href="https://hacks-ai.ru"
          target="_blank"
        >
          <img :src="CPLogo">
        </a>
        <a
          href="https://rsue.ru"
          target="_blank"
        >
          <img :src="RSUELogo">
        </a>
      </div>

    </div>

  </div>
</template>

<script setup lang="ts">
import RSVLogo from "images/footer/rsv_logo.svg"
import CPLogo from "images/footer/cp_logo.svg"
import RSUELogo from "images/footer/rsue_logo.svg"
</script>