'''
その他の情報 (other_information) テーブルのスキーマを定義

'''

'''
OtherInformationの型定義
'''
class OtherInformationType:
    company_code: str
    currency: str
    financial_currency: str
    trailing_peg_ratio: float
    exchange: str
    quote_type: str
    symbol: str
    underlying_symbol: str
    short_name: str
    long_name: str
    first_trade_date_epoch_utc: int
    time_zone_full_name: str
    time_zone_short_name: str
    uuid: str
    message_board_id: str
    gmt_offset_milliseconds: int
    current_price: float
    target_high_price: float
    target_low_price: float
    target_mean_price: float
    target_median_price: float
    recommendation_mean: float
    recommendation_key: str
    number_of_analyst_opinions: int

'''
OtherInformationのDB型定義
'''
class OtherInformationDBType(OtherInformationType):
    id: str
    createdAt: str

def ConvertToOtherInformationType(data: dict) -> OtherInformationType:
    return {
        'company_code': data['companyCode'],
        'currency': data['currency'],
        'financial_currency': data['financialCurrency'],
        'trailing_peg_ratio': data['trailingPegRatio'],
        'exchange': data['exchange'],
        'quote_type': data['quoteType'],
        'symbol': data['symbol'],
        'underlying_symbol': data['underlyingSymbol'],
        'short_name': data['shortName'],
        'long_name': data['longName'],
        'first_trade_date_epoch_utc': data['firstTradeDateEpochUtc'],
        'time_zone_full_name': data['timeZoneFullName'],
        'time_zone_short_name': data['timeZoneShortName'],
        'uuid': data['uuid'],
        'message_board_id': data['messageBoardId'],
        'gmt_offset_milliseconds': data['gmtOffSetMilliseconds'],
        'current_price': data['currentPrice'],
        'target_high_price': data['targetHighPrice'],
        'target_low_price': data['targetLowPrice'],
        'target_mean_price': data['targetMeanPrice'],
        'target_median_price': data['targetMedianPrice'],
        'recommendation_mean': data['recommendationMean'],
        'recommendation_key': data['recommendationKey'],
        'number_of_analyst_opinions': data['numberOfAnalystOpinions']
    }

'''
OtherInformationのスキーマ定義
'''
class OtherInformation:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS other_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(20),
    currency VARCHAR(10),
    financial_currency VARCHAR(10),
    trailing_peg_ratio NUMERIC,
    exchange VARCHAR(10),
    quote_type VARCHAR(10),
    symbol VARCHAR(10),
    underlying_symbol VARCHAR(10),
    short_name VARCHAR(50),
    long_name VARCHAR(100),
    first_trade_date_epoch_utc BIGINT,
    time_zone_full_name VARCHAR(50),
    time_zone_short_name VARCHAR(10),
    uuid UUID,
    message_board_id VARCHAR(50),
    gmt_offset_milliseconds BIGINT,
    current_price NUMERIC,
    target_high_price NUMERIC,
    target_low_price NUMERIC,
    target_mean_price NUMERIC,
    target_median_price NUMERIC,
    recommendation_mean NUMERIC,
    recommendation_key VARCHAR(10),
    number_of_analyst_opinions INTEGER,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON other_info (company_code);
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