'''
企業情報 (industry)

'''
from model.schema.Industry import IndustryType, IndustryDBType
from lib.pgsql import PgSQL
from lib.utils import query_convert

class Industry:

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
    def insert_record(self, data: IndustryType):
        q, v, i = query_convert(data, IndustryType)
        query = f"""
        INSERT INTO
            industry
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

    # 72時間以内に登録されたレコードがない場合、新規登録
    def insert_record_if_not_exists(self, data: IndustryType):
        query = """
        SELECT
            id
        FROM
            industry
        WHERE
            companyCode = %s
        AND
            createdAt >= NOW() - INTERVAL '72 hours';
        """
        record = self._DB.fetch_one(query, (data['companyCode'],))
        if record is None:
            self.insert_record(data)

    # レコードの更新
    def update_record(self, id, **kwargs: IndustryDBType):
        set_clause = ', '.join([f"{key} = %({key})s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            industry
        SET
            {set_clause}
        WHERE
            id = %s;
        """
        self._DB.execute(query, (id, *kwargs))

    # レコードの削除
    def delete_record(self, id):
        query = "DELETE FROM industry WHERE id = %s;"
        self._DB.execute(query, (id,))

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM industry WHERE id = %s;"
        record = self._DB.fetch_one(query, (id,))
        return record

    # company_codeの重複を排除し、全てのレコードを取得し返す
    def get_all_records(self):
        query = "SELECT DISTINCT ON (companyCode) * FROM industry;"
        records = self._DB.fetch_all(query)
        return records
    
    # company_codeaでソート、重複を排除し、指定のCompanyCodeから後のレコードを取得し返す
    def get_records_by_company_code(self, company_code):
        query = f"""
        SELECT DISTINCT ON (companyCode)
            *
        FROM
            industry
        WHERE
            companyCode >= %s
        ORDER BY
            companyCode;
        """
        records = self._DB.fetch_all(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の5件を取得し返す
    def get_latest_5_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            industry
        WHERE
            companyCode = %s
        ORDER BY
            createdAt DESC
        LIMIT 5;
        """
        records = self._DB.fetch_all(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            industry
        WHERE
            companyCode = %s
        ORDER BY
            createdAt DESC
        LIMIT 1;
        """
        record = self._DB.fetch_one(query, (company_code,))
        return record

    # idからレコードを1件検索し、他のテーブルをcompany_codeでjoinし返す
    def get_record_with_joins_by_id(self, id: str):
        query = """
        SELECT
            i.*, co.*, di.*, fi.*, mi.*, oi.*, ri.*
        FROM
            industry i
        LEFT JOIN
            company_officers co ON i.companyCode = co.companyCode
        LEFT JOIN
            dividend_info di ON i.companyCode = di.companyCode
        LEFT JOIN
            financial_info fi ON i.companyCode = fi.companyCode
        LEFT JOIN
            market_info mi ON i.companyCode = mi.companyCode
        LEFT JOIN
            other_information oi ON i.companyCode = oi.companyCode
        LEFT JOIN
            risk_info ri ON i.companyCode = ri.companyCode
        WHERE
            i.id = %s;
        """
        record = self._DB.fetch_one(query, (id,))
        return record

    # company_codeからレコードを検索し、他のテーブルをcompany_codeでjoinし、createdAtでソートし最新の5件を取得し返す
    def get_latest_5_records_with_joins_by_company_code(self, company_code):
        query = """
        SELECT
            i.*, co.*, di.*, fi.*, mi.*, oi.*, ri.*
        FROM
            industry i
        LEFT JOIN
            company_officers co ON i.companyCode = co.companyCode
        LEFT JOIN
            dividend_info di ON i.companyCode = di.companyCode
        LEFT JOIN
            financial_info fi ON i.companyCode = fi.companyCode
        LEFT JOIN
            market_info mi ON i.companyCode = mi.companyCode
        LEFT JOIN
            other_information oi ON i.companyCode = oi.companyCode
        LEFT JOIN
            risk_info ri ON i.companyCode = ri.companyCode
        WHERE
            i.companyCode = %s
        ORDER BY
            i.createdAt DESC
        LIMIT 5;
        """
        records = self._DB.fetch_all(query, (company_code,))
        return records