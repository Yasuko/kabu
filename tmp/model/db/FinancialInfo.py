'''
財務情報 (financial_info) テーブルのスキーマを定義するモジュール

'''

from model.schema.FinancialInfo import FinancialInfoType, FinancialInfoDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class FinancialInfo:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    def insert_record(self, data: FinancialInfoType):
        q, v, i = query_convert(data, FinancialInfoType)
        query = f"""
        INSERT INTO financial_info (
            {q},
            createdAt
        ) VALUES (
            {v},
            NOW()
        )
        """
        self.DB.execute(query, (i))

    def update_record(self, id, **kwargs: FinancialInfoDBType):
        set_clause = ', '.join([f"{key} = %({key})s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            financial_info
        SET
            {set_clause}
        WHERE
            id = %s;
        """
        self.DB.execute(query, (*kwargs.values(), id))

    def delete_record(self, id: str):
        query = "DELETE FROM financial_info WHERE id = %s"
        self.DB.execute(query, (id,))

    def get_record_by_id(self, id):
        query = "SELECT * FROM financial_info WHERE id = %s"
        record = self.DB.fetch_one(query, (id,))
        return record

    def get_latest_records_by_company_code(self, company_code, limit=10):
        query = """
        SELECT * FROM
            financial_info
        WHERE
            companyCode = %s
        ORDER BY
            createdAt DESC
        LIMIT %s
        """
        records = self.DB.fetch_all(query, (company_code, limit))
        return records

    def get_latest_record_by_company_code(self, company_code):
        return self.get_latest_records_by_company_code(company_code, limit=1)[0]
