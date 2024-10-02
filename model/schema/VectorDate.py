"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class VectorDateType:
    companyCode: str
    Date: str
    Vec: list

class VectorDateDBType(VectorDateType):
    id: str
    createdAt: str

def ConvertToVectorDateType(data: dict) -> VectorDateType:
    result = {}
    for key in VectorDateType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], VectorDateType.__annotations__[key])
        else:
            result[key] = validate('', VectorDateType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class VectorDate:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_date (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(10) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_date (companyCode);
    CREATE INDEX ON vector_date (Date);
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
