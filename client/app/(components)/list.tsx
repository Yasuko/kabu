'use client'
import React from "react"

export default function List({
    list,
    callback
}: {
    list: any,
    callback: any
}) {
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
                { buildList(list, callback) }
            </tbody>
        </table>
    </div>
    )
}

const buildList = (list: any, callback: any): JSX.Element[] => {
    return Object.keys(list).map((key, index) => {
        return (
            <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" className="text-center px-6 py-4 font-medium">
                    <a href="#" onClick={() => callback(list[key]['companycode'])}>
                        { list[key]['companycode'] }
                    </a>
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