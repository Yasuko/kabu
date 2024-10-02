"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class VectorMonthType:
    companyCode: str
    Date: str
    Vec: list

class VectorMonthDBType(VectorMonthType):
    id: str
    createdAt: str

def ConvertToVectorMonthType(data: dict) -> VectorMonthType:
    result = {}
    for key in VectorMonthType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], VectorMonthType.__annotations__[key])
        else:
            result[key] = validate('', VectorMonthType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class VectorMonth:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_month (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(10) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_month (companyCode);
    CREATE INDEX ON vector_month (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table vector_month')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
