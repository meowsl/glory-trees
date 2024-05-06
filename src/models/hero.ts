export interface Hero {
  id?: number
  firstname?: string
  lastname?: string
  midname?: string | undefined
  photo: File | undefined
  birthday: string | Date
  deathdate: string | Date
  gravePlace: string | undefined
}