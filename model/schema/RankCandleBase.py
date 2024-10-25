"""
    統計解析情報のスキーマ定義
"""
from lib.utils import validate

class RankCandleBaseType:
    Date: str
    Day: str
    DayOne: str
    DayTwo: str
    DayThree: str
    WeekOne: str

class RankCandleBaseDBType(RankCandleBaseType):
    id: str
    createdAt: str

def ConvertToRankCandleBaseType(data: dict) -> RankCandleBaseType:
    result = {}
    for key in RankCandleBaseType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], RankCandleBaseType.__annotations__[key])
        else:
            result[key] = validate('', RankCandleBaseType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class RankCandleBase:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS rank_candle_base ( 
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        Date Date NOT NULL,
        Day TEXT NOT NULL,
        DayOne TEXT NOT NULL,
        DayTwo TEXT NOT NULL,
        DayThree TEXT NOT NULL,
        WeekOne TEXT NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON rank_candle_base (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table rank_candle_base')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
