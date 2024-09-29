"""
3ヶ月 株価データ breakdown
"""

from lib.utils import validate

class History3MonthType:
    companyCode: str
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Volume: float
    Dividends: float
    StockSplits: float

class History3MonthDBType(History3MonthType):
    id: str
    createdAt: str

def ConvertToHistory3MonthType(data: dict) -> History3MonthType:
    result = {}
    for key in History3MonthType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], History3MonthType.__annotations__[key])
        else:
            result[key] = validate('', History3MonthType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class History3Month:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS history_3month (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Open NUMERIC NOT NULL,
        High NUMERIC NOT NULL,
        Low NUMERIC NOT NULL,
        Close NUMERIC NOT NULL,
        Volume NUMERIC NOT NULL,
        Dividends NUMERIC NOT NULL,
        StockSplits NUMERIC NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON history_3month (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table history_3month')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
