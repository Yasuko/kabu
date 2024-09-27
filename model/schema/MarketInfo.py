'''
市場情報 (MarketInfo)
'''

from lib.utils import validate

class MarketInfoType:
    companyCode: str
    priceHint: int
    previousClose: float
    open: float
    dayLow: float
    dayHigh: float
    regularMarketPreviousClose: float
    regularMarketOpen: float
    regularMarketDayLow: float
    regularMarketDayHigh: float
    volume: int
    regularMarketVolume: int
    averageVolume: int
    averageVolume10days: int
    averageDailyVolume10Day: int
    bid: float
    ask: float
    marketCap: float
    fiftyTwoWeekLow: float
    fiftyTwoWeekHigh: float
    priceToSalesTrailing12Months: float
    fiftyDayAverage: float
    twoHundredDayAverage: float

class MarketInfoDBType(MarketInfoType):
    id: str
    createdAt: str

def ConvertToMarketInfoType(data: dict) -> MarketInfoType:
    result = {}
    for key in MarketInfoType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], MarketInfoType.__annotations__[key])
        else:
            result[key] = validate('', MarketInfoType.__annotations__[key])
    return result

class MarketInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS market_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20) NOT NULL,
    priceHint INTEGER,
    previousClose NUMERIC,
    open NUMERIC,
    dayLow NUMERIC,
    dayHigh NUMERIC,
    regularMarketPreviousClose NUMERIC,
    regularMarketOpen NUMERIC,
    regularMarketDayLow NUMERIC,
    regularMarketDayHigh NUMERIC,
    volume BIGINT,
    regularMarketVolume BIGINT,
    averageVolume BIGINT,
    averageVolume10days BIGINT,
    averageDailyVolume10Day BIGINT,
    bid NUMERIC,
    ask NUMERIC,
    marketCap NUMERIC,
    fiftyTwoWeekLow NUMERIC,
    fiftyTwoWeekHigh NUMERIC,
    priceToSalesTrailing12Months NUMERIC,
    fiftyDayAverage NUMERIC,
    twoHundredDayAverage NUMERIC,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON market_info (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table market_info')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()