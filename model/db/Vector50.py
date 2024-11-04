'''
リスク情報 (RiskInfo) テーブルのスキーマを定義する
'''

from model.schema.Vector50 import Vector50Type
from lib.pgsql import PgSQL
from lib.utils import query_convert

class Vector50:
    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    # レコードの登録
    def insert_record(self, data: Vector50Type):
        q, v, i = query_convert(data, Vector50Type)
        query = f"""
        INSERT INTO
            vector_50
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
        data: Vector50Type,
    ) -> bool:
        query = f"""
        SELECT
            *
        FROM
            vector_50
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

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM vector_50 WHERE id = %s"
        record = self.DB.fetch_one(query, (id,))
        return record

    # ベクトルデータからユークリッド距離で検索
    def get_distance_by_vec(self, vec, limit = 10):
        array_str = '[' + ', '.join([str(d) for d in vec]) + ']'
        query = f"""
        SELECT
            Date,
            companyCode,
            Vec <-> %s AS distance
        FROM
            vector_50
        ORDER BY
            distance DESC
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (array_str,))
        return records
    
    # ベクトルデータから内積で検索
    def get_dot_by_vec(self, vec, limit = 10):
        array_str = '[' + ', '.join([str(d) for d in vec]) + ']'
        query = f"""
        SELECT
            Date,
            companyCode,
            (Vec <#> %s) * -1 AS dot
        FROM
            vector_50
        ORDER BY
            dot ASC
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (array_str,))
        return records

    # ベクトルデータからコサイン類似度で検索
    def get_similarity_by_vec(self, vec, limit = 10):
        array_str = '[' + ', '.join([str(d) for d in vec]) + ']'
        query = f"""
        SELECT
            Date,
            companyCode,
            1 - (Vec <=> %s) AS similality
        FROM
            vector_50
        ORDER BY
            similality DESC
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (array_str,))
        return records
