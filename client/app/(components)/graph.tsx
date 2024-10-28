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

const colormap = Array.from({ length: 10 }, getRandomColor)

export default function Graph({
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
    
    const datasets = Object.keys(list).map((_key, index) => {
        return {
            label: label,
            data: list[_key],
            fill: false,
            borderColor: colormap[index],
            tension: 0.1
        }
    })
    const data: ChartData<'line'> = {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
        datasets: datasets
    }

    return (
        <Line options={options} data={data} />
    )
}