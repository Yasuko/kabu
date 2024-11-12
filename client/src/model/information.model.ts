import { PGService } from '@/src/_lib/db/pg.service'

type ReturnSuccessType = {
    status: true
    data: {
        id: string
        companyCode: string
        Date: string
        auditRisk: number
        boardRisk: number
        compensationRisk: number
        shareHolderRightsRisk: number
        overallRisk: number
        governanceEpochDate: number
        compensationAsOfEpochDate: number
        maxAge: number
        priceHint: number
        previousClose: number
        open: number
        dayLow: number
        dayHigh: number
        regularMarketPreviousClose: number
        regularMarketOpen: number
        regularMarketDayLow: number
        regularMarketDayHigh: number
        dividendRate: number
        dividendYield: number
        exDividendDate: number
        payoutRatio: number
        fiveYearAvgDividendYield: number
        beta: number
        trailingPE: number
        forwardPE: number
        volume: number
        regularMarketVolume: number
        averageVolume: number
        averageVolume10days: number
        averageDailyVolume10Day: number
        bid: number
        ask: number
        marketCap: number
        fiftyTwoWeekLow: number
        fiftyTwoWeekHigh: number
        priceToSalesTrailing12Months: number
        fiftyDayAverage: number
        twoHundredDayAverage: number
        trailingAnnualDividendRate: number
        trailingAnnualDividendYield: number
        currency: string
        enterpriseValue: number
        profitMargins: number
        numberShares: number
        sharesOutstanding: number
        heldPercentInsiders: number
        heldPercentInstitutions: number
        impliedSharesOutstanding: number
        bookValue: number
        priceToBook: number
        lastFiscalYearEnd: number
        nextFiscalYearEnd: number
        mostRecentQuarter: number
        netIncomeToCommon: number
        trailingEps: number
        forwardEps: number
        pegRatio: number
        lastSplitFactor: string
        lastSplitDate: number
        enterpriseToRevenue: number
        enterpriseToEbitda: number
        WeekChange52: number
        SandP52WeekChange: number
        lastDividendValue: number
        lastDividendDate: number
        exchange: string
        quoteType: string
        symbol: string
        underlyingSymbol: string
        shortName: string
        longName: string
        firstTradeDateEpochUtc: number
        timeZoneFullName: string
        timeZoneShortName: string
        uuid: string
        messageBoardId: string
        gmtOffSetMilliseconds: number
        currentPrice: number
        targetHighPrice: number
        targetLowPrice: number
        targetMeanPrice: number
        targetMedianPrice: number
        recommendationMean: number
        recommendationKey: string
        numberOfAnalystOpinions: number
        totalCash: number
        totalCashPerShare: number
        ebitda: number
        totalDebt: number
        quickRatio: number
        currentRatio: number
        totalRevenue: number
        debtToEquity: number
        revenuePerShare: number
        returnOnAssets: number
        returnOnEquity: number
        freeCashflow: number
        operatingCashflow: number
        revenueGrowth: number
        grossMargins: number
        ebitdaMargins: number
        operatingMargins: number
        financialCurrency: string
        trailingPegRatio: number
    }[]
}

type ReturnErrorType = {
    status: false
    message: string
}

export const getFinanceInfo = async (
    companyCode: string
): Promise<ReturnSuccessType | ReturnErrorType> => {
    const pgService = PGService.call()
    const query = `
        SELECT
            i.dividendYield,
            i.beta,
            i.profitMargins,
            i.priceToBook,
            i.enterpriseToEbitda,
            i.enterpriseToRevenue,
            i.quickRatio,
            i.currentRatio,
            i.debtToEquity,
            i.returnOnAssets,
            i.returnOnEquity,
            i.revenueGrowth,
            i.grossMargins,
            i.ebitdaMargins,
            i.operatingMargins
        FROM
            information as i
        WHERE
            i.companyCode = $1
        ORDER BY
            i.Date DESC
        LIMIT 1
    `
    const values = [companyCode]
    const r = await pgService.getOne(query, values)
    return (r === false) ? {
        status: false,
        message: 'Error'
    } : {
        status: true,
        data: r
    }
}

