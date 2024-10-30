

export const utcToJst = (utc: string) => {
    return new Date(utc).toLocaleString('sv-SE', {
        timeZone: 'Asia/Tokyo',
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
    })
}

export const convDateList = (data: any) => {
    const date: string[] = []
    Object.keys(data).map((key) => {
        const d = utcToJst(data[key]['date']).split(' ')[0]
        date.push(d.split('-')[2])
    })
    return date
}