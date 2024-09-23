'''
財務情報 (financial_info) テーブルのスキーマを定義するモジュール

CREATE TABLE IF NOT EXISTS financial_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(7),
    enterprise_value NUMERIC,
    profit_margins NUMERIC,
    float_shares BIGINT,
    shares_outstanding BIGINT,
    held_percent_insiders NUMERIC,
    held_percent_institutions NUMERIC,
    implied_shares_outstanding BIGINT,
    book_value NUMERIC,
    price_to_book NUMERIC,
    last_fiscal_year_end BIGINT,
    next_fiscal_year_end BIGINT,
    most_recent_quarter BIGINT,
    net_income_to_common NUMERIC,
    trailing_eps NUMERIC,
    forward_eps NUMERIC,
    peg_ratio NUMERIC,
    last_split_factor VARCHAR(10),
    last_split_date BIGINT,
    enterprise_to_revenue NUMERIC,
    enterprise_to_ebitda NUMERIC,
    fifty_two_week_change NUMERIC,
    sandp_52_week_change NUMERIC,
    total_cash NUMERIC,
    total_cash_per_share NUMERIC,
    ebitda NUMERIC,
    total_debt NUMERIC,
    quick_ratio NUMERIC,
    current_ratio NUMERIC,
    total_revenue NUMERIC,
    debt_to_equity NUMERIC,
    revenue_per_share NUMERIC,
    return_on_assets NUMERIC,
    return_on_equity NUMERIC,
    free_cashflow NUMERIC,
    operating_cashflow NUMERIC,
    revenue_growth NUMERIC,
    gross_margins NUMERIC,
    ebitda_margins NUMERIC,
    operating_margins NUMERIC,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_company_code ON industry (company_code);
'''

class FinancialInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS financial_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(7),
    enterprise_value NUMERIC,
    profit_margins NUMERIC,
    float_shares BIGINT,
    shares_outstanding BIGINT,
    held_percent_insiders NUMERIC,
    held_percent_institutions NUMERIC,
    implied_shares_outstanding BIGINT,
    book_value NUMERIC,
    price_to_book NUMERIC,
    last_fiscal_year_end BIGINT,
    next_fiscal_year_end BIGINT,
    most_recent_quarter BIGINT,
    net_income_to_common NUMERIC,
    trailing_eps NUMERIC,
    forward_eps NUMERIC,
    peg_ratio NUMERIC,
    last_split_factor VARCHAR(10),
    last_split_date BIGINT,
    enterprise_to_revenue NUMERIC,
    enterprise_to_ebitda NUMERIC,
    fifty_two_week_change NUMERIC,
    sandp_52_week_change NUMERIC,
    total_cash NUMERIC,
    total_cash_per_share NUMERIC,
    ebitda NUMERIC,
    total_debt NUMERIC,
    quick_ratio NUMERIC,
    current_ratio NUMERIC,
    total_revenue NUMERIC,
    debt_to_equity NUMERIC,
    revenue_per_share NUMERIC,
    return_on_assets NUMERIC,
    return_on_equity NUMERIC,
    free_cashflow NUMERIC,
    operating_cashflow NUMERIC,
    revenue_growth NUMERIC,
    gross_margins NUMERIC,
    ebitda_margins NUMERIC,
    operating_margins NUMERIC,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_company_code ON industry (company_code);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table financial_info')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()