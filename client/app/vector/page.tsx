import React from "react"

export default async function Page() {

    // 今日の日付を「YYYY-MM-DD」形式の文字列で取得
    const today = new Date().toISOString().split('T')[0]
    
    return (
        <div className="w-full lg:ps-64">
            <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
            <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
                今日は{ today }
            </main>
            </div>
        </div>
    )
}
