import { PGService } from '@/src/_lib/db/pg.service'

type ReturnSuccessType = {
    status: true
    data: {
        id: string
        companyCode: string
        address1: string
        address2: string
        city: string
        zip: string
        country: string
        phone: string
        website: string
        industry: string
        industryKey: string
        industryDisp: string
        sector: string
        sectorKey: string
        sectorDisp: string
        longbusinessummary: string
        fullTimeEmployees: number
        createdAt: string
    }[]
}

type ReturnErrorType = {
    status: false
    message: string
}

export const getNameAll = async (
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
