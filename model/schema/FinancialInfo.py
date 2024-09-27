'''
財務情報 (financial_info) テーブルのスキーマを定義するモジュール
'''

from lib.utils import validate

class FinancialInfoType:
    companyCode: str
    enterpriseValue: float
    profitMargins: float
    floatShares: int
    sharesOutstanding: int
    heldPercentInsiders: float
    heldPercentInstitutions: float
    impliedSharesOutstanding: int
    bookValue: float
    priceToBook: float
    lastFiscalYearEnd: int
    nextFiscalYearEnd: int
    mostRecentQuarter: int
    netIncomeToCommon: float
    trailingEps: float
    forwardEps: float
    pegRatio: float
    lastSplitFactor: str
    lastSplitDate: int
    enterpriseToRevenue: float
    enterpriseToEbitda: float
    sandP52WeekChange: float
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

class FinancialInfoDBType(FinancialInfoType):
    id: str
    createdAt: str

def ConvertToFinancialInfoType(data: dict) -> FinancialInfoType:
    result = {}
    for key in FinancialInfoType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], FinancialInfoType.__annotations__[key])
        else:
            result[key] = validate('', FinancialInfoType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class FinancialInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS financial_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20) NOT NULL,
    enterpriseValue NUMERIC,
    profitMargins NUMERIC,
    floatShares BIGINT,
    sharesOutstanding BIGINT,
    heldPercentInsiders NUMERIC,
    heldPercentInstitutions NUMERIC,
    impliedSharesOutstanding BIGINT,
    bookValue NUMERIC,
    priceToBook NUMERIC,
    lastFiscalYearEnd BIGINT,
    nextFiscalYearEnd BIGINT,
    mostRecentQuarter BIGINT,
    netIncomeToCommon NUMERIC,
    trailingEps NUMERIC,
    forwardEps NUMERIC,
    pegRatio NUMERIC,
    lastSplitFactor VARCHAR(10),
    lastSplitDate BIGINT,
    enterpriseToRevenue NUMERIC,
    enterpriseToEbitda NUMERIC,
    sandP52WeekChange NUMERIC,
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
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON financial_info (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table financial_info')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()