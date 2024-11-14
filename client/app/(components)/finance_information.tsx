import React from 'react'

import ToolTip from './tooltip'

export default function FinanceInformation({
    info,
}: {
    info: any,
}) {
    return (

    <div className="p-2 md:p-5">
    <div className="flex items-center gap-x-2">
        <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
            Information
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
                            className="px-2 py-3 text-start text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">
                                Info
                        </th>
                        <th
                            scope="col"
                            className="px-2 py-3 text-start text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">
                                Score
                        </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-200 dark:divide-neutral-700">
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                            ">
                                <ToolTip label="DividendYield" tips="Market Capitalization" position='top' />

                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.dividendyield}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                Beta
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.beta}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                ProfitMargins
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.profitmargins}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                PriceToBook
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.pricetobook}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                EnterPriseToEbitda
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.enterprisetoebitda}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                EnterPriseToRevenue
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.enterprisetorevenue}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                QuickRatio
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.quickratio}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                CurrentRatio
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.currentratio}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                DebttoEquity
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.debttoequity}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                ReturnOnAssets
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.returnonassets}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                ReturnOnEquity
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.returnonequity}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                RevenueGrowth
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.revenuegrowth}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                GrossMargins
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.grossmargins}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                EbitdaMargins
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.ebitdamargins}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                OperatingMargins
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.operatingmargins}
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
    
    )
}