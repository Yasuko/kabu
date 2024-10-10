import React from 'react'
//import { notFound } from 'remix'
import GraphHistory from '../../(components)/graph_history'

import {
    getHistoryAction
} from '@/src/domain/rank/action'
import Link from 'next/link'

export default async function Page({
    params
}: {
    params: { id: string }
}) {
    const today = new Date(Date.now() - 86400000).toISOString().split('T')[0]
    const historys = await getHistoryAction(params.id, today, 30)
    console.log(historys)
    return (

    <div className="max-w-[300rem] px-4 py-12 sm:px-6 lg:px-8  mx-auto">
        <div className='px-10 py-2'>
            <Link href="/rank">
                Return ⇐
            </Link>
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-2 gap-4 sm:gap-6">

            <div className="
                flex flex-col bg-white border
                shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Open
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphHistory list={historys.data.open} label='Open' />
                </div>
            </div>
            </div>

            <div className="
                flex flex-col bg-white border
                shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Close
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphHistory list={historys.data.close} label='Open' />
                </div>
            </div>
            </div>

            <div className="
                flex flex-col bg-white border
                shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        High
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphHistory list={historys.data.high} label='Open' />
                </div>
            </div>
            </div>

            <div className="
                flex flex-col bg-white border
                shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Low
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphHistory list={historys.data.low} label='Open' />
                </div>
            </div>
            </div>

            <div className="
                flex flex-col bg-white border
                shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Volume
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphHistory list={historys.data.volume} label='Open' />
                </div>
            </div>
            </div>
        </div>
    </div>

    )
}