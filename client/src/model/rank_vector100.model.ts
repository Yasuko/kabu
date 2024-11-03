import { PGService } from '@/src/_lib/db/pg.service'

export type RankVectorPropertiesType = {
    Rank: string[]
    History: number[][]
    Move: number[][]
    Volume: number[][]
}
export type ReturnSuccessType = {
    status: true
    data: {
        id: string
        date: string
        rank: RankVectorPropertiesType
        createdat: string
    }
}

export type ReturnErrorType = {
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
            rank_vector100 as r
        WHERE
            r.Date = $1
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
            rank_vector100 as r
        ORDER BY
            r.Date DESC
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
        rank: JSON.parse(r.day),
        createdat: r.createdat
    }
}