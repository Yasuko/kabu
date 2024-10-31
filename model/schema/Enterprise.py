'''
企業情報 (industry)

'''
from lib.utils import validate

class EnterpriseType:
    companyCode: str
    stockName: str
    marketProductCategory: str
    industryCode33: str
    industryCategory33: str
    industryCode17: str
    industryCategory17: str
    scaleCode: str
    scaleCategory: str

class EnterpriseDBType(EnterpriseType):
    id: str
    createdAt: str

def ConvertToEnterpriseType(data: dict) -> EnterpriseType:
    result = {}
    for key in EnterpriseType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], EnterpriseType.__annotations__[key])
        else:
            result[key] = validate('', EnterpriseType.__annotations__[key])
    return result

class Enterprise:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS enterprise (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20),
    stockName VARCHAR(255),
    marketProductCategory VARCHAR(255),
    industryCode33 VARCHAR(20),
    industryCategory33 VARCHAR(255),
    industryCode17 VARCHAR(20),
    industryCategory17 VARCHAR(255),
    scaleCode VARCHAR(20),
    scaleCategory VARCHAR(255),
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON enterprise (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table enterprise')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()