<template>
  <div class="q-pa-lg unit">
    <div
      ref="map"
      class="map"
    ></div>
    <p class="map__sources text-white text-subtitle1 q-mt-lg text-bold">Источники:</p>
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
import ArrowLeft from "images/arrow-left.svg"
import ArrowRight from "images/arrow-right.svg"

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

  const heroesByCoordinates: Record<string, Hero[]> = {};

  for (const hero of heroes.value) {
    try {
      const coordinates = await geocodeAddress(hero.gravePlace);
      if (coordinates) {
        if (!heroesByCoordinates[coordinates.lat + ',' + coordinates.lon]) {
          heroesByCoordinates[coordinates.lat + ',' + coordinates.lon] = [];
        }
        heroesByCoordinates[coordinates.lat + ',' + coordinates.lon].push(hero);

        const marker = L.marker([coordinates.lat, coordinates.lon]);

        if (hero.event === 1) {
          marker.setIcon(customIcons.gpw);
        } else if (hero.event === 2) {
          marker.setIcon(customIcons.svo);
        }

        marker.on('click', () => {
          showPopup(heroesByCoordinates[coordinates.lat + ',' + coordinates.lon]);
        });
        marker.addTo(mapInstance);
      }
    } catch (error) {
      console.error(error);
    }
  }

  let currentHeroIndex = 0;

  function showPopup(heroes: Hero[]) {

    let popupContent = `
    <div class="popup-container">
      <div class="popup-header row justify-center text-subtitle2 items-center q-pa-sm">
        <div class="popup-title row items-center">
          <img src="" class="popup-title__star q-px-sm">
          <p class="text-center popup-title__text"></p>
        </div>
        <div class="custom-popup-close-button-container">
          <button class="custom-popup-close-button row justify-center items-center"><img src="${CloseIcon}" alt="Close"></button>
        </div>
      </div>
      <div class="popup-content column text-white">
  `;

    let imageSource = '';
    let titleText = '';

    if (heroes[currentHeroIndex].event === 1) {
      imageSource = GpwStar;
      titleText = 'Герой ВОВ';
    } else if (heroes[currentHeroIndex].event === 2) {
      imageSource = SvoZ;
      titleText = 'Герой СВО';
    }

    popupContent += `
    <div class="popup-card">
      <div class="row">
        <div class="popup-image">
          <img src="${heroes[currentHeroIndex].photo}" alt="${heroes[currentHeroIndex].firstname}">
        </div>
        <div class="popup-info">
          <div class="popup-name">${heroes[currentHeroIndex].lastname} ${heroes[currentHeroIndex].firstname} ${heroes[currentHeroIndex].midname}, ${heroes[currentHeroIndex].birthday} - ${heroes[currentHeroIndex].deathdate}</div>
          <div class="popup-birth text-subtitle2">Место рождения: ${heroes[currentHeroIndex].birthPlace}</div>
          <div class="popup-rank q-mt-sm text-subtitle2">
            Звание: ${heroes[currentHeroIndex].rank ? heroes[currentHeroIndex].rank : 'неизвестно'}
          </div>
        </div>
      </div>
      <div class="popup-feat q-mt-sm text-subtitle2">
        ${heroes[currentHeroIndex].feat}
      </div>
    </div>
  `;

    let navigationButtons = '';

    if (heroes.length > 1) {
      navigationButtons = `
        <div class="custom-popup-navigation row justify-between">
          <button class="custom-popup-prev-button"><img class="custom-popup-prev-button__image" src="${ArrowLeft}" alt="Предыдущий"></button>
          <button class="custom-popup-next-button"><img class="custom-popup-next-button__image" src="${ArrowRight}" alt="Следующий"></button>
        </div>
      `;
    }

    popupContent += `
        ${navigationButtons}
      </div>
    </div>
    `;

    popupContainer.innerHTML = popupContent;
    popupContainer.style.display = 'block';
    popupContainer.style.top = '10px';
    popupContainer.style.left = '10px';

    const closeButtonInPopup = popupContainer.querySelector('.custom-popup-close-button');
    if (closeButtonInPopup) {
      closeButtonInPopup.addEventListener('click', closePopup);
    }

    if (heroes.length > 1) {
      const prevButton = popupContainer.querySelector('.custom-popup-prev-button');
      const nextButton = popupContainer.querySelector('.custom-popup-next-button');

      if (prevButton && nextButton) {
        prevButton.addEventListener('click', () => {
          currentHeroIndex = (currentHeroIndex - 1 + heroes.length) % heroes.length;
          updatePopupContent(heroes[currentHeroIndex]);
        });

        nextButton.addEventListener('click', () => {
          currentHeroIndex = (currentHeroIndex + 1) % heroes.length;
          updatePopupContent(heroes[currentHeroIndex]);
        });
      }
    }

    const popupTitleStar = popupContainer.querySelector('.popup-title__star') as HTMLImageElement;
    const popupTitleText = popupContainer.querySelector('.popup-title__text');

    if (popupTitleStar && popupTitleText) {
      popupTitleStar.src = imageSource;
      popupTitleText.textContent = titleText;
    }
  }

  function updatePopupContent(hero: Hero) {
    const popupImage = popupContainer.querySelector('.popup-image img') as HTMLImageElement;
    const popupName = popupContainer.querySelector('.popup-name');
    const popupBirth = popupContainer.querySelector('.popup-birth');
    const popupRank = popupContainer.querySelector('.popup-rank');
    const popupFeat = popupContainer.querySelector('.popup-feat');

    if (popupImage && popupName && popupBirth && popupRank && popupFeat) {
      let photoUrl = '';
      if (typeof hero.photo === 'string') {
        photoUrl = hero.photo;
      } else if (hero.photo instanceof File) {
        photoUrl = URL.createObjectURL(hero.photo);
      }
      popupImage.src = photoUrl;
      popupImage.alt = hero.firstname ? hero.firstname : '';
      popupName.textContent = `${hero.lastname} ${hero.firstname} ${hero.midname}, ${hero.birthday} - ${hero.deathdate} `;
      popupBirth.textContent = `Место рождения: ${hero.birthPlace} `;
      popupRank.textContent = `Звание: ${hero.rank ? hero.rank : 'неизвестно'} `;
      popupFeat.textContent = hero.feat ? hero.feat : '';
    }
  }
}

onMounted(() => {
  getData()
})
</script>