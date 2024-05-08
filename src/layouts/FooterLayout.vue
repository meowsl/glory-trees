<template>
  <div class="footer q-px-xl q-py-lg justify-end">
    <div class="row">
      <div class="footer__contact col-12 col-md-7">
        <p class="text-white">Если хотите рассказать о герое и посадить его дерево, <br>
          свяжитесь с нами по почте <a
            href="mailto:geroi@rsue.ru"
            target="_blank"
          >geroi@rsue.ru</a> </p>
      </div>
      <div class="footer__links col-12 col-md-5 row justify-around">
        <a
          href="https://www.economy.gov.ru/"
          target="_blank"
        >
          <img :src="MinLogo">
        </a>
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
import MinLogo from "images/footer/min_logo.svg"
</script>