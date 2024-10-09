"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class Vector20Type:
    companyCode: str
    Date: str
    Vec: list

class Vector20DBType(Vector20Type):
    id: str
    createdAt: str

def ConvertToVector20Type(data: dict) -> Vector20Type:
    result = {}
    for key in Vector20Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], Vector20Type.__annotations__[key])
        else:
            result[key] = validate('', Vector20Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class Vector20:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_20 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(20) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_20 (companyCode);
    CREATE INDEX ON vector_20 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table vector_20')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
