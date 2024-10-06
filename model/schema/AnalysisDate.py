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
    Rad1: list
    Rad2: list
    Rad3: list
    Rad4: list
    Rad5: list
    Rad6: list
    Rad7: list
    Rad8: list
    Rad9: list
    Rad10: list

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
        Rad1 NUMERIC[][] NOT NULL,
        Rad2 NUMERIC[][] NOT NULL,
        Rad3 NUMERIC[][] NOT NULL,
        Rad4 NUMERIC[][] NOT NULL,
        Rad5 NUMERIC[][] NOT NULL,
        Rad6 NUMERIC[][] NOT NULL,
        Rad7 NUMERIC[][] NOT NULL,
        Rad8 NUMERIC[][] NOT NULL,
        Rad9 NUMERIC[][] NOT NULL,
        Rad10 NUMERIC[][] NOT NULL,
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
