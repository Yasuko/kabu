'use server'

import {
    getRankByDay, getRankByDayOne, getRankByDayTwo,
    getRankByDayThree, getRankByWeekOne, getRankByWeekTwo
} from '@/src/model/analisis.date.model'

export async function getRankByDayAction(
    date: string,
    limit: number = 10
) {
    const r = await getRankByDay(date, limit)
    return r
}

export async function getRankByDayOneAction(
    date: string,
    limit: number = 10
) {
    const r = await getRankByDayOne(date, limit)
    return r
}

export async function getRankByDayTwoAction(
    date: string,
    limit: number = 10
) {
    const r = await getRankByDayTwo(date, limit)
    return r
}

export async function getRankByDayThreeAction(
    date: string,
    limit: number = 10
) {
    const r = await getRankByDayThree(date, limit)
    return r
}

export async function getRankByWeekOneAction(
    date: string,
    limit: number = 10
) {
    const r = await getRankByWeekOne(date, limit)
    return r
}

export async function getRankByWeekTwoAction(
    date: string,
    limit: number = 10
) {
    const r = await getRankByWeekTwo(date, limit)
    return r
}