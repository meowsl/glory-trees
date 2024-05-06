<template>
  <div class="carousel unit">
    <div
      ref="track"
      class="carousel__track"
      :style="{ transform: `translateX(-${slidePosition}px)`, transition: `transform ${slideDuration}s linear` }"
    >
      <div
        class="carousel__slide"
        v-for="(slide, index) in slides"
        :key="index"
      >
        <div class="card">
          <img
            :src="`src/assets/images/carousel/${slide}.png`"
            :alt="slide"
          >
        </div>
      </div>
      <div
        class="carousel__slide"
        v-for="(slide, index) in slides"
        :key="slides.length + index"
      >
        <div class="card">
          <img
            :src="`src/assets/images/carousel/${slide}.png`"
            :alt="slide"
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue';

const track = ref<HTMLElement | null>(null);
const slidePosition = ref(0);
const slideDuration = ref(5); // Длительность анимации прокрутки в секундах
const slides = ['photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', 'photo7', 'photo8'];

onMounted(async () => {
  await nextTick();
  const slide = document.querySelector('.carousel__slide') as HTMLElement;
  const slideWidthValue = slide.clientWidth + 10; // Добавляем 10 пикселей для расстояния между слайдами
  const trackWidthValue = track.value?.clientWidth ?? 0;

  slideWidth.value = slideWidthValue;
  slideCount.value = Math.ceil(trackWidthValue / slideWidthValue);

  startScrollAnimation();
});


const slideWidth = ref(0);
const slideCount = ref(0);

let scrollInterval: number | undefined;

function startScrollAnimation() {
  scrollInterval = window.setInterval(() => {
    slidePosition.value += 1;
  }, 20); // Интервал обновления анимации в миллисекундах
}
</script>