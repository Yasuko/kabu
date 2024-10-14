"""
    統計解析情報のスキーマ定義
"""
from lib.utils import validate

class RankVector30Type:
    Vec1: str
    Vec1After: list
    Vec2: str
    Vec2After: list
    Vec3: str
    Vec3After: list
    Vec4: str
    Vec4After: list
    Vec5: str
    Vec5After: list
    Vec6: str
    Vec6After: list
    Vec7: str
    Vec7After: list
    Vec8: str
    Vec8After: list
    Vec9: str
    Vec9After: list
    Vec10: str
    Vec10After: list

class RankVector30DBType(RankVector30Type):
    id: str
    createdAt: str

def ConvertToVector10Type(data: dict) -> RankVector30Type:
    result = {}
    for key in RankVector30Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], RankVector30Type.__annotations__[key])
        else:
            result[key] = validate('', RankVector30Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class RankVector10:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS rank_vector_30 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        Date DATE NOT NULL,
        Vec1 VARCHAR(20) NOT NULL,
        Vec1After NUMERIC[] NOT NULL,
        Vec2 VARCHAR(20) NOT NULL,
        Vec2After NUMERIC[] NOT NULL,
        Vec3 VARCHAR(20) NOT NULL,
        Vec3After NUMERIC[] NOT NULL,
        Vec4 VARCHAR(20) NOT NULL,
        Vec4After NUMERIC[] NOT NULL,
        Vec5 VARCHAR(20) NOT NULL,
        Vec5After NUMERIC[] NOT NULL,
        Vec6 VARCHAR(20) NOT NULL,
        Vec6After NUMERIC[] NOT NULL,
        Vec7 VARCHAR(20) NOT NULL,
        Vec7After NUMERIC[] NOT NULL,
        Vec8 VARCHAR(20) NOT NULL,
        Vec8After NUMERIC[] NOT NULL,
        Vec9 VARCHAR(20) NOT NULL,
        Vec9After NUMERIC[] NOT NULL,
        Vec10 VARCHAR(20) NOT NULL,
        Vec10After NUMERIC[] NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON rank_vector_30 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table rank_vector_30')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
