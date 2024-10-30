'use server'

import {
    getByLatest as HistoryLatest,
} from '@/src/model/history.date.model'

import {
    SortHistoryData
} from '@/src/domain/history/_helper/helper'

export const getHistoryAction = async (
    key: string
): Promise<any> => {
    const p = key.split('/')
    if (p.length !== 3) return
    
    const companyCode = p[1]
    const limit = (typeof p[2] === 'string') ? Number(p[2]) : 30

    const r = await HistoryLatest(companyCode, limit)

    if (r.status === false) {
        return []
    }
    // console.log('getHistoryAction', r.data)
    
    return SortHistoryData(r.data)
}

