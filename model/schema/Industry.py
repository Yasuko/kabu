'''
企業情報 (industry)

'''
from lib.utils import validate

class IndustryType:
    companyCode: str
    address1: str
    address2: str
    city: str
    zip: str
    country: str
    phone: str
    website: str
    industry: str
    industryKey: str
    industryDisp: str
    sector: str
    sectorKey: str
    sectorDisp: str
    longBusinessSummary: str
    fullTimeEmployees: str

class IndustryDBType(IndustryType):
    id: str
    createdAt: str

def ConvertToIndustryType(data: dict) -> IndustryType:
    result = {}
    for key in IndustryType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], IndustryType.__annotations__[key])
        else:
            result[key] = validate('', IndustryType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class Industry:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS industry (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20),
    address1 VARCHAR(255),
    address2 VARCHAR(255),
    city VARCHAR(100),
    zip VARCHAR(20),
    country VARCHAR(100),
    phone VARCHAR(50),
    website VARCHAR(255),
    industry VARCHAR(100),
    industryKey VARCHAR(100),
    industryDisp VARCHAR(100),
    sector VARCHAR(100),
    sectorKey VARCHAR(100),
    sectorDisp VARCHAR(100),
    longBusinessSummary TEXT,
    fullTimeEmployees VARCHAR(50),
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON industry (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table industry')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()