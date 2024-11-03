"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class Vector100Type:
    companyCode: str
    Date: str
    Vec: list

class Vector100DBType(Vector100Type):
    id: str
    createdAt: str

def ConvertToVector80Type(data: dict) -> Vector100Type:
    result = {}
    for key in Vector100Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], Vector100Type.__annotations__[key])
        else:
            result[key] = validate('', Vector100Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class Vector100:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_100 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(100) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_100 (companyCode);
    CREATE INDEX ON vector_100 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table vector_100')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
