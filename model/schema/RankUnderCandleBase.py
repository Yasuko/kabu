"""
    統計解析情報のスキーマ定義
"""
from lib.utils import validate

class RankUnderCandleBaseType:
    Date: str
    Day: str
    DayOne: str
    DayTwo: str
    DayThree: str
    WeekOne: str

class RankUnderCandleBaseDBType(RankUnderCandleBaseType):
    id: str
    createdAt: str

def ConvertToRankUnderCandleBaseType(data: dict) -> RankUnderCandleBaseType:
    result = {}
    for key in RankUnderCandleBaseType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], RankUnderCandleBaseType.__annotations__[key])
        else:
            result[key] = validate('', RankUnderCandleBaseType.__annotations__[key])
    return result

class RankUnderCandleBase:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS rank_under_candle_base ( 
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        Date Date NOT NULL,
        Day TEXT NOT NULL,
        DayOne TEXT NOT NULL,
        DayTwo TEXT NOT NULL,
        DayThree TEXT NOT NULL,
        WeekOne TEXT NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON rank_under_candle_base (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table rank_under_candle_base')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
