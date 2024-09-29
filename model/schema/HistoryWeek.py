"""
 株価データ breakdown
"""

from lib.utils import validate

class HistoryMonthType:
    companyCode: str
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Volume: float
    Dividends: float
    StockSplits: float

class HistoryMonthDBType(HistoryMonthType):
    id: str
    createdAt: str

def ConvertToHistoryMonthType(data: dict) -> HistoryMonthType:
    result = {}
    for key in HistoryMonthType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], HistoryMonthType.__annotations__[key])
        else:
            result[key] = validate('', HistoryMonthType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class HistoryWeek:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS history_week (
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
    CREATE INDEX ON history_week (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table history_week')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
