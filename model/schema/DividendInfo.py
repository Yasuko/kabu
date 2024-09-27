'''
配当情報 (DividendInfo) テーブルのスキーマを定義する
'''

from lib.utils import validate

class DividendInfoType:
    companyCode: str
    dividendRate: float
    dividendYield: float
    exDividendDate: int
    payoutRatio: float
    fiveYearAvgDividendYield: float
    trailingAnnualDividendRate: float
    trailingAnnualDividendYield: float
    lastDividendValue: float
    lastDividendDate: int

class DividendInfoDBType(DividendInfoType):
    id: str
    createdAt: str

def ConvertToDividendInfoType(data: dict) -> DividendInfoType:
    result = {}
    for key in DividendInfoType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], DividendInfoType.__annotations__[key])
        else:
            result[key] = validate('', DividendInfoType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class DividendInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS dividend_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20) NOT NULL,
    dividendRate NUMERIC,
    dividendYield NUMERIC,
    exDividendDate BIGINT,
    payoutRatio NUMERIC,
    fiveYearAvgDividendYield NUMERIC,
    trailingAnnualDividendRate NUMERIC,
    trailingAnnualDividendYield NUMERIC,
    lastDividendValue NUMERIC,
    lastDividendDate BIGINT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON dividend_info (companyCode);
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