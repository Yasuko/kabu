'''
財務情報 (financial_info) テーブルのスキーマを定義するモジュール

'''

from model.schema.FinancialInfo import FinancialInfoType, FinancialInfoDBType
from lib.pgsql import Pgsql

class FinancialInfo:

    DB = None

    def __init__(self, DB = None):
        if DB is not None:
            self.DB = DB
        else:
            self.DB = Pgsql.Pgsql().connect()
    
    def insert_record(self, data: FinancialInfoType):
        query = """
        INSERT INTO financial_info (
            company_code, enterprise_value, profit_margins,
            float_shares, shares_outstanding,
            held_percent_insiders, held_percent_institutions,
            implied_shares_outstanding, book_value,
            price_to_book, last_fiscal_year_end,
            next_fiscal_year_end, most_recent_quarter,
            net_income_to_common, trailing_eps,
            forward_eps, peg_ratio, last_split_factor,
            last_split_date, enterprise_to_revenue,
            enterprise_to_ebitda, fifty_two_week_change,
            sandp_52_week_change, total_cash,
            total_cash_per_share, ebitda, total_debt, quick_ratio,
            current_ratio, total_revenue, debt_to_equity,
            revenue_per_share, return_on_assets,
            return_on_equity, free_cashflow, operating_cashflow,
            revenue_growth, gross_margins,
            ebitda_margins, operating_margins, createdAt
        ) VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, NOW()
        )
        """
        self.DB.execute(query, (data, ))

    def update_record(self, id, **kwargs: FinancialInfoDBType):
        set_clause = ', '.join([f"{key} = %({key})s" for key in kwargs.keys()])
        query = f"""
        UPDATE
            financial_info
        SET
            {set_clause}
        WHERE
            id = %s;
        """
        self.DB.execute(query, (*kwargs.values(), id))

    def delete_record(self, id: str):
        query = "DELETE FROM financial_info WHERE id = %s"
        self.DB.execute(query, (id,))

    def get_record_by_id(self, id):
        query = "SELECT * FROM financial_info WHERE id = %s"
        record = self.DB.fetchOne(query, (id,))
        return record

    def get_latest_records_by_company_code(self, company_code, limit=10):
        query = """
        SELECT * FROM
            financial_info
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT %s
        """
        records = self.DB.fetchAll(query, (company_code, limit))
        return records

    def get_latest_record_by_company_code(self, company_code):
        return self.get_latest_records_by_company_code(company_code, limit=1)[0]
