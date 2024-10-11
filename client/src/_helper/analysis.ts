

export const convert_pressure = (
    record: any
) => {
    let upper_wick = 0
    let lower_wick = 0

    if (record.close > record.open) {
        upper_wick = record.high - record.close
        lower_wick = record.open - record.low
    } else {
        upper_wick = record.high - record.open
        lower_wick = record.close - record.low
    }

    return (upper_wick - lower_wick > 0)
        ? ((record.low / record.close) * 100) - 100
        : ((record.high / record.close) * 100) - 100
}