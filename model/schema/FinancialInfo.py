'''
財務情報 (financial_info) テーブルのスキーマを定義するモジュール

'''

class FinancialInfoType:
    company_code: str
    enterprise_value: float
    profit_margins: float
    float_shares: int
    shares_outstanding: int
    held_percent_insiders: float
    held_percent_institutions: float
    implied_shares_outstanding: int
    book_value: float
    price_to_book: float
    last_fiscal_year_end: int
    next_fiscal_year_end: int
    most_recent_quarter: int
    net_income_to_common: float
    trailing_eps: float
    forward_eps: float
    peg_ratio: float
    last_split_factor: str
    last_split_date: int
    enterprise_to_revenue: float
    enterprise_to_ebitda: float
    sandp_52_week_change: float
    total_cash: float
    total_cash_per_share: float
    ebitda: float
    total_debt: float
    quick_ratio: float
    current_ratio: float
    total_revenue: float
    debt_to_equity: float
    revenue_per_share: float
    return_on_assets: float
    return_on_equity: float
    free_cashflow: float
    operating_cashflow: float
    revenue_growth: float
    gross_margins: float
    ebitda_margins: float
    operating_margins: float

class FinancialInfoDBType(FinancialInfoType):
    id: str
    createdAt: str

def ConvertToFinancialInfoType(data: dict) -> FinancialInfoType:
    return {
        'company_code': data['companyCode'],
        'enterprise_value': float(data['enterpriseValue']),
        'profit_margins': float(data['profitMargins']),
        'float_shares': int(data['floatShares']),
        'shares_outstanding': int(data['sharesOutstanding']),
        'held_percent_insiders': float(data['heldPercentInsiders']),
        'held_percent_institutions': float(data['heldPercentInstitutions']),
        'implied_shares_outstanding': int(data['impliedSharesOutstanding']),
        'book_value': float(data['bookValue']),
        'price_to_book': float(data['priceToBook']),
        'last_fiscal_year_end': int(data['lastFiscalYearEnd']),
        'next_fiscal_year_end': int(data['nextFiscalYearEnd']),
        'most_recent_quarter': int(data['mostRecentQuarter']),
        'net_income_to_common': float(data['netIncomeToCommon']),
        'trailing_eps': float(data['trailingEps']),
        'forward_eps': float(data['forwardEps']),
        'peg_ratio': float(data['pegRatio']),
        'last_split_factor': data['lastSplitFactor'],
        'last_split_date': int(data['lastSplitDate']),
        'enterprise_to_revenue': float(data['enterpriseToRevenue']),
        'enterprise_to_ebitda': float(data['enterpriseToEbitda']),
        'sandp_52_week_change': float(data['SandP52WeekChange']),
        'total_cash': float(data['totalCash']),
        'total_cash_per_share': float(data['totalCashPerShare']),
        'ebitda': float(data['ebitda']),
        'total_debt': float(data['totalDebt']),
        'quick_ratio':float( data['quickRatio']),
        'current_ratio': float(data['currentRatio']),
        'total_revenue': float(data['totalRevenue']),
        'debt_to_equity': float(data['debtToEquity']),
        'revenue_per_share': float(data['revenuePerShare']),
        'return_on_assets': float(data['returnOnAssets']),
        'return_on_equity': float(data['returnOnEquity']),
        'free_cashflow': float(data['freeCashflow']),
        'operating_cashflow': float(data['operatingCashflow']),
        'revenue_growth': float(data['revenueGrowth']),
        'gross_margins': float(data['grossMargins']),
        'ebitda_margins': float(data['ebitdaMargins']),
        'operating_margins': float(data['operatingMargins'])

    }

class FinancialInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS financial_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(20) NOT NULL REFERENCES industry(company_code),
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
CREATE INDEX ON financial_info (company_code);
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