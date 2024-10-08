'use client'
import React, { use, useEffect } from "react"
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
const labels = ['1', '2', '3', '4', '5']

const getRandomColor = () => {
    const r = Math.floor(Math.random() * 256)
    const g = Math.floor(Math.random() * 256)
    const b = Math.floor(Math.random() * 256)
    const a = (Math.random() * (1 - 0.5) + 0.5).toFixed(2) // alpha between 0.5 and 1
    return `rgba(${r}, ${g}, ${b}, ${a})`
}

const colormap = Array.from({ length: 10 }, getRandomColor)


export default function Graph({
    list
}: {
    list: any
}) {

    const datasets = Object.keys(list).map((key, index) => {
        return {
            label: 'after1',
            data: list[key]['after1'],
            fill: false,
            borderColor: colormap[index],
            tension: 0.1
        }
    })
    const data: ChartData<'line'> = {
        labels: labels,
        datasets: datasets
    }


    return (
        <Line options={options} data={data} />
    )
}