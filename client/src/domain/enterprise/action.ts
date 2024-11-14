'use server'

import {
    getAll
} from '@/src/model/enterprise.model'

import {
    getFinanceInfo
} from '@/src/model/information.model'

import {
    getLatestHistory
} from '@/src/model/history.date.model'

import { convertFormat } from './_helper/helper'

export const getEnterpriseList = async (
):Promise<{[key: string]: any}> => {
    const e = await getAll()
    if (e.status === false) {
        return []
    }
    // console.log('getEnterpriseList', e.data)
    return e.data
}


export const getCompanyInfoAction = async (
    key: string
):Promise<any> => {
    const companyCode = key.split('/')[1]
    const c = await getFinanceInfo(companyCode)
    const h = await getLatestHistory(companyCode, 30)

    if (c.status === false || h.status === false) {
        return {
            status: false,
            message: 'Error'
        }
    }
    return {
        status: true,
        companyInfo: c.data,
        history: convertFormat(h.data)
    }
}