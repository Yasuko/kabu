"""
    統計解析情報のスキーマ定義
"""
from lib.utils import validate

class RankType:
    Date: str
    Day: float
    DayOne: list
    DayTwo: list
    DayThree: list
    WeekOne: list
    WeekTwo: list


class RankDBType(RankType):
    id: str
    createdAt: str

def ConvertToRankType(data: dict) -> RankType:
    result = {}
    for key in RankType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], RankType.__annotations__[key])
        else:
            result[key] = validate('', RankType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class Rank:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS rank (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        Date DATE NOT NULL,
        Day NUMERIC[] NOT NULL,
        DayOne NUMERIC[] NOT NULL,
        DayTwo NUMERIC[] NOT NULL,
        DayThree NUMERIC[] NOT NULL,
        WeekOne NUMERIC[] NOT NULL,
        WeekTwo NUMERIC[] NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON rank (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table rank')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
