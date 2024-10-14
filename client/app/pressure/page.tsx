import React, { Suspense } from "react"

import List from "../(components)/list_pressure"

export default function Page() {

    // 今日の日付を「YYYY-MM-DD」形式の文字列で取得
    const today = new Date(Date.now() - 86400000).toISOString().split('T')[0]
    // const today = new Date().toISOString().split('T')[0]

    return (
        <>
        <main
            className="
                flex flex-col gap-8 row-start-2
                items-center sm:items-start
            ">
            <div className="
                py-3 flex items-center text-sm text-gray-800 before:flex-1
                before:border-t before:border-gray-200 before:me-6 after:flex-1
                after:border-t after:border-gray-200 after:ms-6 dark:text-white
                dark:before:border-white-600 dark:after:border-white-600
            ">1日の変動ランキング</div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <Suspense fallback={<div>Loading...</div>}>
                    <List date={today} target={'day'} />
                </Suspense>
            </div>
            <div className="
                py-3 flex items-center text-sm text-gray-800 before:flex-1
                before:border-t before:border-gray-200 before:me-6 after:flex-1
                after:border-t after:border-gray-200 after:ms-6 dark:text-white
                dark:before:border-neutral-600 dark:after:border-neutral-600
            ">前日との変動ランキング</div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <Suspense fallback={<div>Loading...</div>}>
                    <List date={today} target={'dayone'} />
                </Suspense>
            </div>
            <div className="
                py-3 flex items-center text-sm text-gray-800 before:flex-1
                before:border-t before:border-gray-200 before:me-6 after:flex-1
                after:border-t after:border-gray-200 after:ms-6 dark:text-white
                dark:before:border-neutral-600 dark:after:border-neutral-600
            ">2日前との変動ランキング</div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <Suspense fallback={<div>Loading...</div>}>
                    <List date={today} target={'daytwo'} />
                </Suspense>
            </div>
            <div className="
                py-3 flex items-center text-sm text-gray-800 before:flex-1
                before:border-t before:border-gray-200 before:me-6 after:flex-1
                after:border-t after:border-gray-200 after:ms-6 dark:text-white
                dark:before:border-neutral-600 dark:after:border-neutral-600
            ">３日前との変動ランキング</div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <Suspense fallback={<div>Loading...</div>}>
                    <List date={today} target={'daythree'} />
                </Suspense>
            </div>
            <div className="
                py-3 flex items-center text-sm text-gray-800 before:flex-1
                before:border-t before:border-gray-200 before:me-6 after:flex-1
                after:border-t after:border-gray-200 after:ms-6 dark:text-white
                dark:before:border-neutral-600 dark:after:border-neutral-600
            ">１週間前との変動ランキング</div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <Suspense fallback={<div>Loading...</div>}>
                    <List date={today} target={'weekone'} />
                </Suspense>
            </div>
            <div className="
                py-3 flex items-center text-sm text-gray-800 before:flex-1
                before:border-t before:border-gray-200 before:me-6 after:flex-1
                after:border-t after:border-gray-200 after:ms-6 dark:text-white
                dark:before:border-neutral-600 dark:after:border-neutral-600
            ">２週間前との変動ランキング</div>
            <div className="flex gap-4 items-center flex-col sm:flex-row">
                <Suspense fallback={<div>Loading...</div>}>
                    <List date={today} target={'weektwo'} />
                </Suspense>
            </div>
        </main>
        </>
    )
}