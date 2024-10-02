"""
 べクトルデータのスキーマ定義
"""
from lib.utils import validate

class VectorWeekType:
    companyCode: str
    Date: str
    Vec: list

class VectorWeekDBType(VectorWeekType):
    id: str
    createdAt: str

def ConvertToVectorWeekType(data: dict) -> VectorWeekType:
    result = {}
    for key in VectorWeekType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], VectorWeekType.__annotations__[key])
        else:
            result[key] = validate('', VectorWeekType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class VectorWeek:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vector_week (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Vec vector(10) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON vector_week (companyCode);
    CREATE INDEX ON vector_week (Date);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table vector_week')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
