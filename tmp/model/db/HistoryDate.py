"""
 株価１日単位株価データ
"""

from model.schema.HistoryDate import HistoryDateType, HistoryDateDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class HistoryDate:
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
    def add_data(self, data: HistoryDateType):
        q, v, i = query_convert(data, HistoryDateType)
        query = f"""
            INSERT INTO
                history_date
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

    # データの更新
    def update_data(self, id, **kwargs: HistoryDateType):
        set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        query = f"""
            UPDATE history_date
            SET
                {set_clause}
            WHERE id = %s
        """
        self._DB.execute(query, (*kwargs.values(), id))

    # データの削除
    def delete_data(self, id):
        query = "DELETE FROM history_date WHERE id = %s"
        self._DB.execute(query, (id,))

    # DateとcompanyCodeの重複がない場合のみ、データの追加
    def add_data_if_not_exists_by_date_and_company_code(
        self, date, companyCode, data: HistoryDateType
    ) -> bool:
        query = "SELECT COUNT(*) FROM history_date WHERE Date = %s AND companyCode = %s"
        if self._DB.fetch_one(query, (date, companyCode)) == 0:
            self.add_data(data)
            return True
        return None

    # Dateに重複がない場合のみ、データの追加
    def add_data_if_not_exists(self, date, data: HistoryDateType):
        query = "SELECT COUNT(*) FROM history_date WHERE Date = %s"
        if self._DB.fetch_one(query, (date,)) == 0:
            self.add_data(data)
            return True
        return None
    
    # DateとcompanyCodeからデータを取得
    def get_data_by_date_and_company_code(self, date, companyCode):
        query = "SELECT * FROM history_date WHERE Date = %s AND companyCode = %s"
        return self._DB.fetch_all(query, (date, companyCode))

    # idからデータを抜き出し
    def get_data_by_id(self, id):
        query = "SELECT * FROM history_date WHERE id = %s"
        return self._DB.fetch_one(query, (id,))

    # Dateで絞り込み、companyCodeからデータを抜き出し
    def get_data_by_date_and_company_code(self, date, companyCode):
        query = "SELECT * FROM history_date WHERE Date = %s AND companyCode = %s"
        return self._DB.fetch_all(query, (date, companyCode))

    # Dateで絞り込んだデータを抜き出し
    def get_data_by_date(self, date):
        query = "SELECT * FROM history_date WHERE Date = %s"
        return self._DB.fetch_all(query, (date,))

    def get_all_data_by_company_code(self, companyCode, getQuery = False):
        query = "SELECT * FROM history_date WHERE companyCode = '" + str(companyCode) + "'"

        if getQuery:
            return query
        return self._DB.fetch_all(query)
    
    # 指定日前から指定日までのデータを取得
    def get_data_by_date_range(
        self,
        companyCode,
        start_date,
        end_date
    ) -> list:
        query = "SELECT * FROM history_date WHERE companyCode = %s AND Date >= %s AND Date <= %s"
        return self._DB.fetch_all(query, (companyCode, start_date, end_date))