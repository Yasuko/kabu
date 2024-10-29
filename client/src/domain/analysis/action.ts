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
    // timezoneをUTCからJSTに変換し、YYYY-MM-DDの形式に変換
    const _d = new Date(d.data['date']).toLocaleString('ja-JP', {
        timeZone: 'Asia/Tokyo',
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    })

    // 「/」を「-」に置き換え
    const date = _d.split(' ')[0].replace(/\//g, '-')
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

