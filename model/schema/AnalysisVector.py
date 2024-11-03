"""
 統計解析情報のスキーマ定義
"""
from lib.utils import validate

class AnalysisVectorType:
    companyCode: str
    Date: str
    Result: float
    DayOne: float
    DayTwo: float
    DayThree: float
    WeekOne: float

class AnalysisVectorDBType(AnalysisVectorType):
    id: str
    createdAt: str

def ConvertToAnalysisVectorType(data: dict) -> AnalysisVectorType:
    result = {}
    for key in AnalysisVectorType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], AnalysisVectorType.__annotations__[key])
        else:
            result[key] = validate('', AnalysisVectorType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class AnalysisVector:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS analysis_vector (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Result NUMERIC NOT NULL,
        Day NUMERIC NOT NULL,
        DayOne NUMERIC NOT NULL,
        DayTwo NUMERIC NOT NULL,
        DayThree NUMERIC NOT NULL,
        WeekOne NUMERIC NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON analysis_vector (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table analysis_vector')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
