"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class Vector30Type:
    companyCode: str
    Date: str
    Vec: list

class Vector30DBType(Vector30Type):
    id: str
    createdAt: str

def ConvertToVector30Type(data: dict) -> Vector30Type:
    result = {}
    for key in Vector30Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], Vector30Type.__annotations__[key])
        else:
            result[key] = validate('', Vector30Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class Vector30:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_30 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(30) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_30 (companyCode);
    CREATE INDEX ON vector_30 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table vector_30')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
