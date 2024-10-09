'''
リスク情報 (RiskInfo) テーブルのスキーマを定義する
'''

from model.schema.Vector20 import Vector20Type
from lib.pgsql import PgSQL
from lib.utils import query_convert

class Vector20:
    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    # レコードの登録
    def insert_record(self, data: Vector20Type):
        q, v, i = query_convert(data, Vector20Type)
        query = f"""
        INSERT INTO
            vector_20
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
        self, date, companyCode, data: Vector20Type
    ) -> bool:
        query = "SELECT COUNT(*) FROM vector_20 WHERE Date = %s AND companyCode = %s"
        if self.DB.fetch_one(query, (date, companyCode)) == 0:
            self.insert_record(data)
            return True
        return False

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM vector_20 WHERE id = %s"
        record = self.DB.fetch_one(query, (id,))
        return record

    # ベクトルデータからユークリッド距離で検索
    def get_distance_by_vec(self, vec, limit = 10):
        query = f"""
        SELECT
            *,
            vec <-> %s AS distance
        FROM
            vector_20
        ORDER BY
            distance
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (vec,))
        return records
    
    # ベクトルデータから内積で検索
    def get_dot_by_vec(self, vec, limit = 10):
        query = f"""
        SELECT
            *,
            (vec <#> %s AS) * -1 AS dot
        FROM
            vector_20
        ORDER BY
            dot
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (vec,))
        return records

    # ベクトルデータからコサイン類似度で検索
    def get_similarity_by_vec(self, vec, limit = 10):
        query = f"""
        SELECT
            *,
            1 - (vec <=> %s) AS similality
        FROM
            vector_20
        ORDER BY
            cosine
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (vec,))
        return records
