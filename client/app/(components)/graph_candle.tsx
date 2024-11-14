'use client'
import React from "react"
import dynamic from "next/dynamic"
import { ApexOptions } from "apexcharts"
const ApexChart = dynamic(() => import("react-apexcharts"), { ssr: false })



const getRandomColor = () => {
    const r = Math.floor(Math.random() * 256)
    const g = Math.floor(Math.random() * 256)
    const b = Math.floor(Math.random() * 256)
    const a = (Math.random() * (1 - 0.5) + 0.5).toFixed(2) // alpha between 0.5 and 1
    return `rgba(${r}, ${g}, ${b}, ${a})`
}

const colormap = Array.from({ length: 10 }, getRandomColor)

export default function GraphCandle({
    list,
    label,
}: {
    list: any,
    label: string,
}) {
    if (list === undefined || list.length === 0) {
        return (
            <div>
                None
            </div>
        )
    }

    const series = [{
            data: list
        }]

    const options: ApexOptions = {
        chart: {
            height: 350
        },
        title: {
            text: 'CandleStick Chart',
            align: 'left'
        },
        xaxis: {
            type: 'datetime'
        },
        yaxis: {
            tooltip: {
                enabled: true
            }
        }
    }


    return (
        <>
            <ApexChart options={options} series={series} type="candlestick" width={800} height={300}/>
        </>
    )

}