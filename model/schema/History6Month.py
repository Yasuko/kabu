"""
6ヶ月 株価データ breakdown
"""
from lib.utils import validate

class History6MonthType:
    companyCode: str
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Volume: float
    Dividends: float
    StockSplits: float

class History6MonthDBType(History6MonthType):
    id: str
    createdAt: str

def ConvertToHistory6MonthType(data: dict) -> History6MonthType:
    result = {}
    for key in History6MonthType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], History6MonthType.__annotations__[key])
        else:
            result[key] = validate('', History6MonthType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class History6Month:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS history_6month (
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
    CREATE INDEX ON history_6month (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table history_6month')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
