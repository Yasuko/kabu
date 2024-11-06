'use client'
import React from 'react'
import Breadcrumbs from '../(components)/breadcrumbs'

export default function RankLayout(
    {
        children,
    }: Readonly<{
        children: React.ReactNode
    }>
) {
    return (
        <div className="w-full lg:ps-64">

            <nav className="inline-flex items-center gap-x-6 p-6 text-lg">
                <Breadcrumbs
                    breadcrumbs={[
                        { label: 'Home', href: '/' },
                        { label: 'Rank', href: '/rank' },
                    ]}
                />
            </nav>
            <div
                className="
                    grid tems-center justify-items-center
                    min-h-screen p-8 pt-2 pb-20
                    font-[family-name:var(--font-geist-sans)]">
                {children}
            </div>
        </div>
 
    )
}
