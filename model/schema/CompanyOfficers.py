'''
役員情報 (company_officers) テーブルのスキーマを定義するモジュール
'''

from lib.utils import validate

class CompanyOfficersType:
    companyCode: str
    maxAge: int
    name: str
    age: int
    title: str
    yearBorn: int
    fiscalYear: int
    totalPay: int
    exercisedValue: int
    unexercisedValue: int

class CompanyOfficersDBType(CompanyOfficersType):
    id: str
    createdAt: str

def ConvertToCompanyOfficersType(
    company_code: str,
    data: list[dict]
) -> list[CompanyOfficersType]:
    officers = []
    for d in data:
        result = {
            'companyCode': company_code
        }
        for key in CompanyOfficersType.__annotations__.keys():
            if key in d:
                result[key] = validate(d[key], CompanyOfficersType.__annotations__[key])
            else:
                result[key] = validate('', CompanyOfficersType.__annotations__[key])
        #print('Validate Test: ', result)
        officers.append(result)
    return officers

class CompanyOfficers:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS company_officers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20) NOT NULL,
    maxAge INTEGER,
    name VARCHAR(255),
    age INTEGER,
    title VARCHAR(255),
    yearBorn INTEGER,
    fiscalYear INTEGER,
    totalPay BIGINT,
    exercisedValue BIGINT,
    unexercisedValue BIGINT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON company_officers (companyCode);
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