"""
    統計解析情報のスキーマ定義
"""
from lib.utils import validate

class RankVector20Type:
    Date: str
    companyCode: str
    VecPrice: list
    VecVolume: list

class RankVector20DBType(RankVector20Type):
    id: str
    createdAt: str

def ConvertToVector20Type(data: dict) -> RankVector20Type:
    result = {}
    for key in RankVector20Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], RankVector20Type.__annotations__[key])
        else:
            result[key] = validate('', RankVector20Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class RankVector20:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS rank_vector_20 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        Date DATE NOT NULL,
        companyCode VARCHAR(20) NOT NULL,
        VecPrice NUMERIC[] NOT NULL,
        VecVolume NUMERIC[] NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON rank_vector_20 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table rank_vector_20')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
