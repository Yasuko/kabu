import React from 'react'
import useSWR from 'swr'

import {
    getCompanyInfoAction
} from '@/src/domain/enterprise/action'
import GraphCandle from '@/app/(components)/graph_candle'
import FinanceInformation from './finance_information'

interface CompanyInfo {
    status: boolean,
    companyInfo: any,
    history: any,
}

export default function CompanyInfo({
    companyCode,
}: {
    companyCode: string,
}) {

    const { data, error } = useSWR<CompanyInfo>('companyInfo/' + companyCode, getCompanyInfoAction, {})

    if (error) return <div>Loading...</div>
    if (!data) return <div>Loading...</div>
    if (data.status === false) return <div>Loading...</div>

    const info = {
        dividendyield: data.companyInfo.dividendyield,
        beta: data.companyInfo.beta,
        profitmargins: data.companyInfo.profitmargins,
        pricetobook: data.companyInfo.pricetobook,
        enterprisetoebitda: data.companyInfo.enterprisetoebitda,
        enterprisetorevenue: data.companyInfo.enterprisetorevenue,
        quickratio: data.companyInfo.quickratio,
        currentratio: data.companyInfo.currentratio,
        debttoequity: data.companyInfo.debttoequity,
        returnonassets: data.companyInfo.returnonassets,
        returnonequity: data.companyInfo.returnonequity,
        revenuegrowth: data.companyInfo.revenuegrowth,
        grossmargins: data.companyInfo.grossmargins,
        ebitdamargins: data.companyInfo.ebitdamargins,
        operatingmargins: data.companyInfo.operatingmargins,
    }
    

    return (
    <div
        className="
            absolute hs-overlay w-[75%] h-lvh top-0 right-0
            overflow-x-hidden overflow-y-auto
            bg-gray-800
            pointer-events-none"
        >
        <div className="grid grid-cols-8 grid-rows-2 gap-0 ">


        <div className="
            flex flex-col mt-5 ml-5 h-full
            col-span-2 row-span-2
            bg-white border
            shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <FinanceInformation info={info} />
        </div>


        <div className="
            flex flex-col mt-5 mr-5 h-full
            col-span-6
            shadow-sm rounded-xl
            dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Candle
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphCandle list={data.history} label={'Open/Close'} />
                </div>
            </div>
        </div>


        </div>
    </div>
    )
}
