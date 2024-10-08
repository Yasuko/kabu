import React from "react"
import {
    getRankByDayAction,
    getRankByDayOneAction,
    getRankByDayTwoAction,
    getRankByDayThreeAction,
    getRankByWeekOneAction,
    getRankByWeekTwoAction
} from "@/src/domain/rank/action"

import Graph from "../(components)/graph"
import List from "../(components)/list"

export default async function Page() {

    // 今日の日付を「YYYY-MM-DD」形式の文字列で取得
    const today = new Date().toISOString().split('T')[0]
    
    //const r = await getRankByDayAction('2024-10-08', 10)
    const r2 = await getRankByDayOneAction(today, 10)
    const r3 = await getRankByDayTwoAction(today, 10)
    const r4 = await getRankByDayThreeAction(today, 10)
    const r5 = await getRankByWeekOneAction(today, 10)
    const r6 = await getRankByWeekTwoAction(today, 10)

    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
        <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <List list={r2} />
            </div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <List list={r3} />
            </div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <List list={r4} />
            </div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <List list={r5} />
            </div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <List list={r6} />
            </div>

            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <Graph list={r2} />
            </div>
        </main>
        </div>
    )
}
