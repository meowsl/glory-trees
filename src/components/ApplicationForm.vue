<template>
  <div class="application-form q-pa-lg">
    <q-form
      ref="form"
      @submit="handleSubmit"
    >
      <q-card class="application-form__card">
        <q-card-section class="card__title row text-center items-center justify-center">
          <p class="text-h4 text-white">Добавить героя</p>
          <div
            class="dialog-close-btn"
            @click="$emit('close')"
          >
            <img :src="CloseIcon">
          </div>>
        </q-card-section>
        <q-separator dark />
        <q-card-section class="q-mt-md">
          <div class="row q-mb-lg">
            <div class="col-12 q-px-sm">
              <q-select
                filled
                v-model="event"
                :options="selectEvent"
                hide-bottom-space
                label="Событие*"
                lazy-rules
                :rules="[val => val || 'Обязательное поле!']"
                class="bg-grey-3 text-white"
              />
            </div>
          </div>
          <div class="row q-mb-lg justify-between">
            <div class="col-12 col-md-4 q-px-sm q-mb-md q-mb-md-auto">
              <q-input
                filled
                v-model="lastname"
                hide-bottom-space
                debounce="1000"
                placeholder="Фамилия*"
                lazy-rules
                :rules="[val => val && val.length > 0 || 'Обязательное поле!']"
                class="bg-grey-3 text-white"
              />
            </div>
            <div class="col-12 col-md-4 q-px-sm q-mb-md q-mb-md-auto">
              <q-input
                filled
                v-model="firstname"
                hide-bottom-space
                debounce="1000"
                placeholder="Имя*"
                lazy-rules
                :rules="[val => val && val.length > 0 || 'Обязательное поле!']"
                class="bg-grey-3 text-white"
              />
            </div>
            <div class="col-12 col-md-4 q-px-sm">
              <q-input
                filled
                v-model="midname"
                debounce="1000"
                placeholder="Отчество"
                class="bg-grey-3 text-white"
              />
            </div>
          </div>
          <div class="row q-mb-lg">
            <div class="col-12 q-px-sm">
              <q-input
                filled
                v-model="photo"
                hide-bottom-space
                label="Выберите фото*"
                stack-label
                @update:model-value="val => { photo = val }"
                type="file"
                lazy-rules
                :rules="[(val) => !!val]"
                class="bg-grey-3 text-white"
              />
            </div>
          </div>
          <div class="row q-mb-lg">
            <div class="col-12 col-md-4 q-px-sm q-mb-md q-mb-md-auto">
              <q-input
                filled
                v-model="birthdate"
                hide-bottom-space
                mask="##.##.####"
                fill-mask="_"
                label="Дата рождения*"
                lazy-rules
                :rules="[val => val && new Date(Number(val.split('.')[2]), Number(val.split('.')[1]) - 1, Number(val.split('.')[0])) <= new Date() || 'Укажите корректную дату!']"
                class="bg-grey-3 text-white"
              ><template v-slot:append>
                  <q-icon
                    name="event"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      cover
                      transition-show="scale"
                      transition-hide="scale"
                    >
                      <q-date
                        v-model="birthdate"
                        minimal
                        mask="DD.MM.YYYY"
                        :options="val => new Date(val) <= new Date()"
                      >
                        <div class="row items-center justify-end">
                          <q-btn
                            v-close-popup
                            label="Close"
                            color="primary"
                            flat
                          />
                        </div>
                      </q-date>
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
            </div>
            <div class="col-12 col-md-8 q-px-sm">
              <q-input
                filled
                v-model="birthplace"
                hide-bottom-space
                placeholder="Место рождения*"
                lazy-rules
                :rules="[val => val && val.length > 0 || 'Обязательное поле!']"
                class="bg-grey-3 text-white"
              />
            </div>
          </div>
          <div class="row q-mb-lg">
            <div class="col-12 col-md-4 q-px-sm q-mb-md q-mb-md-auto">
              <q-input
                filled
                v-model="deathdate"
                hide-bottom-space
                mask="##.##.####"
                fill-mask="_"
                label="Дата смерти*"
                lazy-rules
                :rules="[val => val && new Date(Number(val.split('.')[2]), Number(val.split('.')[1]) - 1, Number(val.split('.')[0])) <= new Date() || 'Укажите корректную дату!']"
                class="bg-grey-3 text-white"
              ><template v-slot:append>
                  <q-icon
                    name="event"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      cover
                      transition-show="scale"
                      transition-hide="scale"
                    >
                      <q-date
                        v-model="deathdate"
                        minimal
                        mask="DD.MM.YYYY"
                        :options="val => new Date(val) <= new Date()"
                      >
                        <div class="row items-center justify-end">
                          <q-btn
                            v-close-popup
                            label="Close"
                            color="primary"
                            flat
                          />
                        </div>
                      </q-date>
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
            </div>
            <div class="col-12 col-md-8 q-px-sm ">
              <q-input
                filled
                v-model="graveplace"
                hide-bottom-space
                placeholder="Место захоронения*"
                lazy-rules
                :rules="[val => val && val.length > 0 || 'Обязательное поле!']"
                class="bg-grey-3 text-white"
              />
            </div>
          </div>
          <div class="row q-mb-md">
            <div class="col-12 col-md-4 q-mb-md q-mb-md-auto q-px-sm">
              <q-input
                filled
                v-model="rank"
                placeholder="Звание"
                class="bg-grey-3 text-white"
              />
            </div>
            <div class="col-12 col-md-8 q-px-sm">
              <q-input
                filled
                v-model="feat"
                placeholder="Описание подвига"
                class="bg-grey-3 text-white"
              />
            </div>
          </div>
        </q-card-section>
        <q-separator dark />
        <q-card-actions class="justify-center">
          <q-btn
            class="submit-button text-white q-my-sm"
            label="Добавить"
            type="submit"
          />
        </q-card-actions>
      </q-card>
      <AppPreloader :showing="isLoading" />
    </q-form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useHero } from 'composables'
import { useQuasar } from 'quasar'
import { selectEvent } from 'src/constant'
import AppPreloader from 'components/AppPreloader.vue'
import CloseIcon from "images/close_icon.svg"

const $q = useQuasar()
const { uploadHero } = useHero()

const isLoading = ref<boolean>(false)
const form = ref<HTMLFormElement>()

/* Обязательные поля */
const event = ref()
const firstname = ref<string>('')
const lastname = ref<string>('')
const photo = ref()
const birthdate = ref<string>('')
const birthplace = ref<string>('')
const deathdate = ref<string>('')
const graveplace = ref<string>('')

const requiredFields = [
  { ref: 'event', value: event.value },
  { ref: 'firstname', value: firstname.value },
  { ref: 'lastname', value: lastname.value },
  { ref: 'photo', value: photo.value },
  { ref: 'birthdate', value: birthdate.value },
  { ref: 'birthplace', value: birthplace.value },
  { ref: 'deathdate', value: deathdate.value },
  { ref: 'graveplace', value: graveplace.value }
]

/* Необязательные поля */
const midname = ref<string>('')
const rank = ref<string>('')
const feat = ref<string>('')

const handleSubmit = async () => {

  isLoading.value = true
  const formData = new FormData()
  formData.append('event', event.value.value)
  formData.append('firstname', firstname.value)
  formData.append('lastname', lastname.value)
  if (midname.value.length > 0) {
    formData.append('midname', midname.value)
  }
  formData.append('photo', photo.value['0'])
  formData.append('birthday', birthdate.value)
  formData.append('birthPlace', birthplace.value)
  formData.append('deathdate', deathdate.value)
  formData.append('gravePlace', graveplace.value)
  if (rank.value.length > 0) {
    formData.append('rank', rank.value)
  }
  if (feat.value.length > 0) {
    formData.append('feat', feat.value)
  }

  try {
    const response = await uploadHero(formData)

    if (response.status !== 201) {
      throw new Error('Ошибка при отправке заявки')
    }

    $q.notify({
      type: 'postitive',
      message: 'Заявка успешно отправлена! Ожидайте модерации.'
    })
    onReset()
  } catch (error) {
    console.error(error)
    $q.notify({
      type: 'negative',
      message: 'Ошибка при отправке заявки'
    })
  } finally {
    isLoading.value = false
  }
}

const onReset = () => {
  /* Обязательные поля */
  event.value = null
  firstname.value = ''
  lastname.value = ''
  photo.value = null
  birthdate.value = ''
  birthplace.value = ''
  deathdate.value = ''
  graveplace.value = ''

  /* Необязательные поля */
  midname.value = ''
  rank.value = ''
  feat.value = ''

  form?.value?.resetValidation()
}

</script>