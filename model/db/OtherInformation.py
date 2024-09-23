'''
その他の情報 (other_information) テーブルのスキーマを定義

CREATE TABLE IF NOT EXISTS other_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    industry_id UUID NOT NULL,
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

'''

class OtherInformation:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS other_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    industry_id UUID NOT NULL,
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
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table info')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()