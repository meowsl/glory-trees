<template>
  <div class="quiz unit q-pa-lg">
    <div class="row">
      <div class="col-12">
        <p class="quiz__title text-white text-uppercase text-center">Что вы знаете о великой победе?</p>
      </div>
      <div class="col-12 col-md-6 q-mt-md q-mt-md-xl row justify-center">
        <img
          class="quiz__image"
          :src="QuizImg"
        >
      </div>
      <div class="quiz__subtitle col-12 col-md-6 q-mt-md q-mt-md-xl q-px-sm q-px-md-xl text-white">
        <p class="main-text text-uppercase">Проверьте свои знания в викторине "История Победы"</p>
        <p class="body-text q-mt-md q-mt-md-lg text-body1">Вспомните ключевые события, главные сражения и основные даты,
          биографии
          полководцев,
          фильмы и песни о Великой Отечественной войне</p>
        <div class="link-block row justify-end items-center q-mt-md q-mt-md-xl q-mr-lg">
          <p class="link-text text-body1 q-pl-md-xl">Присоединяйтесь к телеграм-боту и пройдите увлекательный квест</p>
          <a
            href="https://t.me/CP9m_bot"
            target="_blank"
          >
            <q-btn
              class="link-button"
              color="negative"
            >
              <img :src="LinkIcon">
            </q-btn>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import QuizImg from "images/quiz_img.png"
import LinkIcon from "images/link_icon.svg"
</script>