'use server'

import {
    getByCompanyCode,
    getRankByDay, getRankByDayOne, getRankByDayTwo,
    getRankByDayThree, getRankByWeekOne,
    getLastDate
} from '@/src/model/analisis.candle.model'

import {
    getByBetweenDate,
} from '@/src/model/history.date.model'

import { utcToJst } from '../../_helper/date'

export const getRankAction = async (
    key: string
):Promise<any> => {
    const p = key.split('/')

    // 登録されている最新の日付を取得
    const d = await getLastDate()

    if (d.status === false) {
        return []
    }
    // timezoneをUTCからJSTに変換し、YYYY-MM-DDの形式に変換
    const _d = utcToJst(d.data.date)

    const date = _d.split(' ')[0]
    const limit = 20
    const sort = (p[2] === 'upper') ? 'up' : 'down'
    console.log('getRankAction', p[1], date, limit, sort)
    switch (p[1]) {
        case 'day':
            return getRankByDay(date, limit, sort)
        case 'dayone':
            return getRankByDayOne(date, limit, sort)
        case 'daytwo':
            return getRankByDayTwo(date, limit, sort)
        case 'daythree':
            return getRankByDayThree(date, limit, sort)
        case 'weekone':
            return getRankByWeekOne(date, limit, sort)
        default:
            return getRankByDay(date, limit, sort)
    }
}
