'''
リスク情報 (RiskInfo) テーブルのスキーマを定義する
'''
from lib.utils import validate

class RiskInfoType:
    companyCode: str
    auditRisk: int
    boardRisk: int
    compensationRisk: int
    shareHolderRightsRisk: int
    overallRisk: int
    governanceEpochDate: int
    compensationAsOfEpochDate: int
    maxAge: int

class RiskInfoDBType(RiskInfoType):
    id: str
    createdAt: int

def ConvertToRiskInfoType(data: dict) -> RiskInfoType:
    result = {}
    for key in RiskInfoType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], RiskInfoType.__annotations__[key])
        else:
            result[key] = validate('', RiskInfoType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class RiskInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS risk_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20),
    auditRisk INTEGER,
    boardRisk INTEGER,
    compensationRisk INTEGER,
    shareHolderRightsRisk INTEGER,
    overallRisk INTEGER,
    governanceEpochDate BIGINT,
    compensationAsOfEpochDate BIGINT,
    maxAge INTEGER,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON risk_info (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table risk info')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()