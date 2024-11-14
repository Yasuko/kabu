

export const buildCandleList = (data: any) => {
    const _data = data.map((d: any) => {
        return {
            x: d.Date,
            y: [d.Open, d.High, d.Low, d.Close]
        }
    })
    return _data
}


export const convertFormat = (data: any) => {
    // dataを逆順に並べ替え
    data.reverse()

    return data.map(item => ({
        x: item.date,
        y: [parseFloat(item.open), parseFloat(item.high), parseFloat(item.low), parseFloat(item.close)]
    }));
}