"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class Vector10Type:
    companyCode: str
    Date: str
    Vec: list

class VectorDateDBType(Vector10Type):
    id: str
    createdAt: str

def ConvertToVector10Type(data: dict) -> Vector10Type:
    result = {}
    for key in Vector10Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], Vector10Type.__annotations__[key])
        else:
            result[key] = validate('', Vector10Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class Vector10:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_10 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(10) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_10 (companyCode);
    CREATE INDEX ON vector_10 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table vector_date')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
