import { PGService } from '@/src/_lib/db/pg.service'

export type RankPropertiesType = {
    Rank: string[]
    History: number[][]
    Move: number[][]
}
export type ReturnSuccessType = {
    status: true
    data: {
        id: string
        date: string
        day: RankPropertiesType
        dayone: RankPropertiesType
        daytwo: RankPropertiesType
        daythree: RankPropertiesType
        weekone: RankPropertiesType
        weektwo: RankPropertiesType
        createdat: string
    }
}


type ReturnErrorType = {
    status: false
    message: string
}

export const getByDate = async (
    date: string
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            rank_under as ru
        WHERE
            ru.Date = $1
    `
    const values = [date]
    const r = await pgService.getOne(query, values)

    return (r === false)
    ? {
        status: false,
        message: 'Error'
    } : {
        status: true,
        data: toObject(r)
    }
}


export const getByLatest = async (
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            rank_under as ru
        ORDER BY
            ru.Date DESC
        LIMIT 1
    `
    const r = await pgService.getOne(query, [])
    return (r === false) ? {
        status: false,
        message: 'Error'
    } : {
        status: true,
        data: toObject(r)
    }
}

const toObject = (r: any) => {
    return {
        id: r.id,
        date: r.date,
        day: JSON.parse(r.day),
        dayone: JSON.parse(r.dayone),
        daytwo: JSON.parse(r.daytwo),
        daythree: JSON.parse(r.daythree),
        weekone: JSON.parse(r.weekone),
        weektwo: JSON.parse(r.weektwo),
        createdat: r.createdat
    }
}