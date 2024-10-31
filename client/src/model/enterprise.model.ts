import { PGService } from '@/src/_lib/db/pg.service'

type ReturnSuccessType = {
    status: true
    data: {[key: string]: {
        companyCode: string
        stockName: string
    }}
}

type ReturnErrorType = {
    status: false
    message: string
}

export const getAll = async (
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            e.companyCode,
            e.stockName
        FROM
            enterprise as e
        ORDER BY
            e.companyCode
    `
    const r = await pgService.getMany(query, [])
    if (r === false)
        return {
            status: false,
            message: 'Error'
        } 
    const _r = {}
    r.map((v: any) => {
        _r[v.companyCode] = {
                companyCode: v.companyCode,
                stockName: v.stockName
            }
    })
    console.log(_r)
    return {
        status: true,
        data: _r
    }
}

