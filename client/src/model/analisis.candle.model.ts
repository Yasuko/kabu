import { PGService } from '@/src/_lib/db/pg.service'

type ReturnSuccessType = {
    status: true
    data: any
}

type ReturnErrorType = {
    status: false
    message: string
}

export const getByCompanyCode = async (
    companyCode: string,
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            analysis_candle as a
        WHERE
            a.CompanyCode = $1
        ORDER BY
            a.Date DESC
        LIMIT 1
    `
    const values = [companyCode]
    const r = await pgService.getOne(query, values)
    return returnResult(r)
}

export const getRankByDay = async (
    date: string,
    limit: number = 20,
    sort: 'up' | 'down' = 'up'
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const order = (sort === 'up')
    ? `
            a.DayUp DESC,
            a.DayDown ASC,
            a.DayScore DESC
    `
    : `
            a.DayDown DESC,
            a.DayUp ASC,
            a.DayScore ASC
    `
    const query = `
        SELECT
            *
        FROM
            analysis_candle as a
        WHERE
            a.Date = $1
        ORDER BY
            ${order}
        LIMIT $2
    `
    console.log(query)
    console.log(date, limit)
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    console.log(r)
    return returnResult(r)
}

export const getRankByDayOne = async (
    date: string,
    limit: number = 20,
    sort: 'up' | 'down' = 'up'
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const order = (sort === 'up')
    ? `
            a.DayOneUp DESC,
            a.DayOneDown ASC,
            a.DayOneScore DESC
    `
    : `
            a.DayOneDown DESC,
            a.DayOneUp ASC,
            a.DayOneScore ASC
    `
    const query = `
        SELECT
            *
        FROM
            analysis_candle as a
        WHERE
            a.Date = $1
        ORDER BY
            ${order}
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    console.log(r)
    return returnResult(r)
}

export const getRankByDayTwo = async (
    date: string,
    limit: number = 20,
    sort: 'up' | 'down' = 'up'
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const order = (sort === 'up')
    ? `
            a.DayTwoUp DESC,
            a.DayTwoDown ASC,
            a.DayTwoScore DESC
    `
    : `
            a.DayTwoDown DESC,
            a.DayTwoUp ASC,
            a.DayTwoScore ASC
    `
    const query = `
        SELECT
            *
        FROM
            analysis_candle as a
        WHERE
            a.Date = $1
        ORDER BY
            ${order}
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return returnResult(r)
}

export const getRankByDayThree = async (
    date: string,
    limit: number = 10,
    sort: 'up' | 'down' = 'up'
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const order = (sort === 'up')
    ? `
            a.DayThreeUp DESC,
            a.DayThreeDown ASC,
            a.DayThreeScore DESC
    `
    : `
            a.DayThreeDown DESC,
            a.DayThreeUp ASC,
            a.DayThreeScore ASC
    `
    const query = `
        SELECT
            *
        FROM
            analysis_candle as a
        WHERE
            a.Date = $1
        ORDER BY
            ${order}
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return returnResult(r)
}

export const getRankByWeekOne = async (
    date: string,
    limit: number = 10,
    sort: 'up' | 'down' = 'up'
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const order = (sort === 'up')
    ? `
            a.WeekOneUp DESC,
            a.WeekOneDown ASC,
            a.WeekOneScore DESC
    `
    : `
            a.WeekOneDown DESC,
            a.WeekOneUp ASC,
            a.WeekOneScore ASC
    `
    const query = `
        SELECT
            *
        FROM
            analysis_candle as a
        WHERE
            a.Date = $1
        ORDER BY
            ${order}
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return returnResult(r)
}

export const getLastDate = async (
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            a.Date
        FROM
            analysis_candle as a
        ORDER BY
            a.Date DESC
        LIMIT 1
    `
    const r = await pgService.getOne(query, [])
    return returnResult(r)
}

const returnResult = (r: any): ReturnErrorType | ReturnSuccessType => {
    return (r === false) ? {
        status: false,
        message: 'Error'
    } : {
        status: true,
        data: r
    }
}