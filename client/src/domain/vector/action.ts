'use server'

import {
    getLatestDateList,
} from '@/src/model/history.date.model'

import { getByLatest as Rank50 } from '@/src/model/rank_vector50.model'
import { getByLatest as Rank100 } from '@/src/model/rank_vector100.model'

import { convDateList } from '../../_helper/date'

export const getRankVectorAction = async (

): Promise<any> => {
    const rank50 = await Rank50()
    const rank100 = await Rank100()
    const labels = await getLatestDateList('1301', 30)
    
    if (rank50.status === false || rank100.status === false || labels.status === false) {
        throw new Error('Error')
    }

    return {
        rank50: rank50.data,
        rank100: rank100.data,
        labels: convDateList(labels.data)
    }
}

