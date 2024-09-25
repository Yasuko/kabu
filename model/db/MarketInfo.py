'''
市場情報 (MarketInfo)

'''

from model.schema.MarketInfo import MarketInfoType, MarketInfoDBType
from lib.pgsql import Pgsql

class MarketInfo:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = Pgsql.Pgsql().connect()
    
    # レコードの登録
    def insert_record(self, data: MarketInfoType):
        query = """
        INSERT INTO
            market_info
        (
            company_code, industry_id, price_hint,
            previous_close, open, day_low, day_high, 
            regular_market_previous_close,
            regular_market_open, regular_market_day_low, 
            regular_market_day_high, volume,
            regular_market_volume, average_volume, 
            average_volume_10days, average_daily_volume_10day,
            bid, ask, market_cap, fifty_two_week_low,
            fifty_two_week_high, price_to_sales_trailing_12_months, 
            fifty_day_average, two_hundred_day_average, createdAt
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            NOW()
        )
        RETURNING id;
        """
        new_id = self.DB.fetchOne(query, (data,))
        return new_id

    # レコードの更新
    def update_record(self, id, **kwargs: MarketInfoDBType):
        set_clause = ', '.join([f"{key} = %({key})s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            market_info
        SET
            {set_clause}
        WHERE
            id = %s;
        """
        self.DB.execute(query, (id, *kwargs))

    # レコードの削除
    def delete_record(self, id: str):
        query = "DELETE FROM market_info WHERE id = %s;"
        self.DB.execute(query, (id,))

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM market_info WHERE id = %s;"
        record = self.DB.fetchOne(query, (id,))
        return record

    # company_codeからレコードを検索、createdAtでソートし最新の10件を取得し返す
    def get_latest_10_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            market_info 
        WHERE
            company_code = %s 
        ORDER BY
            createdAt DESC 
        LIMIT 5;
        """
        records = self.DB.fetchAll(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            market_info 
        WHERE
            company_code = %s 
        ORDER BY
            createdAt DESC 
        LIMIT 1;
        """
        record = self.DB.fetchOne(query, (company_code,))
        return record

