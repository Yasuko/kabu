

export const buildCandleList = (data: any) => {
    const _data = data.map((d: any) => {
        return {
            x: d.Date,
            y: [d.Open, d.High, d.Low, d.Close]
        }
    })
    return _data
}