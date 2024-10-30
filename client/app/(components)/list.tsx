'use client'
import React from "react"
import useSWR from "swr"
import {
    getRankActionV2
} from "@/src/domain/rank/action"

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

    // const list = await fetchDataList(date, target)
    if (error) return <div>Loading...</div>
    if (!data) return <div>Loading...</div>

    ranks.upper = data.upper
    ranks.lower = data.lower
    ranks.labels = data.labels

    return (
    <div className="relative overflow-x-auto">
        <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead className="
                text-xs text-gray-700 uppercase bg-gray-50
                dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" className="px-6 py-3">
                        rank
                    </th>
                    <th scope="col" className="px-6 py-3">
                        Code
                    </th>
                    <th scope="col" className="px-6 py-3">
                        History
                    </th>
                </tr>
            </thead>
            <tbody>
                { 
                buildList(target, sort) 
                }
            </tbody>
        </table>
    </div>
    )
}

const buildList = async (
    target: TargetType,
    sort: 'upper' | 'lower' = 'upper'
): Promise<JSX.Element[]> => {

    return ranks[sort][target]['Rank'].map((val: string, index: number) => {
        return (
            <tr
                key={index}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th className="px-6 py-4 text-center">
                    { index + 1 }
                </th>
                <th
                    scope="row"
                    className="text-center px-6 py-4 font-medium cursor-pointer"
                    >
                    <Link href={"/rank/" + val}>
                        { val }
                    </Link>
                </th>
                <td className="px-6 py-4">
                    <History
                        historys={ranks[sort][target]['History'][index]} />
                    <GraphHistory
                        list={ranks[sort][target]['Move'][index]}
                        labels={ranks.labels}
                    />
                </td>
            </tr>
        )
    })
}
