<template>
  <q-inner-loading class="fullscreen ">
    <img
      v-if="darkMode"
      height="60"
      src="~images/puff_light.svg"
    />
    <img
      v-else
      height="60"
      src="~images/puff_dark.svg"
    />
  </q-inner-loading>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const darkMode = ref<boolean | string>($q.dark.mode)
</script>
