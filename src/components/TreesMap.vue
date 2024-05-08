<template>
  <div class="q-pa-lg unit">
    <div
      ref="map"
      class="map"
    ></div>
    <p class="map__sources text-white text-subtitle2 q-mt-lg">Источники:</p>
    <div class="row sources links text-white text-subtitle2 q-mt-sm justify-start">
      <a
        class="q-pr-md"
        href="https://mpomos.ru/heroes"
        target="_blank"
      >
        <p>mpomos.ru/heroes</p>
      </a>
      <a
        class="q-pr-md"
        href="https://pamyat-naroda.ru/"
        target="_blank"
      >
        <p>pamyat-naroda.ru</p>
      </a>
      <a
        class="q-pr-md"
        href="https://warheroes.ru/"
        target="_blank"
      >
        <p>warheroes.ru</p>
      </a>
      <a
        class="q-pr-md"
        href="https://poisk.re/"
        target="_blank"
      >
        <p>poisk.re</p>
      </a>
      <a
        class="q-pr-md"
        href="https://znanierussia.ru/articles/"
        target="_blank"
      >
        <p>znanierussia.ru</p>
      </a>
      <a
        class="q-pr-md"
        href="https://героиспецоперации.рф/"
        target="_blank"
      >
        <p>героиспецоперации.рф</p>
      </a>
      <a
        class="q-pr-md"
        href="https://герои-сво.рф/"
        target="_blank"
      >
        <p>герои-сво.рф</p>
      </a>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import { useHero } from 'composables';
import { Hero } from 'models';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import GpwMark from "images/gpw_mark.png"
import SvoMark from "images/svo_mark.png"
import CloseIcon from "images/close_icon.svg"
import GpwStar from "images/gpw_star.svg"
import SvoZ from "images/svo_z.svg"

const { getHeroList } = useHero()

const map = ref();
const heroes = ref<Hero[]>([])

const getData = async () => {
  getHeroList().then((response) => {
    heroes.value = response.data;
    initMap();
  });
};

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
    return { lon, lat };
  } else {
    return null;
  }
}

async function initMap() {
  const tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

  const mapInstance = L.map(map.value, {
    center: [55.751244, 37.618423], // Координаты Москвы
    zoom: 10,
    layers: [tileLayer]
  });

  const customIcons = {
    gpw: new L.Icon({ iconUrl: GpwMark, iconSize: [25, 41], iconAnchor: [12, 41] }),
    svo: new L.Icon({ iconUrl: SvoMark, iconSize: [25, 41], iconAnchor: [12, 41] })
  };

  const popupContainer = document.createElement('div');
  popupContainer.className = 'custom-popup-container';
  mapInstance.getContainer().appendChild(popupContainer);

  function closePopup() {
    popupContainer.style.display = 'none';
  }

  for (const hero of heroes.value) {
    try {
      const coordinates = await geocodeAddress(hero.gravePlace);
      if (coordinates) {
        const marker = L.marker([coordinates.lat, coordinates.lon]);

        if (hero.event === 1) {
          marker.setIcon(customIcons.gpw);
        } else if (hero.event === 2) {
          marker.setIcon(customIcons.svo);
        }

        const closeButton = document.createElement('button');
        closeButton.className = 'custom-popup-close-button';
        closeButton.innerHTML = `<img src="${CloseIcon}" alt="Close">`;
        closeButton.addEventListener('click', closePopup);

        const popupContent = `
        <div class="popup-container">
        <div class="popup-header row justify-center text-subtitle2 items-center q-pa-sm">
          <div class="popup-title row items-center">
            <img src="${hero.event === 1 ? GpwStar : SvoZ}" class="popup-title__star q-px-sm">
        <p class="text-center">${hero.event === 1 ? 'Герой ВОВ' : 'Герой СВО'}</p>
            </div>
          <div class="custom-popup-close-button-container">
            <button class="custom-popup-close-button row justify-center items-center"><img src="${CloseIcon}" alt="Close"></button>
          </div>
        </div>
          <div class="popup-content column text-white">
            <div class="row">
              <div class="popup-image">
                <img src="${hero.photo}" alt="${hero.firstname}">
              </div>
              <div class="popup-info">
                <div class="popup-name">${hero.lastname} ${hero.firstname} ${hero.midname}, ${hero.birthday} - ${hero.deathdate}</div>
                <div class="popup-birth text-subtitle2">Место рождения: ${hero.birthPlace}</div>
                <div class="popup-rank q-mt-sm text-subtitle2">
                  Звание: ${hero.rank}
                </div>
              </div>
            </div>
            <div class="popup-feat q-mt-sm text-subtitle2">
              ${hero.feat}
            </div>
          </div>
        </div>
        `;

        marker.on('click', () => {
          popupContainer.innerHTML = popupContent;
          popupContainer.style.display = 'block';
          popupContainer.style.top = '10px';
          popupContainer.style.left = '10px';
          const closeButtonInPopup = popupContainer.querySelector('.custom-popup-close-button');
          if (closeButtonInPopup) {
            closeButtonInPopup.addEventListener('click', closePopup);
          }
        });
        marker.addTo(mapInstance);
      }
    } catch (error) {
      console.error(error);
    }
  }
}

onMounted(() => {
  getData()
})
</script>