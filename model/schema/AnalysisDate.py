"""
 統計解析情報のスキーマ定義
"""
from lib.utils import validate

class AnalysisDateType:
    companyCode: str
    Date: str
    Day: float
    DayOne: float
    DayTwo: float
    DayThree: float
    WeekOne: float
    WeekTwo: float
    PressDay: float
    PressOne: float
    PressTwo: float
    PressThree: float
    PressWeekOne: float
    PressWeekTwo: float
    Rad: list

class AnalysisDateDBType(AnalysisDateType):
    id: str
    createdAt: str

def ConvertToAnalysisDateType(data: dict) -> AnalysisDateType:
    result = {}
    for key in AnalysisDateType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], AnalysisDateType.__annotations__[key])
        else:
            result[key] = validate('', AnalysisDateType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class AnalysisDate:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS analysis_date (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        Day NUMERIC NOT NULL,
        DayOne NUMERIC NOT NULL,
        DayTwo NUMERIC NOT NULL,
        DayThree NUMERIC NOT NULL,
        WeekOne NUMERIC NOT NULL,
        WeekTwo NUMERIC NOT NULL,
        PressDay NUMERIC NOT NULL,
        PressOne NUMERIC NOT NULL,
        PressTwo NUMERIC NOT NULL,
        PressThree NUMERIC NOT NULL,
        PressWeekOne NUMERIC NOT NULL,
        PressWeekTwo NUMERIC NOT NULL,
        Rad NUMERIC[] NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON analysis_date (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table analysis_date')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
