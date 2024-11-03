"""
    統計解析情報のスキーマ定義
"""
from lib.utils import validate

class RankVector100Type:
    Date: str
    DayOne: str
    DayTwo: str
    DayThree: str
    WeekOne: str

class RankVector100DBType(RankVector100Type):
    id: str
    createdAt: str

def ConvertToVector100Type(data: dict) -> RankVector100Type:
    result = {}
    for key in RankVector100Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], RankVector100Type.__annotations__[key])
        else:
            result[key] = validate('', RankVector100Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class RankVector100:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS rank_vector_100 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        Date DATE NOT NULL,
        DayOne TEXT NOT NULL,
        DayTwo TEXT NOT NULL,
        DayThree TEXT NOT NULL,
        WeekOne TEXT NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON rank_vector_100 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table rank_vector_100')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
