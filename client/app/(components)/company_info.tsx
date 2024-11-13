import React from 'react'
import useSWR from 'swr'

import {
    getCompanyInfoAction
} from '@/src/domain/enterprise/action'
import Graph from './graph'

interface CompanyInfo {
    companyCode: string
}

export default function CompanyInfo({
    companyCode,
}: {
    companyCode: string,
}) {

    const { data, error } = useSWR<CompanyInfo>('companyInfo/' + companyCode, getCompanyInfoAction, {})

    if (error) return <div>Loading...</div>
    if (!data) return <div>Loading...</div>

    const op_close  = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
    const high_low  = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
    const volumes = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
    const info = {
        dividendyield: '0.023699999',
        beta: '2.028',
        profitmargins: '0.02961',
        pricetobook: '2.4807935',
        enterprisetoebitda: '10.019',
        enterprisetorevenue: '0.741',
        quickratio: '1.102',
        currentratio: '1.374',
        debttoequity: '86.459',
        returnonassets: '0.03423',
        returnonequity: '0.0762',
        revenuegrowth: '0.13',
        grossmargins: '0.47102',
        ebitdamargins: '0.073920004',
        operatingmargins: '0.01523'
    }
    

    return (
    <div
        className="
            absolute hs-overlay w-[75%] h-lvh top-0 right-0
            overflow-x-hidden overflow-y-auto
            bg-gray-800
            pointer-events-none"
        >
        <div className="grid grid-cols-2 gap-8 ">

        <div className="
            flex flex-col m-5 h-[350px]
            bg-white border
            shadow-sm rounded-xl
            dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Open/Close
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <Graph list={op_close} label={'Open/Close'} />
                </div>
            </div>
        </div>

        <div className="
            flex flex-col m-5 h-[350px]
            bg-white border
            shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        High/Low
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <Graph list={high_low} label={'High/Low'} />
                </div>
            </div>
        </div>

        <div className="
            flex flex-col m-5 h-[350px]
            bg-white border
            shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Volumes
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <Graph list={volumes} label={'Volumes'} />
                </div>
            </div>
        </div>
        <div className="
            flex flex-col m-5 h-[350px]
            bg-white border
            shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Volumes
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <div className="flex flex-col">
                        <div className="-m-1.5 overflow-x-auto">
                            <div className="p-1.5 min-w-full inline-block align-middle">
                            <div className="overflow-hidden">
                                <table className="min-w-full divide-y divide-gray-200 dark:divide-neutral-700">
                                <thead>
                                    <tr>
                                    <th 
                                        scope="col"
                                        className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">
                                            Info
                                    </th>
                                    <th
                                        scope="col"
                                        className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">
                                            Score
                                    </th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-gray-200 dark:divide-neutral-700">
                                    <tr>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm font-medium text-gray-800
                                            dark:text-neutral-200
                                            ">
                                            DividendYield
                                    </td>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm text-gray-800 dark:text-neutral-200
                                        ">
                                            {info.dividendyield}
                                    </td>
                                    </tr>
                                    <tr>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm font-medium text-gray-800
                                            dark:text-neutral-200
                                            ">
                                            Beta
                                    </td>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm text-gray-800 dark:text-neutral-200
                                        ">
                                            {info.beta}
                                    </td>
                                    </tr>
                                    <tr>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm font-medium text-gray-800
                                            dark:text-neutral-200
                                            ">
                                            ProfitMargins
                                    </td>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm text-gray-800 dark:text-neutral-200
                                        ">
                                            {info.profitmargins}
                                    </td>
                                    </tr>
                                    <tr>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm font-medium text-gray-800
                                            dark:text-neutral-200
                                            ">
                                            PriceToBook
                                    </td>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm text-gray-800 dark:text-neutral-200
                                        ">
                                            {info.pricetobook}
                                    </td>
                                    </tr>
                                    <tr>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm font-medium text-gray-800
                                            dark:text-neutral-200
                                            ">
                                            EnterPriseToEbitda
                                    </td>
                                    <td
                                        className="
                                            px-6 py-4 whitespace-nowrap
                                            text-sm text-gray-800 dark:text-neutral-200
                                        ">
                                            {info.enterprisetoebitda}
                                    </td>
                                    </tr>
                                    
                                </tbody>
                                </table>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
    </div>
    )
}
