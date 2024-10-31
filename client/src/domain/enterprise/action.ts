'use server'

import {
    getAll
} from '@/src/model/enterprise.model'


export const getEnterpriseList = async (
):Promise<{[key: string]: any}> => {
    const e = await getAll()
    if (e.status === false) {
        return []
    }
console.log('getEnterpriseList', e.data)
    return e.data
}
