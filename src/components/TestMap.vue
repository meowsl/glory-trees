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
      <yandex-map-default-marker
        v-for="marker in markersGeoJsonSource"
        :key="marker.title"
        :settings="marker"
      >
      </yandex-map-default-marker>
    </yandex-map>
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
      </a> </div>
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
  YandexMapDefaultMarker,
  YandexMapMarker
} from 'vue-yandex-maps';
import type { LngLat } from '@yandex/ymaps3-types';
import { useHero } from 'composables';
import { Hero } from 'models';
import GpwMark from "images/gpw_mark.png"
import SvoMark from "images/svo_mark.png"

const { getHeroList } = useHero()

/* Объявлем переменную для получения списка героев */
const heroes = ref<Hero[]>([])

/* Объявлем переменные для маркеров */
const handleClick = (event: MouseEvent) => console.log(event);
// const markers: any[] = []
const markersGeoJsonSource = shallowRef<any[]>([]);

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
      markersGeoJsonSource.value = [
        ...markersGeoJsonSource.value,
        {
          coordinates: coordinates as LngLat,
          onClick: handleClick,
          title: "Test",
          subtitle: "Test test test test",
          icon: markImage,
        }
      ];
    } catch (error) {
      console.error(error)
    } finally {
      // console.log(markersGeoJsonSource)
    }
  }
}


onMounted(() => {
  getData();
  const options = createYmapsOptions({
    apikey: 'c0d403ab-e5be-4049-908c-8122a58acf23',
  });
  initYmaps(options);
});

</script>
