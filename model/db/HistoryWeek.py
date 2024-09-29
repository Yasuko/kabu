"""
 株価データ breakdown
"""

from model.schema.HistoryWeek import HistoryWeekType, HistoryWeekDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class HistoryWeek:
    DB = None

    def __init__(self, DB = None):
        if DB is None:
            self.DB = PgSQL().connect()
        else:
            self.DB = DB

    # データの追加
    def add_data(self, data: HistoryWeekType):
        q, v, i = query_convert(data, HistoryWeekType)
        query = f"""
            INSERT INTO
                history_week
            (
                {q}
            )
            VALUES
            (
                {v}
            )
        """
        result = self.DB.execute(query, (i))
        return result

    # データの更新
    def update_data(self, id, **kwargs: HistoryWeekType):
        set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        query = f"""
            UPDATE history_week
            SET
                {set_clause}
            WHERE id = %s
        """
        self.DB.execute(query, (*kwargs.values(), id))

    # データの削除
    def delete_data(self, id):
        query = "DELETE FROM history_week WHERE id = %s"
        self.DB.execute(query, (id,))

    # Dateに重複がない場合のみ、データの追加
    def add_data_if_not_exists(self, date, data: HistoryWeekType):
        query = "SELECT COUNT(*) FROM history_week WHERE Date = %s"
        if self.DB.fetchone(query, (date,)) == 0:
            self.add_data(data)
            return True
        return None

    # idからデータを抜き出し
    def get_data_by_id(self, id):
        query = "SELECT * FROM history_week WHERE id = %s"
        return self.DB.fetchone(query, (id,))

    # Dateで絞り込み、companyCodeからデータを抜き出し
    def get_data_by_date_and_company_code(self, date, companyCode):
        query = "SELECT * FROM history_week WHERE Date = %s AND companyCode = %s"
        return self.DB.fetchall(query, (date, companyCode))

    # Dateで絞り込んだデータを抜き出し
    def get_data_by_date(self, date):
        query = "SELECT * FROM history_week WHERE Date = %s"
        return self.DB.fetchall(query, (date,))

