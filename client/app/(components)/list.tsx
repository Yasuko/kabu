'use client'
import React from "react"
import useSWR from "swr"
import {
    getRankActionV2
} from "@/src/domain/rank/action"
import {
    getEnterpriseList
} from "@/src/domain/enterprise/action"

import History from "@/app/(components)/history"
import GraphHistory from "@/app/(components)/graph_history"

import Link from "next/link"

type rankType = {
    upper: any,
    lower: any,
    labels: number[]
}

const ranks: rankType = {
    upper: {
        day: [],
        dayOne: [],
        dayTwo: [],
        dayThree: [],
        weekOne: [],
        weekTwo: [],
    },
    lower: {
        day: [],
        dayOne: [],
        dayTwo: [],
        dayThree: [],
        weekOne: [],
        weekTwo: [],
    },
    labels: []
}

type TargetType = 'day' | 'dayone' | 'daytwo' | 'daythree' | 'weekone' | 'weektwo'

export default function List({
    target,
    sort = 'upper'
}: {
    target: TargetType,
    sort: 'upper' | 'lower'
}) {

    const { data, error } = useSWR<rankType>('ranks', getRankActionV2, {})
    const { data: enterprise, error: enterpriseError } = useSWR('enterprise', getEnterpriseList, {})

    // const list = await fetchDataList(date, target)
    if (error) return <div>Loading...</div>
    if (!data) return <div>Loading...</div>
    if (enterpriseError) return <div>Loading...</div>
    if (!enterprise) return <div>Loading...</div>

    ranks.upper = data.upper
    ranks.lower = data.lower
    ranks.labels = data.labels

    return (
    <div className="relative overflow-x-auto">
        <div
            className="
                w-full
                text-xs text-center
                rtl:text-right text-gray-500 dark:text-gray-400
            ">
            <div>
                { 
                buildList(target, sort, enterprise) 
                }
            </div>
        </div>
    </div>
    )
}

const buildList = async (
    target: TargetType,
    sort: 'upper' | 'lower' = 'upper',
    enterprise: any
): Promise<JSX.Element[]> => {

    return ranks[sort][target]['Rank'].map((val: string, index: number) => {
        return (
            <div
                key={index}
                className="
                grid grid-cols-7 gap-4
                max-w-[600px] mx-auto
                bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <div
                    className="
                        w-full
                        col-span-7 px-6 py-4
                        text-sm text-center
                    ">
                    <p className="relative float-left pl-2">rank { index + 1 }</p>
                    <p className="relative float-center">
                        <Link href={"/rank/" + val}>
                            { enterprise[val]['stockName'] }
                        </Link>
                    </p>
                </div>
                <div className="col-span-2 px-6 py-4 h-[200px]">
                    <History
                        historys={ranks[sort][target]['History'][index]}
                    />
                </div>
                <div className="col-span-5 px-6 py-4">
                    <GraphHistory
                        list={ranks[sort][target]['Move'][index]}
                        labels={ranks.labels}
                    />
                </div>
            </div>
        )
    })
}
