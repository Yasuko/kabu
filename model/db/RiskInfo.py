'''
リスク情報 (RiskInfo) テーブルのスキーマを定義する
'''

from model.schema.RiskInfo import RiskInfoDBType
from lib.pgsql import Pgsql


class RiskInfo:
    DB = None

    def __init__(self, DB):
        self.DB = Pgsql.Pgsql().connect()
    
    # レコードの登録
    def insert_record(self, data: RiskInfoDBType):
        query = """
        INSERT INTO
            risk_info
        (
            company_code, audit_risk,
            board_risk, compensation_risk,
            shareholder_rights_risk, overall_risk,
            governance_epoch_date,
            compensation_as_of_epoch_date,
            max_age,
            createdAt
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW()
        )
        """
        self.DB.execute(query, (data,))

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
        record = self.DB.execute(query, (id,))
        return record

    # company_codeからレコードを検索、createdAtでソートし最新の10件を取得し返す
    def get_latest_10_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            risk_info
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT 10
        """
        records = self.DB.execute(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            risk_info
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT 1
        """
        record = self.DB.execute(query, (company_code,))
        return record