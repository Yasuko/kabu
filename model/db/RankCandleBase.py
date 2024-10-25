"""
 株価の分析データのDB操作を行うクラス
"""

from model.schema.RankCandleBase import RankCandleBaseType, RankCandleBaseDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class RankCandleBase:
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
    def add_data(self, data: RankCandleBaseType):
        q, v, i = query_convert(data, RankCandleBaseType)
        query = f"""
            INSERT INTO
                rank_candle_base
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
        query = "DELETE FROM rank_candle_base WHERE id = %s"
        self._DB.execute(query, (id,))

    # companyCodeとDateでデータの削除
    def delete_by_date_and_company_code(self, date):
        query = """
        DELETE FROM
            rank_candle_base
        WHERE
            Date = %s
        """
        self._DB.execute(query, (date))

    # Dateの重複がない場合のみ、データの追加
    def add_exists_by_date(
        self, date, data: RankCandleBaseType
    ) -> bool:
        query = f"""
        SELECT
            *
        FROM
            rank_candle_base
        WHERE
            Date = %s
        """
        r = self._DB.fetch_all(query, (date,))
        if len(r) <= 0:
            self.add_data(data)
            return True
        return None

    # Dateから最新のデータを取得
    def get_latest_data(self, date):
        query = f"""
        SELECT
            *
        FROM
            rank_candle_base
        WHERE
            Date = %s
        """
        return self._DB.fetch_one(query, (date,))

    def get_by_date(self, date):
        query = f"""
        SELECT
            *
        FROM
            rank_candle_base
        WHERE
            Date = %s
        """
        return self._DB.fetch_all(query, (date,))
    
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
            rank_candle_base
        WHERE
            Date >= %s
        AND
            Date <= %s
        """
        return self._DB.fetch_all(query, (start_date, end_date))