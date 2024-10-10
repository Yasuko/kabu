import { PGService } from '@/src/_lib/db/pg.service'

export const getPressureByDay = async (
    date: string,
    limit: number = 10
) => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            analysis_date as a
        WHERE
            a.date = $1
        ORDER BY
            a.pressday DESC
        LIMIT $2
    `
    const values = [date]
    const r = await pgService.getMany(query, values)
    return r
}

export const getPressureByDayOne = async (
    date: string,
    limit: number = 10
) => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            analysis_date as a
        WHERE
            a.Date = $1
        ORDER BY
            a.pressone DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}

export const getPressureByDayTwo = async (
    date: string,
    limit: number = 10
) => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            analysis_date as a
        WHERE
            a.Date = $1
        ORDER BY
            a.presstwo DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}

export const getPressureByDayThree = async (
    date: string,
    limit: number = 10
) => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            analysis_date as a
        WHERE
            a.Date = $1
        ORDER BY
            a.pressthree DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}

export const getPressureByWeekOne = async (
    date: string,
    limit: number = 10
) => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            analysis_date as a
        WHERE
            a.Date = $1
        ORDER BY
            a.pressweekone DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}

export const getPressureByWeekTwo = async (
    date: string,
    limit: number = 10
) => {
    const pgService = PGService.call()
    const query = `
        SELECT
            *
        FROM
            analysis_date as a
        WHERE
            a.Date = $1
        ORDER BY
            a.pressweektwo DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}