<template>
  <div
    class="banner unit parallax column flex-center justify-center items-center"
    ref="parallaxElement"
    @wheel.prevent="handleScroll"
  >
    <p class="banner__title text-white text-uppercase">Деревья славы</p>
    <p class="banner__subtitle text-white text-subtitle2 text-uppercase">Проект амбассадоров "Цифровой Прорыв. Сезон:
      Искусственный Интеллект"
      совместно с РГЭУ
      (РИНХ)</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const parallaxElement = ref<HTMLElement | null>(null);
let maxSizeReached = false;
let scrollPosition = 0;

function handleScroll(event: WheelEvent) {
  if (!maxSizeReached) {
    event.preventDefault();
    scrollPosition += event.deltaY;
    updateParallax();
  } else {
    window.scrollBy(0, event.deltaY);
  }
}

function updateParallax() {
  if (parallaxElement.value) {
    const maxScroll = parallaxElement.value.clientHeight;
    const scrollPercent = scrollPosition / maxScroll;
    const minSize = 25;
    const maxSize = 60;
    let size = minSize + (maxSize - minSize) * scrollPercent;

    size = Math.min(size, maxSize);

    parallaxElement.value.style.backgroundSize = `${size}% auto`;

    if (size >= maxSize) {
      maxSizeReached = true;
    }
  }
}

onMounted(() => {
  window.addEventListener('scroll', updateParallax);
});

</script>