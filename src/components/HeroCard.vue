<template>
  <div class="hero-card">
    <div class="hero-card__header row justify-center text-subtitle2 items-center q-pa-sm">
      <div class="title row items-center">
        <img
          class="title mark"
          :src="hero.event === 1 ? GpwStar : SvoZ"
          alt=""
        >
        <p class="text-center title text">{{ hero.event === 1 ? 'Герой ВОВ' : 'Герой СВО' }}</p>
      </div>
      <div class="close-action">
        <button
          class="close-action button row justify-center items-center"
          @click="close"
        >
          <img
            :src="CloseIcon"
            alt="Закрыть"
          >
        </button>
      </div>
    </div>
    <div class="hero-card__content column text-white">
      <div class="row">
        <div class="content photo">
          <img
            :src="hero.photo"
            :alt="hero.firstname"
          >
        </div>
        <div class="content info">
          <div class="info fullname">
            {{ hero.lastname }} {{ hero.firstname }} {{ hero.lastname }}, {{ hero.birthday }} - {{ hero.deathdate }}
          </div>
          <div class="infor birth-place text-subtitle2">
            Место рождения: {{ hero.birthPlace }}
          </div>
          <div class="info__rank q-mt-sm text-subtitle2">
            Звание: {{ hero.rank ? hero.rank : 'неизвестно' }}
          </div>
        </div>
      </div>
      <div class="hero-card__feat q-mt-sm text-subtitle2">
        {{ hero.feat }}
      </div>
      <div
        class="hero-buttons"
        v-if="heroes.length > 1"
      >
        <button
          :disabled="heroIndex === 0"
          @click="heroIndex--"
        >
          Предыдущий
        </button>
        <button
          :disabled="heroIndex === heroes.length - 1"
          @click="heroIndex++"
        >
          Следующий
        </button>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { defineProps, ref, PropType } from 'vue';
import { Hero } from 'models';
import GpwStar from "images/gpw_star.svg"
import SvoZ from "images/svo_z.svg"
import CloseIcon from "images/close_icon.svg"

const props = defineProps({
  hero: {
    type: Object as PropType<Hero>,
    required: true,
  },
  heroes: {
    type: Array as PropType<Hero[]>,
    required: true,
  },
});

const heroIndex = ref(0);

</script>