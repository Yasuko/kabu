"""
 株価データ breakdown
"""

from lib.utils import validate

class HistoryYearType:
    companyCode: str
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Volume: float
    Dividends: float
    StockSplits: float

class HistoryYearDBType(HistoryYearType):
    id: str
    createdAt: str

def ConvertToHistoryYearType(data: dict) -> HistoryYearType:
    result = {}
    for key in HistoryYearType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], HistoryYearType.__annotations__[key])
        else:
            result[key] = validate('', HistoryYearType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class HistoryYear:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS history_year (
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
    CREATE INDEX ON history_year (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table history_year')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
