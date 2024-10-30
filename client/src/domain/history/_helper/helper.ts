import { utcToJst } from "@/src/_helper/date"

export const SortHistoryData = (data: any) => {
    const open: number[] = []
    const close: number[] = []
    const high: number[] = []
    const low: number[] = []
    const volume: number[] = []
    const date: number[] = []

    Object.keys(data).map((key) => {
        const d = utcToJst(data[key]['date']).split(' ')[0]
        open.push(data[key]['open'])
        close.push(data[key]['close'])
        high.push(data[key]['high'])
        low.push(data[key]['low'])
        volume.push(data[key]['volume'])
        date.push(Number(d.split('-')[2]))
    })
    // console.log('SortHistoryData', open, close, high, low)
    return {
        open,
        close,
        high,
        low,
        volume,
        date
    }
}

