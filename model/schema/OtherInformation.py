from lib.utils import validate

'''
その他の情報 (other_information) テーブルのスキーマを定義
'''

from lib.utils import validate

'''
OtherInformationの型定義
'''
class OtherInformationType:
    companyCode: str
    currency: str
    financialCurrency: str
    trailingPegRatio: float
    exchange: str
    quoteType: str
    symbol: str
    underlyingSymbol: str
    shortName: str
    longName: str
    firstTradeDateEpochUtc: int
    timeZoneFullName: str
    timeZoneShortName: str
    uuid: str
    messageBoardId: str
    gmtOffsetMilliseconds: int
    currentPrice: float
    targetHighPrice: float
    targetLowPrice: float
    targetMeanPrice: float
    targetMedianPrice: float
    recommendationMean: float
    recommendationKey: str
    numberOfAnalystOpinions: int

'''
OtherInformationのDB型定義
'''
class OtherInformationDBType(OtherInformationType):
    id: str
    createdAt: str

def ConvertToOtherInformationType(data: dict) -> OtherInformationType:
    result = {}
    for key in OtherInformationType.__annotations__.keys():
        if key in data:
            result[key] = validate(data[key], OtherInformationType.__annotations__[key])
        else:
            result[key] = validate('', OtherInformationType.__annotations__[key])
    #print('Validate Test: ', result)
    return result

'''
OtherInformationのスキーマ定義
'''
class OtherInformation:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS other_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20),
    currency VARCHAR(10),
    financialCurrency VARCHAR(10),
    trailingPegRatio NUMERIC,
    exchange VARCHAR(10),
    quoteType VARCHAR(10),
    symbol VARCHAR(10),
    underlyingSymbol VARCHAR(10),
    shortName VARCHAR(50),
    longName VARCHAR(100),
    firstTradeDateEpochUtc BIGINT,
    timeZoneFullName VARCHAR(50),
    timeZoneShortName VARCHAR(10),
    uuid UUID,
    messageBoardId VARCHAR(50),
    gmtOffsetMilliseconds BIGINT,
    currentPrice NUMERIC,
    targetHighPrice NUMERIC,
    targetLowPrice NUMERIC,
    targetMeanPrice NUMERIC,
    targetMedianPrice NUMERIC,
    recommendationMean NUMERIC,
    recommendationKey VARCHAR(20),
    numberOfAnalystOpinions INTEGER,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON other_info (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table otherinformation')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()