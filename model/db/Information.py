'''
市場情報 (MarketInfo)

'''

from model.schema.Information import InformationType, InformationDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class Information:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    # レコードの登録
    def insert_record(self, data: InformationType):
        q, v, i = query_convert(data, InformationType)
        query = f"""
        INSERT INTO
            information
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

    # DateとcompanyCodeの重複がない場合のみ、データの追加
    def insert_exists_by_date_and_company_code(
        self,
        date,
        companyCode,
        data: InformationType,
    ) -> bool:
        query = f"""
        SELECT
            *
        FROM
            information
        WHERE
            Date = %s
        AND
            companyCode = %s
        """
        r = self.DB.fetch_all(query, (date, companyCode))
        if len(r) <= 0:
            self.insert_record(data)
            return True

        return False

    # レコードの更新
    def update_record(self, id, **kwargs: InformationType):
        set_clause = ', '.join([f"{key} = %({key})s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            information
        SET
            {set_clause}
        WHERE
            id = %s;
        """
        self.DB.execute(query, (id, *kwargs))

    # レコードの削除
    def delete_record(self, id: str):
        query = "DELETE FROM information WHERE id = %s;"
        self.DB.execute(query, (id,))

    # 最新のDateで登録された全てのレコードを取得し返す
    def get_all_records(self):
        query = f"""
        SELECT * FROM
            information
        WHERE
            Date = %s
        ORDER BY
            Date DESC;
        """
        date = self.get_latest_date()
        records = self.DB.fetch_all(query, (date,))
        return records


    # company_codeからレコードを検索、createdAtでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            information 
        WHERE
            companyCode = %s 
        ORDER BY
            createdAt DESC 
        LIMIT 1;
        """
        record = self.DB.fetch_one(query, (company_code,))
        return record

    # 最新のレコードのDateを取得
    def get_latest_date(self):
        query = """
        SELECT
            Date
        FROM
            information
        ORDER BY
            createdAt DESC
        LIMIT 1;
        """
        record = self.DB.fetch_one(query)
        return record
