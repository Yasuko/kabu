import { PGService } from '@/src/_lib/db/pg.service'

type ReturnSuccessType = {
    status: true
    data: any
}

type ReturnErrorType = {
    status: false
    message: string
}

export const getByBeforeDate = async (
    companyCode: string,
    date: string,
    limit: number = 30
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            history_date as h
        WHERE
            h.companyCode = $1
        AND
            h.Date < $2
        ORDER BY
            h.Date DESC
        LIMIT $3
    `
    const values = [companyCode, date, limit]
    const r = await pgService.getMany(query, values)
    if (r === false) {
        return {
            status: false,
            message: 'Error'
        }
    }
    return {
        status: true,
        data: r
    }
}

export const getByLatest = async (
    companyCode: string,
    limit: number = 20
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            h.companyCode,
            h.Date,
            h.open,
            h.high,
            h.low,
            h.close,
            h.volume,
            e.stockName
        FROM
            history_date as h
            enterprise as e
        WHERE
            h.companyCode = $1
        INNER JOIN
            e.companyCode = h.companyCode
        ORDER BY
            h.Date DESC
        LIMIT $2
    `
    const values = [companyCode, limit]
    const r = await pgService.getMany(query, values)
    if (r === false) {
        return {
            status: false,
            message: 'Error'
        }
    }
    return {
        status: true,
        data: r
    }
}

export const getByBetweenDate = async (
    companyCode: string,
    startDate: string,
    endDate: string
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            history_date as h
        WHERE
            h.companyCode = $1
        AND
            h.Date >= $2
        AND
            h.Date <= $3
        ORDER BY
            h.Date DESC
    `
    const values = [companyCode, startDate, endDate]
    const r = await pgService.getMany(query, values)
    if (r === false) {
        return {
            status: false,
            message: 'Error'
        }
    }
    return {
        status: true,
        data: r
    }
}

export const getLatestDateList = async (
    companyCode: string,
    limit: number = 20
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            h.Date
        FROM
            history_date as h
        WHERE
            h.companyCode = $1
        ORDER BY
            h.Date DESC
        LIMIT $2
    `
    const values = [companyCode, limit]
    const r = await pgService.getMany(query, values)
    if (r === false)
        return {
            status: false,
            message: 'Error'
        }
    
    return {
        status: true,
        data: r
    }
}

export const getLatestHistory = async (
    companyCode: string,
    limit: number = 20
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            history_date as h
        WHERE
            h.companyCode = $1
        ORDER BY
            h.Date DESC
        LIMIT $2
    `
    const values = [companyCode, limit]
    const r = await pgService.getMany(query, values)
    if (r === false)
        return {
            status: false,
            message: 'Error'
        }
    
    return {
        status: true,
        data: r
    }
}