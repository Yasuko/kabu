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
    
    return (
        <>
            <div className="relative top-[-20px]">値動き</div>
            { buildHistoryList(historys) }
        </>
    )
}

const buildHistoryList = (history: number[]) => {
    // 配列を逆に並べ替える
    history.reverse()
    // 10以降は削除
    if (history.length > 10) {
        history = history.slice(0, 10)
    }

    // 配列を逆に並べ替える
    // history.reverse()

    return history.map((value, index) => {
        return (
            <div key={index}>
                { Math.floor(value * 100) / 100 }
            </div>
        )
    })
}