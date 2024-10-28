'use client'
import React from "react"
import useSWR from "swr"

import {
    getHistoryAction
} from "@/src/domain/history/action"

export default function History({
    //companyCode = '0000',
    historys
}: {
    //companyCode: string
    historys: number[]
}) {
    //console.log(companyCode)
    //const { data: history, error: historyError } = useSWR(companyCode, getHistoryAction)

    //if (historyError) return <div>failed to load</div>
    //if (!history) return <div>loading...</div>

    
    return (
        <>
            { buildHistoryList(historys) }
        </>
    )
}

/*
const buildHistoryList = (history: any) => {
    const r = history.map((item: any) => {
        return item.open
    })

    // 配列を逆に並べ替える
    r.reverse()

    return r.join(', ')
}*/

const buildHistoryList = (history: number[]) => {
    // 配列を逆に並べ替える
    history.reverse()
    // 10以降は削除
    if (history.length > 10) {
        history = history.slice(0, 10)
    }

    // 配列を逆に並べ替える
    // history.reverse()

    return history.join(', ')
}