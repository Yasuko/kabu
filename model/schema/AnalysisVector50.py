"""
 統計解析情報のスキーマ定義
"""
from lib.utils import validate

class AnalysisVector50Type:
    companyCode: str
    Date: str
    Score: float
    VecList: str

class AnalysisVector50DBType(AnalysisVector50Type):
    id: str
    createdAt: str

def ConvertToAnalysisVectorType(data: dict) -> AnalysisVector50Type:
    result = {}
    for key in AnalysisVector50Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], AnalysisVector50Type.__annotations__[key])
        else:
            result[key] = validate('', AnalysisVector50Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class AnalysisVector:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS analysis_vector50 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Score FLOAT NOT NULL,
        VecList TEXT NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON analysis_vector50 (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table analysis_vector50')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
