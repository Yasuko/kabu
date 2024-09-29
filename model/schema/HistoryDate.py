"""
 株価データ breakdown
"""
from lib.utils import validate

class HistoryDateType:
    companyCode: str
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Volume: float
    Dividends: float
    StockSplits: float

class HistoryDateDBType(HistoryDateType):
    id: str
    createdAt: str

def ConvertToHistoryDateType(data: dict) -> HistoryDateType:
    result = {}
    for key in HistoryDateType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], HistoryDateType.__annotations__[key])
        else:
            result[key] = validate('', HistoryDateType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class HistoryDate:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS history_date (
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
    CREATE INDEX ON history_date (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table history_date')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
