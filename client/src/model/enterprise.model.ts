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
    const _r: {[key:string]: any} = {}
    r.map((v: any) => {
        _r[v.companycode] = {
                companyCode: v.companycode,
                stockName: v.stockname
            }
    })
    return {
        status: true,
        data: _r
    }
}

