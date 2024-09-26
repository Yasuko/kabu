'''
市場情報 (MarketInfo)

'''

class MarketInfoType:
    company_code: str
    price_hint: int
    previous_close: float
    open: float
    day_low: float
    day_high: float
    regular_market_previous_close: float
    regular_market_open: float
    regular_market_day_low: float
    regular_market_day_high: float
    volume: int
    regular_market_volume: int
    average_volume: int
    average_volume_10days: int
    average_daily_volume_10day: int
    bid: float
    ask: float
    market_cap: float
    fifty_two_week_low: float
    fifty_two_week_high: float
    price_to_sales_trailing_12_months: float
    fifty_day_average: float
    two_hundred_day_average: float

class MarketInfoDBType(MarketInfoType):
    id: str
    createdAt: str

def ConvertToMarketInfoType(data: dict) -> MarketInfoType:
    return {
        'company_code': data['companyCode'],
        'price_hint': data['priceHint'],
        'previous_close': data['previousClose'],
        'open': data['open'],
        'day_low': data['dayLow'],
        'day_high': data['dayHigh'],
        'regular_market_previous_close': data['regularMarketPreviousClose'],
        'regular_market_open': data['regularMarketOpen'],
        'regular_market_day_low': data['regularMarketDayLow'],
        'regular_market_day_high': data['regularMarketDayHigh'],
        'volume': data['volume'],
        'regular_market_volume': data['regularMarketVolume'],
        'average_volume': data['averageVolume'],
        'average_volume_10days': data['averageVolume10days'],
        'average_daily_volume_10day': data['averageDailyVolume10Day'],
        'bid': data['bid'],
        'ask': data['ask'],
        'market_cap': data['marketCap'],
        'fifty_two_week_low': data['fiftyTwoWeekLow'],
        'fifty_two_week_high': data['fiftyTwoWeekHigh'],
        'price_to_sales_trailing_12_months': data['priceToSalesTrailing12Months'],
        'fifty_day_average': data['fiftyDayAverage'],
        'two_hundred_day_average': data['twoHundredDayAverage']
    }

class MarketInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS market_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(20) NOT NULL REFERENCES industry(company_code),
    price_hint INTEGER,
    previous_close NUMERIC,
    open NUMERIC,
    day_low NUMERIC,
    day_high NUMERIC,
    regular_market_previous_close NUMERIC,
    regular_market_open NUMERIC,
    regular_market_day_low NUMERIC,
    regular_market_day_high NUMERIC,
    volume BIGINT,
    regular_market_volume BIGINT,
    average_volume BIGINT,
    average_volume_10days BIGINT,
    average_daily_volume_10day BIGINT,
    bid NUMERIC,
    ask NUMERIC,
    market_cap NUMERIC,
    fifty_two_week_low NUMERIC,
    fifty_two_week_high NUMERIC,
    price_to_sales_trailing_12_months NUMERIC,
    fifty_day_average NUMERIC,
    two_hundred_day_average NUMERIC,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON market_info (company_code);
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