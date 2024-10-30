'use client'
import React from "react"
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

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement)

export const options: ChartOptions<'line'> = {
    plugins: {
        legend: {
            position: 'top',
        },
        title: {
            display: false,
        }
    },
    scales: {
        x: {
            display: true,
        },
        y: {
            display: true,
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

export const GraphHistory = (
    list: any,
    label: string = 'Open/Close'
) => {
    const data: ChartData<'line'> = {
        labels: list.labels,
        datasets: [{
            label: label,
            data: list.list,
            fill: false,
            borderColor: getRandomColor(),
            tension: 0.1,
        }]
    }

    return (
        <Line options={options} data={data} className="h-[100px] w-[200px]"/>
    )
}

export default GraphHistory