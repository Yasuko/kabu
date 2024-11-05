"""
 統計解析情報のスキーマ定義
"""
from lib.utils import validate

class AnalysisVector100Type:
    companyCode: str
    Date: str
    DayOne: float
    DayOneResult: str
    DayTwo: float
    DayTwoResult: str
    DayThree: float
    DayThreeResult: str
    WeekOne: float
    WeekOneResult: str

class AnalysisVector100DBType(AnalysisVector100Type):
    id: str
    createdAt: str

def ConvertToAnalysisVector100Type(data: dict) -> AnalysisVector100Type:
    result = {}
    for key in AnalysisVector100Type.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], AnalysisVector100Type.__annotations__[key])
        else:
            result[key] = validate('', AnalysisVector100Type.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class AnalysisVector100:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS analysis_vector100 (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        DayOne NUMERIC NOT NULL
        DayOneResult TEXT NOT NULL,
        DayTwo NUMERIC NOT NULL,
        DayTwoResult TEXT NOT NULL,
        DayThree NUMERIC NOT NULL,
        DayThreeResult TEXT NOT NULL,
        WeekOne NUMERIC NOT NULL,
        WeekOneResult TEXT NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON analysis_vector100 (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table analysis_vector100')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
