export interface Hero {
  id?: number
  event: number | string
  firstname?: string
  lastname?: string
  midname?: string | undefined
  photo: File | undefined
  birthday: string | Date
  birthPlace: string
  deathdate: string | Date
  gravePlace: string
  rank: string
  feat: Text | undefined
}