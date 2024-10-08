import { PGService } from '@/src/_lib/db/pg.service'

export const getRankByDay = async (
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
            a.Day DESC
        LIMIT $2
    `
    const values = [date]
    const r = await pgService.getMany(query, values)
    return r
}

export const getRankByDayOne = async (
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
            a.DayOne DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}

export const getRankByDayTwo = async (
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
            a.DayTwo DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}

export const getRankByDayThree = async (
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
            a.DayThree DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}

export const getRankByWeekOne = async (
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
            a.WeekOne DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}

export const getRankByWeekTwo = async (
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
            a.WeekTwo DESC
        limit $2
    `
    const values = [date, limit]
    const r = await pgService.getMany(query, values)
    return r
}