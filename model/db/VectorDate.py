'''
リスク情報 (RiskInfo) テーブルのスキーマを定義する
'''

from model.schema.VectorDate import VectorDateType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class VectorDate:
    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = PgSQL().connect()
    
    # レコードの登録
    def insert_record(self, data: VectorDateType):
        q, v, i = query_convert(data, VectorDateType)
        query = f"""
        INSERT INTO
            vector_date
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
        data: VectorDateType,
    ) -> bool:
        query = f"""
        SELECT
            COUNT(*)
        FROM
            vector_date
        WHERE
            Date = %s
        AND
            companyCode = %s
        """
        if self.DB.fetch_one(query, (date, companyCode)) == 0:
            self.insert_record(data)
            return True
        return False

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM vector_date WHERE id = %s"
        record = self.DB.fetch_one(query, (id,))
        return record

    # ベクトルデータからユークリッド距離で検索
    def get_distance_by_vec(self, vec, limit = 10):
        array_str = '[' + ', '.join([str(d) for d in vec]) + ']'
        query = f"""
        SELECT
            Date, companyCode,
            Vec <-> %s AS distance
        FROM
            vector_date
        ORDER BY
            distance
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (array_str,))
        return records
    
    # ベクトルデータから内積で検索
    def get_dot_by_vec(self, vec, limit = 10):
        array_str = '[' + ', '.join([str(d) for d in vec]) + ']'
        query = f"""
        SELECT
            Date, companyCode,
            (Vec <#> %s ) * -1 AS dot
        FROM
            vector_date
        ORDER BY
            dot
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (array_str,))
        return records

    # ベクトルデータからコサイン類似度で検索
    def get_similarity_by_vec(self, vec, limit = 10):
        array_str = '[' + ', '.join([str(d) for d in vec]) + ']'
        print(array_str)
        query = f"""
        SELECT
            Date, companyCode,
            1 - (Vec <=> %s) AS similality
        FROM
            vector_date
        ORDER BY
            similality DESC
        LIMIT {limit}
        """
        records = self.DB.fetch_all(query, (array_str,))
        return records
