'use client'
import React from 'react'

export default function PressureLayout(
    {
        children,
    }: Readonly<{
        children: React.ReactNode
    }>
) {

    return (
        <div className="w-full lg:ps-64">
            <div
                className="
                    grid tems-center justify-items-center
                    min-h-screen p-8 pb-20 gap-16 sm:p-20
                    font-[family-name:var(--font-geist-sans)]">
                {children}
            </div>
        </div>
 
    )
}
