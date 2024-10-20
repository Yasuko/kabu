'use client'
import React, { Suspense } from "react"
import { usePathname } from "next/navigation"
import { useEffect } from "react"

import { IStaticMethods } from "preline/preline"
declare global {
  interface Window {
    HSStaticMethods: IStaticMethods;
  }
}
import List from "../(components)/list"

export default function Page() {
    const path = usePathname()
    // 今日の日付を「YYYY-MM-DD」形式の文字列で取得
    const today = new Date(Date.now() - 86400000).toISOString().split('T')[0]
    // const today = new Date().toISOString().split('T')[0]

    useEffect(() => {
        const loadPreline = async () => {
            await import("preline/preline")
    
            window.HSStaticMethods.autoInit()
        }
    
        loadPreline()
    }, [path])

    return (
        <>
        <main
            className="
                flex flex-col gap-8 row-start-2
                items-center sm:items-start
            ">
            <div className="justify-center border-b border-gray-200 dark:border-neutral-700">
                <nav className="-mb-0.5 flex justify-center gap-x-6" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
                    <button
                        type="button"
                        className="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500 active" id="horizontal-alignment-item-1"
                        aria-selected="true"
                        data-hs-tab="#horizontal-alignment-1"
                        aria-controls="horizontal-alignment-1"
                        role="tab">
                    当日
                    </button>
                    <button
                        type="button"
                        className="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500" id="horizontal-alignment-item-2"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-2"
                        aria-controls="horizontal-alignment-2"
                        role="tab">
                    前日
                    </button>
                    <button
                        type="button"
                        className="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500" id="horizontal-alignment-item-2"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-3"
                        aria-controls="horizontal-alignment-3"
                        role="tab">
                    2日前
                    </button>
                    <button
                        type="button"
                        className="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500" id="horizontal-alignment-item-3"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-4"
                        aria-controls="horizontal-alignment-4"
                        role="tab">
                    3日前
                    </button>
                    <button
                        type="button"
                        className="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500" id="horizontal-alignment-item-3"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-5"
                        aria-controls="horizontal-alignment-5"
                        role="tab">
                    1週前
                    </button>
                    <button
                        type="button"
                        className="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500" id="horizontal-alignment-item-3"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-6"
                        aria-controls="horizontal-alignment-6"
                        role="tab">
                    2週前
                    </button>
                </nav>
            </div>
            <div className="mt-3">
                <div id="horizontal-alignment-1" role="tabpanel" aria-labelledby="horizontal-alignment-item-1">
   
                    <p className="text-gray-500 dark:text-neutral-400">
                        1日の変動ランキング [上昇ランク、下降ランク]
                    </p>
                    <div className="flex gap-4 items-center flex-col sm:flex-row">
                        <Suspense fallback={<div>Loading...</div>}>
                            <div className="grid grid-cols-2 gap-1">
                                <div>
                                    <List date={today} target={'day'} sort={'upper'} />
                                </div>
                                <div>
                                    <List date={today} target={'day'} sort={'lower'} />
                                </div>
                            </div>
                        </Suspense>
                    </div>
                </div>
            <div id="horizontal-alignment-2" role="tabpanel" aria-labelledby="horizontal-alignment-item-1">
                <p className="text-gray-500 dark:text-neutral-400">
                    前日との変動ランキング [上昇ランク、下降ランク]
                </p>
            
                <div className="flex gap-4 items-center flex-col sm:flex-row">
                    <Suspense fallback={<div>Loading...</div>}>
                    <div className="grid grid-cols-2 gap-1">
                        <div>
                            <List date={today} target={'dayone'} sort={'upper'} />
                        </div>
                        <div>
                            <List date={today} target={'dayone'} sort={'lower'} />
                        </div>
                    </div>
                    </Suspense>
                </div>
            </div>
            <div id="horizontal-alignment-3" role="tabpanel" aria-labelledby="horizontal-alignment-item-1">
                <p className="text-gray-500 dark:text-neutral-400">
                    2日前との変動ランキング [上昇ランク、下降ランク]
                </p>
                
                <div className="flex gap-4 items-center flex-col sm:flex-row">
                    <Suspense fallback={<div>Loading...</div>}>
                    <div className="grid grid-cols-2 gap-1">
                        <div>
                            <List date={today} target={'daytwo'} sort={'upper'} />
                        </div>
                        <div>
                            <List date={today} target={'daytwo'} sort={'lower'} />
                        </div>
                    </div>
                    </Suspense>
                </div>
            </div>
            <div id="horizontal-alignment-4" role="tabpanel" aria-labelledby="horizontal-alignment-item-1">
                <p className="text-gray-500 dark:text-neutral-400">
                    3日前との変動ランキング [上昇ランク、下降ランク]
                </p>
                <div className="flex gap-4 items-center flex-col sm:flex-row">
                    <Suspense fallback={<div>Loading...</div>}>
                    <div className="grid grid-cols-2 gap-1">
                        <div>
                            <List date={today} target={'daythree'} sort={'upper'} />
                        </div>
                        <div>
                            <List date={today} target={'daythree'} sort={'lower'} />
                        </div>
                    </div>
                    </Suspense>
                </div>
            </div>
            <div id="horizontal-alignment-5" role="tabpanel" aria-labelledby="horizontal-alignment-item-1">
                <p className="text-gray-500 dark:text-neutral-400">
                    １週間前との変動ランキング [上昇ランク、下降ランク]
                </p>
                <div className="flex gap-4 items-center flex-col sm:flex-row">
                    <Suspense fallback={<div>Loading...</div>}>
                    <div className="grid grid-cols-2 gap-1">
                        <div>
                            <List date={today} target={'weekone'} sort={'upper'} />
                        </div>
                        <div>
                            <List date={today} target={'daythree'} sort={'lower'} />
                        </div>
                    </div>
                    </Suspense>
                </div>
            </div>
            <div id="horizontal-alignment-6" role="tabpanel" aria-labelledby="horizontal-alignment-item-1">
                <p className="text-gray-500 dark:text-neutral-400">
                    ２週間前との変動ランキング [上昇ランク、下降ランク]
                </p>
                <div className="flex gap-4 items-center flex-col sm:flex-row">
                    <Suspense fallback={<div>Loading...</div>}>
                    <div className="grid grid-cols-2 gap-1">
                        <div>
                            <List date={today} target={'weektwo'} sort={'upper'} />
                        </div>
                        <div>
                            <List date={today} target={'daythree'} sort={'lower'} />
                        </div>
                    </div>
                    </Suspense>
                </div>
            </div>
        </div>
    </main>
    </>
    )
}
