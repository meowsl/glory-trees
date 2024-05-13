<template>
  <div class="q-pa-lg unit">
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
        :key="index"
        :settings="{
          ...marker,
          onClick: () => openMarker = { index, heroIndex: 0, marker },
          zIndex: openMarker && openMarker.index === index ? 1 : 0,
        }"
        :coordinates="marker.coordinates"
        position="top left-center"
      >
        <div class="custom-marker">
          <img
            class="custom-marker__image"
            :src="marker.heroes[0].event === 1 ? GpwMark : SvoMark"
          >
        </div>
      </yandex-map-marker>

    </yandex-map>
    <div
      class="hero-info"
      v-if="openMarker"
    >
      <HeroCard
        :hero="openMarker?.marker.heroes[openMarker?.heroIndex]"
        :heroes="openMarker?.marker.heroes"
        @close="openMarker = null"
      />
      <div
        class="hero-buttons"
        v-if="openMarker?.marker.heroes.length > 1"
      >
        <button
          :disabled="openMarker?.heroIndex === 0"
          @click="openMarker && openMarker.heroIndex--"
        >
          Предыдущий
        </button>
        <button
          :disabled="openMarker?.heroIndex === openMarker?.marker.heroes.length - 1"
          @click="openMarker && openMarker.heroIndex++"
        >
          Следующий
        </button>
      </div>
    </div>
    <p class="map__sources text-white text-subtitle1 q-mt-lg text-bold">Источники:</p>
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
import GpwMark from "images/gpw_mark.png"
import SvoMark from "images/svo_mark.png"
import HeroCard from './HeroCard.vue';

const { getHeroList } = useHero()

/* Объявлем переменную для получения списка героев */
const heroes = ref<Hero[]>([])

/* Объявлем переменные для маркеров */
const markers = shallowRef<Array<{ coordinates: LngLat, heroes: Hero[] }>>([]);

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
  for (const hero of heroes.value) {
    try {
      const coordinates: LngLat | null = await geocodeAddress(hero.gravePlace)
      let markImage;
      if (hero.event === 1) {
        markImage = GpwMark;
      } else if (hero.event === 2) {
        markImage = SvoMark;
      } else {
        markImage = null;
      }
      const markerIndex = markers.value.findIndex(m => m.coordinates.toString() === coordinates?.toString());
      if (markerIndex === -1) {
        markers.value.push({
          coordinates: coordinates as LngLat,
          heroes: [hero],
        });
      } else {
        markers.value[markerIndex].heroes.push(hero);
      }
    } catch (error) {
      console.error(error)
    }
  }

}

const openMarker = ref<{ index: number; heroIndex: number; marker: { coordinates: LngLat, heroes: Hero[] } } | null>(null);

onMounted(() => {
  getData();
  const options = createYmapsOptions({
    apikey: 'c0d403ab-e5be-4049-908c-8122a58acf23',
  });
  initYmaps(options);
});

</script>
