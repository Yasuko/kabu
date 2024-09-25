'''
その他の情報 (other_information) テーブルのスキーマを定義
'''

from model.schema.OtherInformation import OtherInformationType
from model.schema.OtherInformation import OtherInformationDBType

class OtherInformation:
    # テーブル作成クエリ

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def insert_record(self, data: OtherInformationDBType):
        query = """
        INSERT INTO
            other_info
        (
            company_code, currency, financial_currency,
            trailing_peg_ratio, exchange, quote_type,
            symbol, underlying_symbol, short_name, long_name,
            first_trade_date_epoch_utc, time_zone_full_name,
            time_zone_short_name, uuid, message_board_id,
            gmt_offset_milliseconds, current_price,
            target_high_price, target_low_price, target_mean_price,
            target_median_price, recommendation_mean,
            recommendation_key, number_of_analyst_opinions,
            createdAt
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, NOW()
        )
        """
        self.DB.execute(query, (data,))

    def update_record(self, id: str, **kwargs: OtherInformationDBType):
        set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        query = """
        UPDATE
            other_info
        SET
            {set_clause}
        WHERE
            id = %s
        """
        self.DB.execute(query, (*kwargs.values(), id))

    def delete_record(self, id: str):
        query = "DELETE FROM other_info WHERE id = %s"
        self.DB.execute(query, (id,))

    def get_record_by_id(self, id: str):
        query = "SELECT * FROM other_info WHERE id = %s"
        record = self.DB.fetchOne(query, (id,))
        return record

    def get_latest_records_by_company_code(self, company_code: str, limit=10):
        query = """
        SELECT * FROM
            other_info
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT %s
        """
        records = self.DB.fetchAll(query, (company_code, limit))
        return records

    def get_latest_record_by_company_code(self, company_code: str):
        return self.get_latest_records_by_company_code(company_code, limit=1)[0]