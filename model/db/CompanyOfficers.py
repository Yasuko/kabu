'''
役員情報 (company_officers) テーブルのスキーマを定義するモジュール
'''

from model.schema.CompanyOfficers import CompanyOfficersType, CompanyOfficersDBType

class CompanyOfficers:

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    # レコードの登録
    def insert_record(self, data: CompanyOfficersType):
        query = """
        INSERT INTO
            company_officers
        (
            company_code, max_age, name,
            age, title, year_born, fiscal_year,
            total_pay, exercised_value,
            unexercised_value, createdAt
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW()
        )
        """
        self.DB.execute(query, (data,))

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
        record = self.DB.execute(query, (id,))
        return record

    # company_codeからレコードを検索、createdAtでソートし最新の20件を取得し返す
    def get_latest_20_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            company_officers
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT 20
        """
        records = self.DB.execute(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の5件を取得し返す
    def get_latest_5_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            company_officers
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT 5
        """
        records = self.DB.execute(query, (company_code,))
        return records