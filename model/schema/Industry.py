'''
企業情報 (industry)

CREATE TABLE IF NOT EXISTS industry (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(7),
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
CREATE INDEX idx_company_code ON industry (company_code);
'''

class Industry:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS industry (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(7) UNIQUE,
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