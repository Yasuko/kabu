"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class Vector50Type:
    companyCode: str
    Date: str
    Vec: list

class Vector50DBType(Vector50Type):
    id: str
    createdAt: str

def ConvertToVector50Type(data: dict) -> Vector50Type:
    result = {}
    for key in Vector50Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], Vector50Type.__annotations__[key])
        else:
            result[key] = validate('', Vector50Type.__annotations__[key])
    return result

class Vector50:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_50 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(50) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_50 (companyCode);
    CREATE INDEX ON vector_50 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table vector_50')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
