"""
 株価の分析データのDB操作を行うクラス
"""

from model.schema.RankVector20 import RankVector20Type, RankVector20DBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class RankVector20:
    _DB = None

    def __init__(self, DB = None):
        if DB is None:
            self._DB = PgSQL().connect()
        else:
            self._DB = DB
    
    @property
    def DB(self):
        return self._DB

    # データの追加
    def add_data(self, data: RankVector20Type):
        q, v, i = query_convert(data, RankVector20Type)
        query = f"""
            INSERT INTO
                rank_vector_20
            (
                {q}
            )
            VALUES
            (
                {v}
            )
        """
        result = self._DB.execute(query, (i))
        return result
    
    # idを指定してデータを削除
    def delete(self, id):
        query = "DELETE FROM rank_vector_20 WHERE id = %s"
        self._DB.execute(query, (id,))

    # companyCodeとDateでデータの削除
    def delete_by_date_and_company_code(self, date):
        query = f"""
        DELETE FROM
            rank_vector_20
        WHERE
            Date = %s
        """
        self._DB.execute(query, (date))

    # DateとCompanyCodeの重複がない場合のみ、データの追加
    def add_exists_by_date_and_company_code(
        self,
        date: str,
        companyCode: str,
        data: RankVector20Type
    ) -> bool:
        if not self.check_exists_by_date_and_company_code(date, companyCode):
            self.add_data(data)
            return True
        return None

    def check_exists_by_date_and_company_code(
        self,
        date: str,
        companyCode: str
    ) -> bool:
        query = f"""
        SELECT
            *
        FROM
            rank_vector_20
        WHERE
            Date = %s
        AND
            companyCode = %s
        """
        r = self._DB.fetch_all(query, (date, companyCode,))
        if len(r) <= 0:
            return False
        return True

    # Dateから最新のデータを取得
    def get_latest_data(self, date):
        query = f"""
        SELECT
            *
        FROM
            rank_vector_20
        WHERE
            Date = %s
        """
        return self._DB.fetch_one(query, (date))

    # 指定日前から指定日までのデータを取得
    def get_data_by_date_range(
        self,
        start_date,
        end_date
    ) -> list:
        query = f"""
        SELECT
            *
        FROM
            rank_vector_20
        WHERE
            Date >= %s
        AND
            Date <= %s
        """
        return self._DB.fetch_all(query, (start_date, end_date))