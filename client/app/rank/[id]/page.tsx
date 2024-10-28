import React from 'react'
//import { notFound } from 'remix'
import GraphHistory from '../../(components)/graph_history'
import Graph from '../../(components)/graph'

import {
    getAnalysisAction,
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
    const analysis = await getAnalysisAction(params.id)
    
    if (historys.status === false || analysis.status === false) {
        return <div>Loading...</div>
    }
    console.log(historys.data)

    const op_close  = {
        open: historys.data.open,
        close: historys.data.close,
    }
    const high_low  = {
        high: historys.data.high,
        low: historys.data.low,
    }
    const volumes = {
        volume: historys.data.volume
    }

    const pressure = {
        pressure: historys.data.pressure
    }
    return (

    <div className="w-full max-w-[600rem] px-4 py-6 sm:px-6 lg:px-8  mx-auto">
        <div className='px-10 py-2'>
            <Link href="/rank">
                Return ⇐ {params.id}
            </Link>
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-2 gap-4 sm:gap-6">

            <div className="
                flex flex-col bg-white border
                shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Open/Close
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphHistory list={op_close} />
                </div>
            </div>
            </div>

            <div className="
                flex flex-col bg-white border
                shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        High/Low
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphHistory list={high_low} label={'High/Low'} />
                </div>
            </div>
            </div>

            <div className="
                flex flex-col bg-white border
                shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Volumes
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    <GraphHistory list={volumes} />
                </div>
            </div>
            </div>

        </div>
    </div>

    )
}