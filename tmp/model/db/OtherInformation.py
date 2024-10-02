'''
その他の情報 (other_information) テーブルのスキーマを定義
'''

from model.schema.OtherInformation import OtherInformationType, OtherInformationDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class OtherInformation:
    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    def insert_record(self, data: OtherInformationDBType):
        q, v, i = query_convert(data, OtherInformationType)
        query = f"""
        INSERT INTO
            other_info
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

    def update_record(self, id: str, **kwargs: OtherInformationDBType):
        set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        query = f"""
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
        record = self.DB.fetch_one(query, (id,))
        return record

    def get_latest_records_by_company_code(self, company_code: str, limit=10):
        query = """
        SELECT * FROM
            other_info
        WHERE
            companyCode = %s
        ORDER BY
            createdAt DESC
        LIMIT %s
        """
        records = self.DB.fetch_all(query, (company_code, limit))
        return records

    def get_latest_record_by_company_code(self, company_code: str):
        return self.get_latest_records_by_company_code(company_code, limit=1)[0]