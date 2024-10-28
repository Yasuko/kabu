'use server'

import {
    getByLatest as HistoryLatest,
} from '@/src/model/history.date.model'


export const getHistoryAction = async (
    companyCode: string,
): Promise<any> => {
    const r = await HistoryLatest(companyCode, 10)

    if (r.status === false) {
        return []
    }
    
    return r
}

