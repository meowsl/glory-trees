<template>
  <div class="mate-card col justify-center text-center q-mr-sm">
    <img
      class="mate-card__photo"
      :src="photo"
    >
    <p class="text-white text-subtitle1">{{ name }}</p>
    <p class="text-white text-subtitle2">{{ role }}</p>
  </div>
</template>

<script setup lang="ts">
defineProps({
  photo: {
    type: String,
    required: true
  },
  name: {
    type: String,
    required: true
  },
  role: {
    type: String,
    required: true
  }
})
</script>