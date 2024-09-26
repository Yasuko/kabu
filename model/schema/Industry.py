'''
企業情報 (industry)

'''

class IndustryType:
    company_code: str
    address1: str
    address2: str
    city: str
    zip: str
    country: str
    phone: str
    website: str
    industry: str
    industry_key: str
    industry_disp: str
    sector: str
    sector_key: str
    sector_disp: str
    long_business_summary: str
    full_time_employees: str


class IndustryDBType(IndustryType):
    id: str
    createdAt: str

def ConvertToIndustryType(data: dict) -> IndustryType:
    return {
        'company_code': data['companyCode'],
        'address1': data['address1'],
        'address2': data['address2'],
        'city': data['city'],
        'zip': data['zip'],
        'country': data['country'],
        'phone': data['phone'],
        'website': data['website'],
        'industry': data['industry'],
        'industry_key': data['industryKey'],
        'industry_disp': data['industryDisp'],
        'sector': data['sector'],
        'sector_key': data['sectorKey'],
        'sector_disp': data['sectorDisp'],
        'long_business_summary': data['longBusinessSummary'],
        'full_time_employees': data['fullTimeEmployees']
    }

class Industry:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS industry (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(20) UNIQUE,
    address1 VARCHAR(255),
    address2 VARCHAR(255),
    city VARCHAR(100),
    zip VARCHAR(20),
    country VARCHAR(100),
    phone VARCHAR(50),
    website VARCHAR(255),
    industry VARCHAR(100),
    industry_key VARCHAR(100),
    industry_disp VARCHAR(100),
    sector VARCHAR(100),
    sector_key VARCHAR(100),
    sector_disp VARCHAR(100),
    long_business_summary TEXT,
    full_time_employees VARCHAR(50),
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON industry (company_code);
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