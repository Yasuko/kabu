import React from 'react'
import useSWR from 'swr'

interface CompanyInfo {
    companyCode: string
}

export default function CompanyInfo({
    companyCode,
}: {
    companyCode: string,
}) {
    return (
    <div
        className="
            absolute hs-overlay w-[75%] h-lvh top-0 right-0
            overflow-x-hidden overflow-y-auto
            bg-gray-800
            pointer-events-none"
        >
        <div className="grid grid-cols-2 gap-8 ">

        <div className="
            flex flex-col m-5 h-[350px]
            bg-white border
            shadow-sm rounded-xl
            dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Open/Close
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    
                </div>
            </div>
        </div>

        <div className="
            flex flex-col m-5 h-[350px]
            bg-white border
            shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        High/Low
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    
                </div>
            </div>
        </div>

        <div className="
            flex flex-col m-5 h-[350px]
            bg-white border
            shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Volumes
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    
                </div>
            </div>
        </div>
        <div className="
            flex flex-col m-5 h-[350px]
            bg-white border
            shadow-sm rounded-xl dark:bg-neutral-800 dark:border-neutral-700">
            <div className="p-4 md:p-5">
                <div className="flex items-center gap-x-2">
                    <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
                        Volumes
                    </p>
                </div>

                <div className="mt-1 flex items-center gap-x-2">
                    
                </div>
            </div>
        </div>
        </div>
    </div>
    )
}
