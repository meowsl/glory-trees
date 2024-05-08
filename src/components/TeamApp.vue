<template>
  <div class="team unit q-pa-lg relative-position">
    <p class="team__title text-white text-uppercase text-center">Над проектом работали</p>
    <div class="row reverse q-mt-xl">
      <div class="col-12 col-md-6 col-lg-7 flex flex-first">
        <div class="row justify-end">
          <div
            class="team__card col-6 col-md-4 col-lg-3 row justify-center"
            v-for="(mate, index) in mates"
            :key="mate.name"
          >
            <MateCard
              :photo="mate.photo"
              :name="mate.name"
              :role="mate.role"
            />
            <div
              v-if="(index + 1) % 2 === 0"
              class="col-0 col-md-12 q-mt-xl q-pt-md"
            ></div>
          </div>
        </div>
      </div>
      <div class="team__list col-12 col-md-6 col-lg-5 flex flex-center flex-last">
        <ul class="text-uppercase text-white text-body1 text-center">
          <li>
            Амбассадоры "Цифровой прорыв. <br> Сезон: Искусственный Интеллект"
          </li>
          <li class="q-mt-lg">
            РГЭУ (РИНХ)
          </li>
        </ul>
      </div>
      <img
        :src="TeamBackground"
        class="team__image absolute-position"
      >
    </div>
  </div>
</template>

<script setup lang="ts">
import MateCard from "./MateCard.vue";
import TeamBackground from "images/team_background.svg"
import Olesya from "images/team/Olesya.png"
import Anton from "images/team/Anton.png"
import Galina from "images/team/Galina.png"
import Maria from "images/team/Maria.png"
import Vladislav from "images/team/Vladislav.png"
import Sergey from "images/team/Sergey.png"
import Dmitriy from "images/team/Dmitriy.png"
import Igor from "images/team/Igor.png"

const mates = [
  { photo: Olesya, name: 'Савельева Олеся', role: 'Идейный вдохновитель проекта' },
  { photo: Anton, name: 'Прохоров Антон', role: 'Куратор проектной группы РГЭУ(РИНХ)' },
  { photo: Galina, name: 'Бондаренко Галина', role: 'Координатор группы разработки РГЭУ(РИНХ)' },
  { photo: Maria, name: 'Галкина Мария', role: 'Дизайнер' },
  { photo: Vladislav, name: 'Бабушкин Владислав', role: 'Тимлид разработки' },
  { photo: Sergey, name: 'Казанцев Сергей', role: 'Бэкенд разработчик' },
  { photo: Dmitriy, name: 'Мяличкин Дмитрий', role: 'Бэкенд разработчик' },
  { photo: Igor, name: 'Швецов Игорь', role: 'Бэкенд разработчик' }
]
</script>