'use server'

import {
    getByLatest as HistoryLatest,
} from '@/src/model/history.date.model'

import {
    getByLatest as UpperRank
} from '@/src/model/rank.model'
import {
    getByLatest as LowerRank
} from '@/src/model/rank_under.model'


import {
    convert_pressure
} from '@/src/_helper/analysis'


export const getHistoryAction = async (
    companyCode: string,
): Promise<any> => {
    const r = await HistoryLatest(companyCode, 10)

    if (r.status === false) {
        return []
    }
    
    return r
}

