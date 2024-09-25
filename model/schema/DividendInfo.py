'''
配当情報 (DividendInfo) テーブルのスキーマを定義する

'''

class DividendInfoType:
    company_code: str
    dividend_rate: float
    dividend_yield: float
    ex_dividend_date: int
    payout_ratio: float
    five_year_avg_dividend_yield: float
    trailing_annual_dividend_rate: float
    trailing_annual_dividend_yield: float
    last_dividend_value: float
    last_dividend_date: int

class DividendInfoDBType(DividendInfoType):
    id: str
    createdAt: str


class DividendInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS dividend_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(7),
    dividend_rate NUMERIC,
    dividend_yield NUMERIC,
    ex_dividend_date BIGINT,
    payout_ratio NUMERIC,
    five_year_avg_dividend_yield NUMERIC,
    trailing_annual_dividend_rate NUMERIC,
    trailing_annual_dividend_yield NUMERIC,
    last_dividend_value NUMERIC,
    last_dividend_date BIGINT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON dividend_info (company_code);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table dividend_info')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()