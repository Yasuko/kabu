'''
役員情報 (company_officers) テーブルのスキーマを定義するモジュール
'''

from model.schema.CompanyOfficers import CompanyOfficersType, CompanyOfficersDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class CompanyOfficers:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    # レコードの登録
    def insert_record(self, data: list[CompanyOfficersType]):
        for d in data:
            print(d)
            q, v, i = query_convert(d, CompanyOfficersType)
            query = f"""
            INSERT INTO
                company_officers
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
            self.DB.execute(query, (i))



    # レコードの更新
    def update_record(self, id, **kwargs: CompanyOfficersDBType):
        set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            company_officers
        SET
            {set_clause}
        WHERE
            id = %s
        """
        self.DB.execute(query, (*kwargs.values(), id))

    # レコードの削除
    def delete_record(self, id):
        query = "DELETE FROM company_officers WHERE id = %s"
        self.DB.execute(query, (id,))

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM company_officers WHERE id = %s"
        record = self.DB.fetch_one(query, (id,))
        return record

    # company_codeからレコードを検索、createdAtでソートし最新の20件を取得し返す
    def get_latest_20_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            company_officers
        WHERE
            companyCode = %s
        ORDER BY
            createdAt DESC
        LIMIT 20
        """
        records = self.DB.fetch_all(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の5件を取得し返す
    def get_latest_5_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            company_officers
        WHERE
            companyCode = %s
        ORDER BY
            createdAt DESC
        LIMIT 5
        """
        records = self.DB.fetch_all(query, (company_code,))
        return records