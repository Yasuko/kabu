'use server'

import {
    getRankByDay, getRankByDayOne, getRankByDayTwo,
    getRankByDayThree, getRankByWeekOne, getRankByWeekTwo
} from '@/src/model/analisis.date.model'

export async function getRankByDayOneAction(
    date: string,
    limit: number = 10
) {
    return await getRankByDayOne(date, limit)
}

