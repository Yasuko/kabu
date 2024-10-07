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
    After1: list
    After1Pressure: list
    After2: list
    After2Pressure: list
    After3: list
    After3Pressure: list
    After4: list
    After4Pressure: list
    After5: list
    After5Pressure: list
    After6: list
    After6Pressure: list
    After7: list
    After7Pressure: list
    After8: list
    After8Pressure: list
    After9: list
    After9Pressure: list
    After10: list
    After10Pressure: list


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
        After1 NUMERIC[] NOT NULL,
        After1Pressure NUMERIC[] NOT NULL,
        After2 NUMERIC[] NOT NULL,
        After2Pressure NUMERIC[] NOT NULL,
        After3 NUMERIC[] NOT NULL,
        After3Pressure NUMERIC[] NOT NULL,
        After4 NUMERIC[] NOT NULL,
        After4Pressure NUMERIC[] NOT NULL,
        After5 NUMERIC[] NOT NULL,
        After5Pressure NUMERIC[] NOT NULL,
        After6 NUMERIC[] NOT NULL,
        After6Pressure NUMERIC[] NOT NULL,
        After7 NUMERIC[] NOT NULL,
        After7Pressure NUMERIC[] NOT NULL,
        After8 NUMERIC[] NOT NULL,
        After8Pressure NUMERIC[] NOT NULL,
        After9 NUMERIC[] NOT NULL,
        After9Pressure NUMERIC[] NOT NULL,
        After10 NUMERIC[] NOT NULL,
        After10Pressure NUMERIC[] NOT NULL,
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
