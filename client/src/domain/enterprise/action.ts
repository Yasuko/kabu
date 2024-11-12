'use server'

import {
    getAll
} from '@/src/model/enterprise.model'

import {
    getFinanceInfo
} from '@/src/model/information.model'


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
    companyCode: string
):Promise<any> => {
    return getByCompanyCode(companyCode)
}