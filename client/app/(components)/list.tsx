import React from "react"
import {
    getRankAction,
} from "@/src/domain/rank/action"
import Link from "next/link"

export default async function List({
    date,
    target
}: {
    date: any,
    target: 'day' | 'dayone' | 'daytwo' | 'daythree' | 'weekone' | 'weektwo',
}) {
    const list = await fetchDataList(date, target)
    return (
    <div className="relative overflow-x-auto">
        <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead className="
                text-xs text-gray-700 uppercase bg-gray-50
                dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" className="px-6 py-3">
                        Company Code
                    </th>
                    <th scope="col" className="px-6 py-3">
                        Day
                    </th>
                    <th scope="col" className="px-6 py-3">
                        DayOne
                    </th>
                    <th scope="col" className="px-6 py-3">
                        DayTwo
                    </th>
                    <th scope="col" className="px-6 py-3">
                        DayThree
                    </th>
                    <th scope="col" className="px-6 py-3">
                        WeekOne
                    </th>
                    <th scope="col" className="px-6 py-3">
                        WeekTwo
                    </th>
                </tr>
            </thead>
            <tbody>
                { buildList(list) }
            </tbody>
        </table>
    </div>
    )
}

const buildList = async (
    list: any,
): Promise<JSX.Element[]> => {
    return Object.keys(list).map((key, index) => {
        return (
            <tr
                key={index}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th
                    scope="row"
                    className="text-center px-6 py-4 font-medium cursor-pointer"
                    >
                    <Link href={"/rank/" + list[key]['companycode']}>
                        { list[key]['companycode'] }
                    </Link>
                </th>
                <td className="px-6 py-4">
                    { strSplit(list[key]['day']) }
                </td>
                <td className="px-6 py-4">
                    { strSplit(list[key]['dayone']) }
                </td>
                <td className="px-6 py-4">
                    { strSplit(list[key]['daytwo']) }
                </td>
                <td className="px-6 py-4">
                    { strSplit(list[key]['daythree']) }
                </td>
                <td className="px-6 py-4">
                    { strSplit(list[key]['weekone']) }
                </td>
                <td className="px-6 py-4">
                    { strSplit(list[key]['weektwo']) }
                </td>
            </tr>
        )
    })
}

const strSplit = (str: string, len: number = 8): string => {
    return str.length > len ? str.slice(0, len) + '...' : str
}


const fetchDataList = async (
    today: string,
    target: 'day' | 'dayone' | 'daytwo' | 'daythree' | 'weekone' | 'weektwo'
): Promise<any> => {
    switch (target) {
        case 'day':
            return await getRankAction(today, 10, 'day')
        case 'dayone':
            return await getRankAction(today, 10, 'dayOne')
        case 'daytwo':
            return await getRankAction(today, 10, 'dayTwo')
        case 'daythree':
            return await getRankAction(today, 10, 'dayThree')
        case 'weekone':
            return await getRankAction(today, 10, 'weekOne')
        case 'weektwo':
            return await getRankAction(today, 10, 'weekTwo')
        default:
            return []
    }
}