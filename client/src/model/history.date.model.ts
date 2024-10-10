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
