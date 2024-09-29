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



'''
MarketInfoType = [
    {
        'key': 'companyCode',
        'type': 'str',
        'required': True,
        'db_type': 'UUID PRIMARY KEY DEFAULT uuid_generate_v4()'
    },
    {
        'key': 'priceHint',
        'type': 'int',
        'required': False,
        'db_type': 'INTEGER'
    },
    {
        'key': 'previousClose',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'open',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'dayLow',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'dayHigh',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'regularMarketPreviousClose',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'regularMarketOpen',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'regularMarketDayLow',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'regularMarketDayHigh',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'volume',
        'type': 'int',
        'required': False,
        'db_type': 'BIGINT'
    },
    {
        'key': 'regularMarketVolume',
        'type': 'int',
        'required': False,
        'db_type': 'BIGINT'
    },
    {
        'key': 'averageVolume',
        'type': 'int',
        'required': False,
        'db_type': 'BIGINT'
    },
    {
        'key': 'averageVolume10days',
        'type': 'int',
        'required': False,
        'db_type': 'BIGINT'
    },
    {
        'key': 'averageDailyVolume10Day',
        'type': 'int',
        'required': False,
        'db_type': 'BIGINT'
    },
    {
        'key': 'bid',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'ask',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'marketCap',
        'type': 'float',
    },
    {
        'key': 'fiftyTwoWeekLow',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'fiftyTwoWeekHigh',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'priceToSalesTrailing12Months',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'fiftyDayAverage',
        'type': 'float', 'required': False,'db_type': 'NUMERIC'
    },
    {
        'key': 'twoHundredDayAverage',
        'type': 'float',
        'required': False,
        'db_type': 'NUMERIC'
    },
    {
        'key': 'createdAt',
        'type': 'str',
        'required': False,
        'db_type': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
    }
]


'''