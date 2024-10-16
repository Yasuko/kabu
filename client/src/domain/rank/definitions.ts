export type ReturnSuccessType = {
    status: true
    data: any
}

export type ReturnErrorType = {
    status: false
    message: string
}

export type AnalysisType = {
    companyCode: string,
    Date: string,
    Day: number,
    DayOne: number,
    DayTwo: number,
    DayThree: number,
    WeekOne: number,
    WeekTwo: number,
    PressDay: number,
    PressOne: number,
    PressTwo: number,
    PressThree: number,
    PressWeekOne: number,
    PressWeekTwo: number,
    After1: number[],
    After1Pressure: number[],
    After2: number[],
    After2Pressure: number[],
    After3: number[],
    After3Pressure: number[],
    After4: number[],
    After4Pressure: number[],   
    After5: number[],
    After5Pressure: number[],
    After6: number[],
    After6Pressure: number[],
    After7: number[],
    After7Pressure: number[],
    After8: number[],
    After8Pressure: number[],
    After9: number[],
    After9Pressure: number[],
    After10: number[],
    After10Pressure: number[],
}

export type AnalysisFormType = {
    DayRank: AnalysisType[],
    DayOneRank: AnalysisType[],
    DayTwoRank: AnalysisType[],
    DayThreeRank: AnalysisType[],
    WeekOneRank: AnalysisType[],
    WeekTwoRank: AnalysisType[],
}