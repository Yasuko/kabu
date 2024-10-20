'use server'
import {
    ReturnSuccessType, ReturnErrorType
} from '@/src/domain/rank/definitions'

import {
    getByCompanyCode,
    getRankByDay, getRankByDayOne, getRankByDayTwo,
    getRankByDayThree, getRankByWeekOne, getRankByWeekTwo
} from '@/src/model/analisis.history.model'

import {
    getPressureByDay, getPressureByDayOne, getPressureByDayTwo,
    getPressureByWeekOne, getPressureByWeekTwo
} from '@/src/model/analisis.pressure.model'

import {
    getByBeforeDate,
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

export const getAnalysisAction = async (
    companyCode: string,
    date: string,
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const r = await getByCompanyCode(companyCode, date)

    if (r.status === false) {
        return {
            status: false,
            message: 'Error'
        }
    }
    
    const afters = [
        r.data.after1,
        r.data.after2,
        r.data.after3,
        r.data.after4,
        r.data.after5,
        r.data.after6,
        r.data.after7,
        r.data.after8,
        r.data.after9,
        r.data.after10,
    ]
    const pressures = [
        r.data.after1pressure,
        r.data.after2pressure,
        r.data.after3pressure,
        r.data.after4pressure,
        r.data.after5pressure,
        r.data.after6pressure,
        r.data.after7pressure,
        r.data.after8pressure,
        r.data.after9pressure,
        r.data.after10pressure,
    ]

    return {
        status: true,
        data: {
            id: r.data.id,
            companyCode: r.data.companycode,
            date: r.data.date,
            day: r.data.day,
            dayOne: r.data.dayone,
            dayTwo: r.data.daytwo,
            dayThree: r.data.daythree,
            pressureDay: r.data.pressday,
            pressureOne: r.data.pressone,
            pressureTwo: r.data.presstwo,
            pressureThree: r.data.pressthree,
            pressureWeekOne: r.data.pressweekone,
            pressureWeekTwo: r.data.pressweektwo,
            weekOne: r.data.weekone,
            weekTwo: r.data.weektwo,

            afters,
            pressures
        }
    }
}

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

export const getRankActionV2 = async (
    rank: 'upper' | 'lower'
): Promise<any> => {
    const upper = await UpperRank()
    const lower = await LowerRank()

    if (upper.status === false || lower.status === false) {
        throw new Error('Error')
    }

    return {
        upper: upper.data,
        lower: lower.data
    }
}
export const getPressureAction = async (
    date: string,
    limit: number = 10,
    target: 'day' | 'dayOne' | 'dayTwo' | 'dayThree' | 'weekOne' | 'weekTwo',
) => {
    switch (target) {
        case 'day':
            return getPressureByDay(date, limit)
        case 'dayOne':
            return getPressureByDayOne(date, limit)
        case 'dayTwo':
            return getPressureByDayTwo(date, limit)
        case 'weekOne':
            return getPressureByWeekOne(date, limit)
        case 'weekTwo':
            return getPressureByWeekTwo(date, limit)
        default:
            return getPressureByDay(date, limit)
    }
}

export const getHistoryAction = async (
    companyCode: string,
    date: string,
    limit: number = 30,
): Promise<ReturnSuccessType | ReturnErrorType> => {
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
    const pressure = []

    for (let i = r.data.length; i > 0; i--) {
        open.push(r.data[i - 1].open)
        close.push(r.data[i - 1].close)
        high.push(r.data[i - 1].high)
        low.push(r.data[i - 1].low)
        volume.push(r.data[i - 1].volume)
        pressure.push(convert_pressure(r.data[i - 1]))
    }

    return {
        status: true,
        data: {
            open,
            close,
            high,
            low,
            volume,
            pressure
        }
    }
}