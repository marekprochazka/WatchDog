import type { IBaseUser } from '@/types/auth'

interface IHelloProps  {
  msg: string
}

interface INewComponentProps{
    hello: string
}

interface IUsersListProps {
    users: IBaseUser[]
}

export type { IHelloProps, INewComponentProps, IUsersListProps }