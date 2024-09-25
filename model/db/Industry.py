'''
企業情報 (industry)

'''

from model.schema.Industry import IndustryType, IndustryDBType
from lib.pgsql import Pgsql

class Industry:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = Pgsql.Pgsql().connect()
    
    # レコードの登録
    def insert_record(self, data: IndustryType):
        query = """
        INSERT INTO
            industry
        (
            company_code, address1, address2,
            city, zip, country, phone, website,
            industry, industry_key, industry_disp,
            sector, sector_key, sector_disp,
            long_business_summary, full_time_employees,
            createdAt
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, NOW()
        )
        RETURNING id;
        """
        new_id = self.DB.fetchOne(query, (data,))
        return new_id

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
        self.DB.execute(query, (id, *kwargs))

    # レコードの削除
    def delete_record(self, id):
        query = "DELETE FROM industry WHERE id = %s;"
        self.DB.execute(query, (id,))

    # idからレコードを1件検索し返す
    def get_record_by_id(self, id):
        query = "SELECT * FROM industry WHERE id = %s;"
        record = self.DB.fetchOne(query, (id,))
        return record

    # company_codeからレコードを検索、createdAtでソートし最新の5件を取得し返す
    def get_latest_5_records_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            industry
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT 5;
        """
        records = self.DB.fetchAll(query, (company_code,))
        return records

    # company_codeからレコードを検索、createdAtでソートし最新の1件を取得し返す
    def get_latest_record_by_company_code(self, company_code):
        query = """
        SELECT * FROM
            industry
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT 1;
        """
        record = self.DB.fetchOne(query, (company_code,))
        return record

    # idからレコードを1件検索し、他のテーブルをcompany_codeでjoinし返す
    def get_record_with_joins_by_id(self, id: str):
        query = """
        SELECT
            i.*, co.*, di.*, fi.*, mi.*, oi.*, ri.*
        FROM
            industry i
        LEFT JOIN
            company_officers co ON i.company_code = co.company_code
        LEFT JOIN
            dividend_info di ON i.company_code = di.company_code
        LEFT JOIN
            financial_info fi ON i.company_code = fi.company_code
        LEFT JOIN
            market_info mi ON i.company_code = mi.company_code
        LEFT JOIN
            other_information oi ON i.company_code = oi.company_code
        LEFT JOIN
            risk_info ri ON i.company_code = ri.company_code
        WHERE
            i.id = %s;
        """
        record = self.DB.fetchOne(query, (id,))
        return record

    # company_codeからレコードを検索し、他のテーブルをcompany_codeでjoinし、createdAtでソートし最新の5件を取得し返す
    def get_latest_5_records_with_joins_by_company_code(self, company_code):
        query = """
        SELECT
            i.*, co.*, di.*, fi.*, mi.*, oi.*, ri.*
        FROM
            industry i
        LEFT JOIN
            company_officers co ON i.company_code = co.company_code
        LEFT JOIN
            dividend_info di ON i.company_code = di.company_code
        LEFT JOIN
            financial_info fi ON i.company_code = fi.company_code
        LEFT JOIN
            market_info mi ON i.company_code = mi.company_code
        LEFT JOIN
            other_information oi ON i.company_code = oi.company_code
        LEFT JOIN
            risk_info ri ON i.company_code = ri.company_code
        WHERE
            i.company_code = %s
        ORDER BY
            i.createdAt DESC
        LIMIT 5;
        """
        records = self.DB.fetchAll(query, (company_code,))
        return records