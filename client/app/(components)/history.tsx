'use client'
import React from "react"
import useSWR from "swr"

import {
    getHistoryAction
} from "@/src/domain/history/action"

export default function History({
    companyCode = '0000',
}: {
    companyCode: string
}) {
    console.log(companyCode)
    const { data: history, error: historyError } = useSWR(companyCode, getHistoryAction)

    if (historyError) return <div>failed to load</div>
    if (!history) return <div>loading...</div>

    
    return (
        <>
            { buildHistoryList(history.data) }
        </>
    )
}


const buildHistoryList = (history: any) => {
    const r = history.map((item: any) => {
        return item.open
    })

    // 配列を逆に並べ替える
    r.reverse()

    return r.join(', ')
}