'''
リスク情報 (RiskInfo) テーブルのスキーマを定義する
'''

from model.schema.RiskInfo import RiskInfoDBType, RiskInfoType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class RiskInfo:
    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    # レコードの登録
    def insert_record(self, data: RiskInfoType):
        q, v, i = query_convert(data, RiskInfoType)
        query = f"""
        INSERT INTO
            risk_info
        (
            {q},
            createdAt
        )
        VALUES
        (
            {v},
            NOW()
        )
        """
        result = self.DB.execute(query, (i))
        return result

    # レコードの更新
    def update_record(self, id: str, **kwargs: RiskInfoDBType):
        set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            risk_info
        SET
            {set_clause}
        WHERE
            id = %s"""
        self.DB.execute(query, (*kwargs.values(), id))

    # レコードの削除
    def delete_record(self, id):
        query = "DELETE FROM risk_info WHERE id = %s"
        self.DB.execute(query, (id,))

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM risk_info WHERE id = %s"
        record = self.DB.fetch_one(query, (id,))
        return record

    # company_codeからレコードを検索、createdAtでソートし最新の10件を取得し返す
    def get_latest_10_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            risk_info
        WHERE
            companyCode = %s
        ORDER BY
            createdAt DESC
        LIMIT 10
        """
        records = self.DB.fetch_all(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            risk_info
        WHERE
            companyCode = %s
        ORDER BY
            createdAt DESC
        LIMIT 1
        """
        record = self.DB.fetch_one(query, (company_code,))
        return record