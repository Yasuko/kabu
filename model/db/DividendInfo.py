'''
配当情報 (DividendInfo) テーブルのスキーマを定義する

'''

from model.schema.DividendInfo import DividendInfoDBType, DividendInfoType
from lib.pgsql import Pgsql

class DividendInfo:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = Pgsql.Pgsql().connect()
    
    # レコードの登録
    def insert_record(self, data: DividendInfoType):
        query = """
        INSERT INTO
            dividend_info
        (
            company_code, dividend_rate, dividend_yield,
            ex_dividend_date, payout_ratio, 
            five_year_avg_dividend_yield,
            trailing_annual_dividend_rate,
            trailing_annual_dividend_yield, 
            last_dividend_value, last_dividend_date, createdAt
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW()
        );
        RETURNING id;
        """
        self.DB.execute(query, (data,))
        new_id = self.DB.fetchone()[0]
        return new_id

    # レコードの更新
    def update_record(self, id, **kwargs: DividendInfoDBType):
        set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            dividend_info
        SET
            {set_clause}
        WHERE
            id = %s;
        """
        self.DB.execute(query, (*kwargs.values(), id))

    # レコードの削除
    def delete_record(self, id):
        query = "DELETE FROM dividend_info WHERE id = %s;"
        self.DB.execute(query, (id,))


    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM dividend_info WHERE id = %s;"
        record = self.DB.fetchOne(query, (id,))
        return record

    # company_codeからレコードを検索、createdAtでソートし最新の10件を取得し返す
    def get_latest_10_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            dividend_info 
        WHERE
            company_code = %s 
        ORDER BY
            createdAt DESC 
        LIMIT 10;
        """
        records = self.DB.fetchAll(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            dividend_info 
        WHERE
            company_code = %s 
        ORDER BY
            createdAt DESC 
        LIMIT 1;
        """
        record = self.DB.fetchOne(query, (company_code,))
        return record