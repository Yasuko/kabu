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

export const GraphHistory = (
    historys: any,
    label: string,
) => {

    // 数値の連番で初期化された、30個の配列を作成
    // 例: [1, 2, 3, 4, 5]
    const labels = Array.from({ length: 30 }, (_v, i) => {
        return i
    })
    const datasets = Object.keys(historys.list).map((_key, index) => {
        console.log(historys.list[_key])
        return {
                label: _key,
                data: historys.list[_key],
                fill: false,
                borderColor: colormap[index],
                tension: 0.1,
            }
    })

    const data: ChartData<'line'> = {
        labels: labels,
        datasets: datasets,
    }

    return (
        <Line options={options} data={data} />
    )
}

export default GraphHistory