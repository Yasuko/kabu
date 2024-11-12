'use client'
import React from "react"
import useSWR from "swr"

import {
    getHistoryAction
} from "@/src/domain/history/action"

export default function History({
    historys,
    label = 'price',
}: {
    historys: number[],
    label: string,
}) {
    
    return (
        <>
            <div
                className="
                    absolute mt-[-20px] indent-1 text-center
                ">
                { label }
            </div>
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