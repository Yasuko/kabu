import pandas as pd

from model.db.HistoryDate import HistoryDate
from model.db.HistoryWeek import HistoryWeek
from model.db.HistoryMonth import HistoryMonth
from model.db.History3Month import History3Month

def convert_date_to_week(
    company_code: str,
):
    df = pd.read_sql_query(
        HistoryDate().get_all_data_by_company_code(company_code),
        HistoryDate().DB
    )

    # 日付をdatetime型に変換
    df['Date'] = pd.to_datetime(df['Date'])

    # 週ごとにデータをグループ化し、必要な集計を行う
    weekly_df = df.resample('W-MON', on='Date').agg({
        'companyCode': 'first',
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum',
        'Dividends': 'sum',
        'StockSplits': 'sum'
    }).reset_index()

    print(weekly_df)


def convert_date_to_month(
    company_code: str,
):
    df = pd.read_sql_query(
        HistoryDate().get_all_data_by_company_code(company_code),
        HistoryDate().DB
    )

    # 日付をdatetime型に変換
    df['Date'] = pd.to_datetime(df['Date'])

    # 月ごとにデータをグループ化し、必要な集計を行う
    monthly_df = df.resample('M', on='Date').agg({
        'companyCode': 'first',
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum',
        'Dividends': 'sum',
        'StockSplits': 'sum'
    }).reset_index()

    print(monthly_df)

def convert_date_to_3month(
    company_code: str,
):
    df = pd.read_sql_query(
        HistoryDate().get_all_data_by_company_code(company_code),
        HistoryDate().DB
    )

    # 日付をdatetime型に変換
    df['Date'] = pd.to_datetime(df['Date'])

    # 3ヶ月ごとにデータをグループ化し、必要な集計を行う
    monthly_df = df.resample('3M', on='Date').agg({
        'companyCode': 'first',
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum',
        'Dividends': 'sum',
        'StockSplits': 'sum'
    }).reset_index()

    print(monthly_df)

