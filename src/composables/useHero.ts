import { api } from 'boot/axios'
import { Hero } from 'src/models/hero'

export function useHero() {

  const getHeroList = () => {
    const response = api.get<Hero[]>('heroes/list')
    return response
  }

  const getHero = (id: number) => {
    const response = api.get<Hero>(`heroes/${id}`)
    return response
  }

  const uploadHero = async (formData: FormData) => {
    const response = await api.post('heroes/applications/create', formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    })
    return response
  }

  return {
    getHeroList,
    getHero,
    uploadHero
  }
}
