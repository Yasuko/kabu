import { PGService } from '@/src/_lib/db/pg.service'

type ReturnSuccessType = {
    status: true
    data: any
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
            rank as r
        WHERE
            r.Date = $1
    `
    const values = [date]
    const r = await pgService.getOne(query, values)
    return (r === false) ? {
        status: false,
        message: 'Error'
    } : {
        status: true,
        data: r
    }
}


export const getByLatest = async (

): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            rank as r
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
        data: r
    }
}
