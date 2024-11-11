'''
市場情報 (MarketInfo)
'''

from lib.utils import validate

'''

「WeekChange52」は「52WeekChange」から代入
'''
class InformationType:
    companyCode: str
    Date: str
    auditRisk: float
    boardRisk: float
    compensationRisk: float
    shareHolderRightsRisk: float
    overallRisk: float
    governanceEpochDate: float
    compensationAsOfEpochDate: float
    maxAge: float
    priceHint: float
    previousClose: float
    open: float
    dayLow: float
    dayHigh: float
    regularMarketPreviousClose: float
    regularMarketOpen: float
    regularMarketDayLow: float
    regularMarketDayHigh: float
    dividendRate: float
    dividendYield: float
    exDividendDate: float
    payoutRatio: float
    fiveYearAvgDividendYield: float
    beta: float
    trailingPE: float
    forwardPE: float
    volume: float
    regularMarketVolume: float
    averageVolume: float
    averageVolume10days: float
    averageDailyVolume10Day: float
    bid: float
    ask: float
    marketCap: float
    fiftyTwoWeekLow: float
    fiftyTwoWeekHigh: float
    priceToSalesTrailing12Months: float
    fiftyDayAverage: float
    twoHundredDayAverage: float
    trailingAnnualDividendRate: float
    trailingAnnualDividendYield: float
    currency: str
    enterpriseValue: float
    profitMargins: float
    floatShares: float
    sharesOutstanding: float
    heldPercentInsiders: float
    heldPercentInstitutions: float
    impliedSharesOutstanding: float
    bookValue: float
    priceToBook: float
    lastFiscalYearEnd: float
    nextFiscalYearEnd: float
    mostRecentQuarter: float
    netIncomeToCommon: float
    trailingEps: float
    forwardEps: float
    pegRatio: float
    lastSplitFactor: str
    lastSplitDate: float
    enterpriseToRevenue: float
    enterpriseToEbitda: float
    WeekChange52: float
    SandP52WeekChange: float
    lastDividendValue: float
    lastDividendDate: float
    exchange: str
    quoteType: str
    symbol: str
    underlyingSymbol: str
    shortName: str
    longName: str
    firstTradeDateEpochUtc: float
    timeZoneFullName: str
    timeZoneShortName: str
    uuid: str
    messageBoardId: str
    gmtOffSetMilliseconds: float
    currentPrice: float
    targetHighPrice: float
    targetLowPrice: float
    targetMeanPrice: float
    targetMedianPrice: float
    recommendationMean: float
    recommendationKey: str
    numberOfAnalystOpinions: float
    totalCash: float
    totalCashPerShare: float
    ebitda: float
    totalDebt: float
    quickRatio: float
    currentRatio: float
    totalRevenue: float
    debtToEquity: float
    revenuePerShare: float
    returnOnAssets: float
    returnOnEquity: float
    freeCashflow: float
    operatingCashflow: float
    revenueGrowth: float
    grossMargins: float
    ebitdaMargins: float
    operatingMargins: float
    financialCurrency: str
    trailingPegRatio: float



class InformationDBType(InformationType):
    id: str
    createdAt: str

def ConvertToInformationType(data: dict) -> InformationType:
    result = {}
    for key in InformationType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], InformationType.__annotations__[key])
        else:
            result[key] = validate('', InformationType.__annotations__[key])
    if '52WeekChange' in data:
        result['WeekChange52'] = validate(data['52WeekChange'], float)
    return result

class Information:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS information (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20) NOT NULL,
    Date DATE NOT NULL,
    auditRisk NUMERIC,
    boardRisk NUMERIC,
    compensationRisk NUMERIC,
    shareHolderRightsRisk NUMERIC,
    overallRisk NUMERIC,
    governanceEpochDate NUMERIC,
    compensationAsOfEpochDate NUMERIC,
    maxAge NUMERIC,
    priceHint NUMERIC,
    previousClose NUMERIC,
    open NUMERIC,
    dayLow NUMERIC,
    dayHigh NUMERIC,
    regularMarketPreviousClose NUMERIC,
    regularMarketOpen NUMERIC,
    regularMarketDayLow NUMERIC,
    regularMarketDayHigh NUMERIC,
    dividendRate NUMERIC,
    dividendYield NUMERIC,
    exDividendDate NUMERIC,
    payoutRatio NUMERIC,
    fiveYearAvgDividendYield NUMERIC,
    beta NUMERIC,
    trailingPE NUMERIC,
    forwardPE NUMERIC,
    volume NUMERIC,
    regularMarketVolume NUMERIC,
    averageVolume NUMERIC,
    averageVolume10days NUMERIC,
    averageDailyVolume10Day NUMERIC,
    bid NUMERIC,
    ask NUMERIC,
    marketCap NUMERIC,
    fiftyTwoWeekLow NUMERIC,
    fiftyTwoWeekHigh NUMERIC,
    priceToSalesTrailing12Months NUMERIC,
    fiftyDayAverage NUMERIC,
    twoHundredDayAverage NUMERIC,
    trailingAnnualDividendRate NUMERIC,
    trailingAnnualDividendYield NUMERIC,
    currency VARCHAR(50),
    enterpriseValue NUMERIC,
    profitMargins NUMERIC,
    floatShares NUMERIC,
    sharesOutstanding NUMERIC,
    heldPercentInsiders NUMERIC,
    heldPercentInstitutions NUMERIC,
    impliedSharesOutstanding NUMERIC,
    bookValue NUMERIC,
    priceToBook NUMERIC,
    lastFiscalYearEnd NUMERIC,
    nextFiscalYearEnd NUMERIC,
    mostRecentQuarter NUMERIC,
    netIncomeToCommon NUMERIC,
    trailingEps NUMERIC,
    forwardEps NUMERIC,
    pegRatio NUMERIC,
    lastSplitFactor VARCHAR(50),
    lastSplitDate NUMERIC,
    enterpriseToRevenue NUMERIC,
    enterpriseToEbitda NUMERIC,
    WeekChange52 NUMERIC,
    SandP52WeekChange NUMERIC,
    lastDividendValue NUMERIC,
    lastDividendDate NUMERIC,
    exchange VARCHAR(50),
    quoteType VARCHAR(50),
    symbol VARCHAR(50),
    underlyingSymbol VARCHAR(50),
    shortName VARCHAR(100),
    longName VARCHAR(100),
    firstTradeDateEpochUtc NUMERIC,
    timeZoneFullName VARCHAR(100),
    timeZoneShortName VARCHAR(100),
    uuid VARCHAR(100),
    messageBoardId VARCHAR(100),
    gmtOffSetMilliseconds NUMERIC,
    currentPrice NUMERIC,
    targetHighPrice NUMERIC,
    targetLowPrice NUMERIC,
    targetMeanPrice NUMERIC,
    targetMedianPrice NUMERIC,
    recommendationMean NUMERIC,
    recommendationKey VARCHAR(50),
    numberOfAnalystOpinions NUMERIC,
    totalCash NUMERIC,
    totalCashPerShare NUMERIC,
    ebitda NUMERIC,
    totalDebt NUMERIC,
    quickRatio NUMERIC,
    currentRatio NUMERIC,
    totalRevenue NUMERIC,
    debtToEquity NUMERIC,
    revenuePerShare NUMERIC,
    returnOnAssets NUMERIC,
    returnOnEquity NUMERIC,
    freeCashflow NUMERIC,
    operatingCashflow NUMERIC,
    revenueGrowth NUMERIC,
    grossMargins NUMERIC,
    ebitdaMargins NUMERIC,
    operatingMargins NUMERIC,
    financialCurrency VARCHAR(50),
    trailingPegRatio NUMERIC,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON information (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table information')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()

