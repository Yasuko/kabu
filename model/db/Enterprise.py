'''
和名会社情報 (enterprise)

'''
from model.schema.Enterprise import EnterpriseType, EnterpriseDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class Enterprise:

    _DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self._DB = DB
        else:
            self._DB = PgSQL().connect()
    
    @property
    def DB(self):
        return self._DB
    
    # レコードの登録
    def insert_record(self, data: EnterpriseType):
        q, v, i = query_convert(data, EnterpriseType)
        query = f"""
        INSERT INTO
            enterprise
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
        new_id = self._DB.execute(query, (i))
        #print('Insert Industory new_id:', new_id)
        return new_id

    def add_exists_by_company_code(
        self, company_code, data: EnterpriseType
    ) -> bool:
        query = """
        SELECT
            *
        FROM
            enterprise
        WHERE
            companyCode = %s
        """
        #print(query % (company_code))
        r = self._DB.fetch_all(query, (company_code,))
        if len(r) <= 0:
            self.insert_record(data)
            return True
        return None


    # レコードの更新
    def update_record(self, id, **kwargs: EnterpriseDBType):
        set_clause = ', '.join([f"{key} = %({key})s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            enterprise
        SET
            {set_clause}
        WHERE
            id = %s;
        """
        self._DB.execute(query, (id, *kwargs))

    # レコードの削除
    def delete_record(self, id):
        query = "DELETE FROM enterprise WHERE id = %s;"
        self._DB.execute(query, (id,))

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM enterprise WHERE id = %s;"
        record = self._DB.fetch_one(query, (id,))
        return record

    # company_codeの重複を排除し、全てのレコードを取得し返す
    def get_all_records(self):
        query = f"""
        SELECT DISTINCT ON
            (companyCode) *
        FROM
            enterprise
        ORDER BY
            companyCode, createdAt DESC
        ;"""
        records = self._DB.fetch_all(query)
        return records
    
    # company_codeaでソート、重複を排除し、指定のCompanyCodeから後のレコードを取得し返す
    def get_records_by_company_code(self, company_code):
        query = f"""
        SELECT DISTINCT ON
            (companyCode) *
        FROM
            enterprise
        WHERE
            companyCode >= %s
        ORDER BY
            companyCode;
        """
        records = self._DB.fetch_all(query, (company_code,))
        return records

