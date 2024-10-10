'use server'

import {
    getRankByDay, getRankByDayOne, getRankByDayTwo,
    getRankByDayThree, getRankByWeekOne, getRankByWeekTwo
} from '@/src/model/analisis.date.model'

import {
    getByBeforeDate,
} from '@/src/model/history.date.model'

export const getRankAction = async (
    date: string,
    limit: number = 10,
    target: 'day' | 'dayOne' | 'dayTwo' | 'dayThree' | 'weekOne' | 'weekTwo',
) => {
    switch (target) {
        case 'day':
            return getRankByDay(date, limit)
        case 'dayOne':
            return getRankByDayOne(date, limit)
        case 'dayTwo':
            return getRankByDayTwo(date, limit)
        case 'dayThree':
            return getRankByDayThree(date, limit)
        case 'weekOne':
            return getRankByWeekOne(date, limit)
        case 'weekTwo':
            return getRankByWeekTwo(date, limit)
        default:
            return getRankByDay(date, limit)
    }
}

export const getHistoryAction = async (
    companyCode: string,
    date: string,
    limit: number = 30,
) => {
    const r = await getByBeforeDate(companyCode, date, limit)

    if (r.status === false) {
        return {
            status: false,
            message: 'Error'
        }
    }

    const open = []
    const close = []
    const high = []
    const low = []
    const volume = []

    for (let i = r.data.length; i > 0; i--) {
        open.push(r.data[i - 1].open)
        close.push(r.data[i - 1].close)
        high.push(r.data[i - 1].high)
        low.push(r.data[i - 1].low)
        volume.push(r.data[i - 1].volume)
    }

    return {
        status: true,
        data: {
            open,
            close,
            high,
            low,
            volume
        }
    }
}