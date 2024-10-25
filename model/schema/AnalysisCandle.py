"""
 統計解析情報のスキーマ定義
"""
from lib.utils import validate

class AnalysisCandleType:
    companyCode: str
    Date: str
    DayScore: int
    DayUp: int
    DayDown: int
    DayTrends: list
    DayOneScore: int
    DayOneUp: int
    DayOneDown: int
    DayOneTrends: list
    DayTwoScore: int
    DayTwoUp: int
    DayTwoDown: int
    DayTwoTrends: list
    DayThreeScore: int
    DayThreeUp: int
    DayThreeDown: int
    DayThreeTrends: list
    WeekOneScore: int
    WeekOneUp: int
    WeekOneDown: int
    WeekOneTrends: list


class AnalysisCandleDBType(AnalysisCandleType):
    id: str
    createdAt: str

def ConvertToAnalysisCandleType(data: dict) -> AnalysisCandleType:
    result = {}
    for key in AnalysisCandleType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], AnalysisCandleType.__annotations__[key])
        else:
            result[key] = validate('', AnalysisCandleType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

class AnalysisCandle:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS analysis_candle (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        companyCode VARCHAR(20) NOT NULL,
        Date DATE NOT NULL,
        DayScore INTEGER NOT NULL,
        DayUp INTEGER NOT NULL,
        DayDown INTEGER NOT NULL,
        DayTrends VARCHAR(10)[] NOT NULL,
        DayOneScore INTEGER NOT NULL,
        DayOneUp INTEGER NOT NULL,
        DayOneDown INTEGER NOT NULL,
        DayOneTrends VARCHAR(10)[] NOT NULL,
        DayTwoScore INTEGER NOT NULL,
        DayTwoUp INTEGER NOT NULL,
        DayTwoDown INTEGER NOT NULL,
        DayTwoTrends VARCHAR(10)[] NOT NULL,
        DayThreeScore INTEGER NOT NULL,
        DayThreeUp INTEGER NOT NULL,
        DayThreeDown INTEGER NOT NULL,
        DayThreeTrends VARCHAR(10)[] NOT NULL,
        WeekOneScore INTEGER NOT NULL,
        WeekOneUp INTEGER NOT NULL,
        WeekOneDown INTEGER NOT NULL,
        WeekOneTrends VARCHAR(10)[] NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX ON analysis_candle (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table analysis_candle')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
