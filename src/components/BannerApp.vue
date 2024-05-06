<template>
  <div class="banner unit parallax column flex-center justify-center items-center">
    <p class="banner__title text-white text-uppercase">Деревья славы</p>
    <p class="banner__subtitle text-white text-subtitle2 text-uppercase ">Проект амбассадоров "Цифрового Прорыва" и РГЭУ
      (РИНХ)</p>
  </div>
</template>

<script setup lang="ts">
const parallaxElement: HTMLElement | null = document.querySelector('.parallax');

function updateParallax() {
  if (parallaxElement) {
    const scrollPosition = window.scrollY;
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = scrollPosition / maxScroll;
    const minSize = 50; // минимальный размер фонового изображения в %
    const maxSize = 70; // максимальный размер фонового изображения в %
    const size = minSize + (maxSize - minSize) * scrollPercent;

    parallaxElement.style.backgroundSize = `${size}% auto`;
  }
}

window.addEventListener('scroll', updateParallax);

// вызываем updateParallax после загрузки страницы
window.addEventListener('load', updateParallax);

</script>