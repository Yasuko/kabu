'use server'

import {
    getByCompanyCode,
    getRankByDay, getRankByDayOne, getRankByDayTwo,
    getRankByDayThree, getRankByWeekOne,
    getLastDate
} from '@/src/model/analisis.candle.model'

export const getRankAction = async (
    key: string
):Promise<any> => {
    const p = key.split('/')
    console.log('getRankAction', p)
    // 登録されている最新の日付を取得
    const d = await getLastDate()

    if (d.status === false) {
        return []
    }
    // dateフォーマットからYYYY-MM-DDに変換
    const date = new Date(d.data['date']).toISOString().split('T')[0]
    const limit = 20
    const sort = (p[2] === 'upper') ? 'up' : 'down'

    switch (p[1]) {
        case 'day':
            return getRankByDay(date, limit, sort)
        case 'dayOne':
            return getRankByDayOne(date, limit, sort)
        case 'dayTwo':
            return getRankByDayTwo(date, limit, sort)
        case 'dayThree':
            return getRankByDayThree(date, limit, sort)
        case 'weekOne':
            return getRankByWeekOne(date, limit, sort)
        default:
            return getRankByDay(date, limit, sort)
    }
}

