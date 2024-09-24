import yfinance as yf
from lib.pgsql import Pgsql

# DB接続
db = Pgsql.Pgsql().connect()
msft = yf.Ticker("9984.T")

data = msft.info
#r = msft.history(start="2022-12-10", end="2022-12-20", period="1d")

#print(r)



# Industryテーブルへのデータ挿入
industry_data = (
    data['uuid'], data['symbol'], data['address1'], data['address2'], data['city'], data['zip'], data['country'],
    data['phone'], data['website'], data['industry'], data['industryKey'], data['industryDisp'], data['sector'],
    data['sectorKey'], data['sectorDisp'], data['longBusinessSummary'], data['fullTimeEmployees']
)
db.execute("""
    INSERT INTO industry (id, company_code, address1, address2, city, zip, country, phone, website, industry, industry_key, industry_disp, sector, sector_key, sector_disp, long_business_summary, full_time_employees)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", industry_data)

# CompanyOfficersテーブルへのデータ挿入
for officer in data['companyOfficers']:
    officer_data = (
        data['uuid'], data['symbol'], officer['maxAge'], officer['name'], officer.get('age'), officer['title'],
        officer.get('yearBorn'), officer['fiscalYear'], officer['totalPay'], officer['exercisedValue'], officer['unexercisedValue']
    )
db.execute("""
    INSERT INTO company_officers (id, company_code, max_age, name, age, title, year_born, fiscal_year, total_pay, exercised_value, unexercised_value)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", officer_data)

# RiskInfoテーブルへのデータ挿入
risk_info_data = (
    data['uuid'], data['symbol'], data['auditRisk'], data['boardRisk'], data['compensationRisk'], data['shareHolderRightsRisk'],
    data['overallRisk'], data['governanceEpochDate'], data['compensationAsOfEpochDate'], data['maxAge']
)
db.execute("""
    INSERT INTO risk_info (id, company_code, audit_risk, board_risk, compensation_risk, shareholder_rights_risk, overall_risk, governance_epoch_date, compensation_as_of_epoch_date, max_age)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", risk_info_data)

# MarketInfoテーブルへのデータ挿入
market_info_data = (
    data['uuid'], data['symbol'], data['uuid'], data['priceHint'], data['previousClose'], data['open'], data['dayLow'], data['dayHigh'],
    data['regularMarketPreviousClose'], data['regularMarketOpen'], data['regularMarketDayLow'], data['regularMarketDayHigh'], data['volume'],
    data['regularMarketVolume'], data['averageVolume'], data['averageVolume10days'], data['averageDailyVolume10Day'], data['bid'], data['ask'],
    data['marketCap'], data['fiftyTwoWeekLow'], data['fiftyTwoWeekHigh'], data['priceToSalesTrailing12Months'], data['fiftyDayAverage'],
    data['twoHundredDayAverage']
)
db.execute("""
    INSERT INTO market_info (id, company_code, industry_id, price_hint, previous_close, open, day_low, day_high, regular_market_previous_close, regular_market_open, regular_market_day_low, regular_market_day_high, volume, regular_market_volume, average_volume, average_volume_10days, average_daily_volume_10day, bid, ask, market_cap, fifty_two_week_low, fifty_two_week_high, price_to_sales_trailing_12_months, fifty_day_average, two_hundred_day_average)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", market_info_data)

# FinancialInfoテーブルへのデータ挿入
financial_info_data = (
    data['uuid'], data['symbol'], data['enterpriseValue'], data['profitMargins'], data['floatShares'], data['sharesOutstanding'],
    data['heldPercentInsiders'], data['heldPercentInstitutions'], data['impliedSharesOutstanding'], data['bookValue'], data['priceToBook'],
    data['lastFiscalYearEnd'], data['nextFiscalYearEnd'], data['mostRecentQuarter'], data['netIncomeToCommon'], data['trailingEps'],
    data['forwardEps'], data['pegRatio'], data['lastSplitFactor'], data['lastSplitDate'], data['enterpriseToRevenue'], data['enterpriseToEbitda'],
    data['52WeekChange'], data['SandP52WeekChange'], data['totalCash'], data['totalCashPerShare'], data['ebitda'], data['totalDebt'],
    data['quickRatio'], data['currentRatio'], data['totalRevenue'], data['debtToEquity'], data['revenuePerShare'], data['returnOnAssets'],
    data['returnOnEquity'], data['freeCashflow'], data['operatingCashflow'], data['revenueGrowth'], data['grossMargins'], data['ebitdaMargins'],
    data['operatingMargins']
)
db.execute("""
    INSERT INTO financial_info (id, company_code, enterprise_value, profit_margins, float_shares, shares_outstanding, held_percent_insiders, held_percent_institutions, implied_shares_outstanding, book_value, price_to_book, last_fiscal_year_end, next_fiscal_year_end, most_recent_quarter, net_income_to_common, trailing_eps, forward_eps, peg_ratio, last_split_factor, last_split_date, enterprise_to_revenue, enterprise_to_ebitda, fifty_two_week_change, sandp_52_week_change, total_cash, total_cash_per_share, ebitda, total_debt, quick_ratio, current_ratio, total_revenue, debt_to_equity, revenue_per_share, return_on_assets, return_on_equity, free_cashflow, operating_cashflow, revenue_growth, gross_margins, ebitda_margins, operating_margins)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
""", financial_info_data)


