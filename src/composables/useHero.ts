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

  return {
    getHeroList,
    getHero
  }
}
