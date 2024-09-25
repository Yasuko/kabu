'''
役員情報 (company_officers) テーブルのスキーマを定義するモジュール
'''

class CompanyOfficersType:
    company_code: str
    max_age: int
    name: str
    age: int
    title: str
    year_born: int
    fiscal_year: int
    total_pay: int
    exercised_value: int
    unexercised_value: int

class CompanyOfficersDBType(CompanyOfficersType):
    id: str
    createdAt: str

class CompanyOfficers:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS company_officers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(7),
    max_age INTEGER,
    name VARCHAR(255),
    age INTEGER,
    title VARCHAR(255),
    year_born INTEGER,
    fiscal_year INTEGER,
    total_pay BIGINT,
    exercised_value BIGINT,
    unexercised_value BIGINT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON company_officers (company_code);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table company_officers')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()