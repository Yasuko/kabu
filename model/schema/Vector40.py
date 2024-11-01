"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class Vector40Type:
    companyCode: str
    Date: str
    Vec: list

class Vector40DBType(Vector40Type):
    id: str
    createdAt: str

def ConvertToVector40Type(data: dict) -> Vector40Type:
    result = {}
    for key in Vector40Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], Vector40Type.__annotations__[key])
        else:
            result[key] = validate('', Vector40Type.__annotations__[key])
    return result

class Vector40:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_40 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(40) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_40 (companyCode);
    CREATE INDEX ON vector_40 (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table vector_40')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
