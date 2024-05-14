<template>
  <div class="q-pa-lg unit">
    <div class="">
      <yandex-map
        :settings="{
          location: {
            center: [37.617644, 55.755819],
            zoom: 9,
          },
        }"
        width="100%"
        height="85vh"
        @ymapsready="initMap"
      >
        <yandex-map-default-scheme-layer />
        <yandex-map-default-features-layer />
        <yandex-map-marker
          v-for="(marker, index) in markers"
          :key="marker.title"
          :settings="{
            ...marker,
            onClick: () => {
              if (openMarker && openMarker.index === index) {
                openMarker = null;
                currentSlide = 0;
              } else {
                openMarker = { index, heroes: marker.heroes };
                currentSlide = 0;
              }
            },
            zIndex: openMarker && openMarker.index === index ? 1 : 0,
          }"
          position="top left-center"
        >
          <div class="custom-marker">
            <img
              class="custom-marker__image"
              :src="marker.icon"
            >
          </div>
        </yandex-map-marker>

      </yandex-map>
    </div>
    <AppPreloader :showing="isLoading" />
    <div
      class="hero-info"
      v-if="openMarker"
    >
      <div class="hero-slider">
        <div
          class="hero-slide"
          v-for="(hero, index) in openMarker.heroes"
          :key="index"
          :class="{ 'hero-slide--active': currentSlide === index }"
        >
          <HeroCard
            :hero="hero"
            @close="openMarker = null; currentSlide = 0"
          />
        </div>
        <div
          class="hero-slider__controls"
          v-if="openMarker?.heroes.length > 1"
        >
          <button
            class="hero-slider__control hero-slider__control--prev"
            @click="prevSlide"
          >
            &lt;
          </button>
          <button
            class="hero-slider__control hero-slider__control--next"
            @click="nextSlide"
          >
            &gt;
          </button>
        </div>
      </div>
    </div>
    <div class="undermap row justify-between q-mt-lg">
      <div class="map-legend">
        <p class="map__sources text-white text-subtitle1  text-bold">Источники:</p>
        <div class="row sources links text-white text-subtitle2 q-mt-sm justify-start"> <a
            class="q-pr-md"
            href="https://mpomos.ru/heroes"
            target="_blank"
          >
            <p>mpomos.ru/heroes</p>
          </a> <a
            class="q-pr-md"
            href="https://pamyat-naroda.ru/"
            target="_blank"
          >
            <p>pamyat-naroda.ru</p>
          </a> <a
            class="q-pr-md"
            href="https://warheroes.ru/"
            target="_blank"
          >
            <p>warheroes.ru</p>
          </a> <a
            class="q-pr-md"
            href="https://poisk.re/"
            target="_blank"
          >
            <p>poisk.re</p>
          </a> <a
            class="q-pr-md"
            href="https://znanierussia.ru/articles/"
            target="_blank"
          >
            <p>znanierussia.ru</p>
          </a> <a
            class="q-pr-md"
            href="https://героиспецоперации.рф/"
            target="_blank"
          >
            <p>героиспецоперации.рф</p>
          </a> <a
            class="q-pr-md"
            href="https://герои-сво.рф/"
            target="_blank"
          >
            <p>герои-сво.рф</p>
          </a>
        </div>
      </div>
      <div class="application-btn">
        <q-btn
          class="application-btn__btn text-white"
          push
          label="Добавить героя"
          @click="openApplicationForm"
        />
        <q-dialog v-model="showApplicationForm">
          <ApplicationForm @close="showApplicationForm = false" />
        </q-dialog>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { shallowRef, ref, onMounted } from 'vue';
import {
  YandexMap,
  YandexMapDefaultSchemeLayer,
  YandexMapDefaultFeaturesLayer,
  initYmaps,
  createYmapsOptions,
  YandexMapMarker,
} from 'vue-yandex-maps';
import type { LngLat } from '@yandex/ymaps3-types';
import { useHero } from 'composables';
import { Hero } from 'models';
import HeroCard from './HeroCard.vue';
import AppPreloader from './AppPreloader.vue';
import ApplicationForm from './ApplicationForm.vue';
import GpwMark from "images/gpw_mark.png"
import SvoMark from "images/svo_mark.png"

/* Переменные для функционала */
const isLoading = ref(false)
const { getHeroList } = useHero()
const showApplicationForm = ref(false);

/* Объявляем список геров */
const heroes = ref<Hero[]>([])

/* Объявлем переменные для маркеров */
const markers = shallowRef<any[]>([]);
const markersWithHeroes = shallowRef<any[]>([]);

/* Получение координат по адресу */
async function geocodeAddress(address: string | any) {
  const apiKey = 'c0d403ab-e5be-4049-908c-8122a58acf23';
  const response = await fetch(
    `https://geocode-maps.yandex.ru/1.x/?apikey=${apiKey}&geocode=${encodeURIComponent(
      address
    )}&format=json`
  );
  const data = await response.json();

  if (data.response.GeoObjectCollection.featureMember.length > 0) {
    const [lon, lat] = data.response.GeoObjectCollection.featureMember[0].GeoObject.Point.pos.split(' ');
    return [parseFloat(lon), parseFloat(lat)] as LngLat;
  } else {
    return null;
  }
}

/* Получение списка героев */
const getData = async () => {
  getHeroList().then((response) => {
    heroes.value = response.data;
    initMap();
  });
};

/* Создание карты с метками */
async function initMap() {
  const heroesByCoordinates = new Map();

  for (const hero of heroes.value) {
    try {
      const coordinates: LngLat | null = await geocodeAddress(hero.gravePlace)
      if (coordinates) {
        let markImage;
        if (hero.event === 1) {
          markImage = GpwMark;
        } else if (hero.event === 2) {
          markImage = SvoMark;
        } else {
          markImage = null;
        }
        if (heroesByCoordinates.has(coordinates.toString())) {
          heroesByCoordinates.get(coordinates.toString()).push(hero);
        } else {
          heroesByCoordinates.set(coordinates.toString(), [hero]);
          markersWithHeroes.value = [
            ...markersWithHeroes.value,
            {
              coordinates: coordinates as LngLat,
              title: hero.firstname,
              subtitle: "Test test test test",
              icon: markImage,
              heroes: heroesByCoordinates.get(coordinates.toString())
            }
          ];
        }
      }
    } catch (error) {
      console.error(error)
    }
  }
  markers.value = markersWithHeroes.value;
  isLoading.value = false
}

const openMarker = ref<null | { index: number; heroes: Hero[] }>(null)

const currentSlide = ref(0);

function prevSlide() {
  if (openMarker.value && openMarker.value.heroes) {
    currentSlide.value = (currentSlide.value - 1 + openMarker.value.heroes.length) % openMarker.value.heroes.length;
  }
}

function nextSlide() {
  if (openMarker.value && openMarker.value.heroes) {
    currentSlide.value = (currentSlide.value + 1) % openMarker.value.heroes.length;
  }
}

function openApplicationForm() {
  showApplicationForm.value = true;
}

onMounted(() => {
  isLoading.value = true
  getData();
  const options = createYmapsOptions({
    apikey: 'c0d403ab-e5be-4049-908c-8122a58acf23',
  });
  initYmaps(options);
});
</script>
