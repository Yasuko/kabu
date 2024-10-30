'use client'
import React from "react"
import useSWR from "swr"
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    ChartOptions,
    ChartData,
} from "chart.js"

import { Line } from 'react-chartjs-2'

import {
    getHistoryAction
} from "@/src/domain/history/action"

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement)

type swrType = {
    open: number[],
    close: number[],
    high: number[],
    low: number[],
    volume: number[],
    date: string[]
}

export default function GraphActive({
    companyCode,
    limit = 30,
    label = 'Graph'
}: {
    companyCode: string,
    limit?: number,
    label?: string
}): JSX.Element {
    if (companyCode === undefined) {
        return (
            <div>
                None
            </div>
        )
    }

    const { data, error } = useSWR(
            'get_graph_history/' + companyCode + '/' + limit,
            getHistoryAction,
            {}
        )
    
    if (error) return <div>Loading...</div>
    if (!data) return <div>Loading...</div>
    // const list = await fetchDataList(date, target)

    if (!data) return <div>Loading...</div>
    console.log(companyCode, data['open'])
    const datasets = [{
            label: label,
            data: data['open'],
            fill: false,
            borderColor: getRandomColor(),
            tension: 0.1
        }]
    const _data: ChartData<'line'> = {
        labels: data['date'],
        datasets: datasets
    }

    return (
        <Line options={options} data={_data} />
    )
}

export const options: ChartOptions<'line'> = {
    responsive: true,
    plugins: {
        legend: {
            position: 'top',
        },
        title: {
            display: true,
            text: 'Chart.js Line Chart'
        }
    }
}

const getRandomColor = () => {
    const r = Math.floor(Math.random() * 256)
    const g = Math.floor(Math.random() * 256)
    const b = Math.floor(Math.random() * 256)
    const a = (Math.random() * (1 - 0.5) + 0.5).toFixed(2) // alpha between 0.5 and 1
    return `rgba(${r}, ${g}, ${b}, ${a})`
}