'''
市場情報 (MarketInfo)

'''

from model.schema.Financials import FinancialsType, FinancialsDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class Financials:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    # レコードの登録
    def insert_record(self, data: FinancialsType):
        q, v, i = query_convert(data, FinancialsType)
        query = f"""
        INSERT INTO
            financials
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
        data: FinancialsType,
    ) -> bool:
        query = f"""
        SELECT
            *
        FROM
            financials
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

    # レコードの削除
    def delete_record(self, id: str):
        query = "DELETE FROM financials WHERE id = %s;"
        self.DB.execute(query, (id,))


    # company_codeからレコードを検索、Dateでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            financials 
        WHERE
            companyCode = %s 
        ORDER BY
            Date DESC 
        LIMIT 1;
        """
        record = self.DB.fetch_one(query, (company_code,))
        return record

