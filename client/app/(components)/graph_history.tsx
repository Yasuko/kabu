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
            display: false,
        }
    },
    scales: {
        x: {
            display: false,
        },
        y: {
            display: false,
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
    console.log(list.list)
    const data: ChartData<'line'> = {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
        datasets: [{
            label: label,
            data: list.list,
            fill: false,
            borderColor: getRandomColor(),
            tension: 0.1,
        }]
    }

    return (
        <Line options={options} data={data}/>
    )
}

export default GraphHistory