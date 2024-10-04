"""
 株価の分析データのDB操作を行うクラス
"""

from model.schema.AnalysisDate import AnalysisDateType, AnalysisDateDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class AnalysisDate:
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
    def add_data(self, data: AnalysisDateType):
        q, v, i = query_convert(data, AnalysisDateType)
        query = f"""
            INSERT INTO
                analysis_date
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
    
    # companyCodeとDateでデータの削除
    def delete_by_date_and_company_code(self, date, companyCode):
        query = """
        DELETE FROM
            analysis_date
        WHERE
            Date = %s
        AND companyCode = %s
        """
        self._DB.execute(query, (date, companyCode))

    # DateとcompanyCodeの重複がない場合のみ、データの追加
    def add_exists_by_date_and_company_code(
        self, date, companyCode, data: AnalysisDateType
    ) -> bool:
        query = f"""
        SELECT
            COUNT(*)
        FROM
            analysis_date
        WHERE
            Date = %s
        AND
            companyCode = %s
        """
        if self._DB.fetch_one(query, (date, companyCode)) == 0:
            self.add_data(data)
            return True
        return None

    # DateとcompanyCodeからデータを取得
    def get_by_date_and_company_code(self, date, companyCode):
        query = f"""
        SELECT
            *
        FROM
            analysis_date
        WHERE
            Date = %s
        AND
            companyCode = %s
        """
        return self._DB.fetch_all(query, (date, companyCode))

    def get_all_by_company_code(self, companyCode, getQuery = False):
        query = f"""
        SELECT
            *
        FROM
            analysis_date
        WHERE
            companyCode = %s
        """

        if getQuery:
            return print(query % companyCode)
        return self._DB.fetch_all(query, (companyCode,))

    # Dateから最新のデータ30件を取得
    def get_latest_data(self, date, limit = 30):
        query = f"""
        SELECT
            *
        FROM
            analysis_date
        WHERE
            Date = %s
        ORDER BY
            createdAt DESC
        LIMIT %s
        """
        return self._DB.fetch_all(query, (date, limit))

    # 指定日前から指定日までのデータを取得
    def get_data_by_date_range(
        self,
        companyCode,
        start_date,
        end_date
    ) -> list:
        query = f"""
        SELECT
            *
        FROM
            analysis_date
        WHERE
            companyCode = %s
        AND
            Date >= %s
        AND
            Date <= %s
        """
        return self._DB.fetch_all(query, (companyCode, start_date, end_date))