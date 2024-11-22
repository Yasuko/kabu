'''
市場情報 (MarketInfo)

'''

from model.schema.BalanceSheet import BalanceSheetType, BalanceSheetDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class BalanceSheet:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    # レコードの登録
    def insert_record(self, data: BalanceSheetType):
        q, v, i = query_convert(data, BalanceSheetType)
        query = f"""
        INSERT INTO
            balance_sheet
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
        data: BalanceSheetType,
    ) -> bool:
        query = f"""
        SELECT
            *
        FROM
            balance_sheet
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
        query = "DELETE FROM balance_sheet WHERE id = %s;"
        self.DB.execute(query, (id,))


    # company_codeからレコードを検索、Dateでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            balance_sheet 
        WHERE
            companyCode = %s 
        ORDER BY
            Date DESC 
        LIMIT 1;
        """
        record = self.DB.fetch_one(query, (company_code,))
        return record

