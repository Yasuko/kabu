import pandas as pd

from model.db.HistoryDate import HistoryDate
from model.db.HistoryWeek import HistoryWeek
from model.db.HistoryMonth import HistoryMonth
from model.db.History3Month import History3Month
from model.db.History6Month import History6Month
from model.db.HistoryYear import HistoryYear


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

def convert_date_to_6month(
    company_code: str,
):
    df = pd.read_sql_query(
        HistoryDate().get_all_data_by_company_code(company_code),
        HistoryDate().DB
    )

    # 日付をdatetime型に変換
    df['Date'] = pd.to_datetime(df['Date'])

    # 6ヶ月ごとにデータをグループ化し、必要な集計を行う
    monthly_df = df.resample('6M', on='Date').agg({
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


def convert_date_to_year(
    company_code: str,
):
    df = pd.read_sql_query(
        HistoryDate().get_all_data_by_company_code(company_code),
        HistoryDate().DB
    )

    # 日付をdatetime型に変換
    df['Date'] = pd.to_datetime(df['Date'])

    # 年ごとにデータをグループ化し、必要な集計を行う
    monthly_df = df.resample('Y', on='Date').agg({
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


def convert_pressure(
    record: dict,
):

    open_price = record['Open']
    close_price = record['Close']
    high_price = record['High']
    low_price = record['Low']

    if close_price > open_price:  # 陽線の場合
        upper_wick = high_price - close_price
        lower_wick = open_price - low_price
    else:  # 陰線の場合
        upper_wick = high_price - open_price
        lower_wick = close_price - low_price
    
    wick_difference = upper_wick - lower_wick

    if wick_difference < 0: # ローソク足が逆転している場合
        percentage = (wick_difference / (10 * low_price)) * 100
    else: # ローソク足が正しい場合
        percentage = (wick_difference / (10 * high_price)) * 100

    return {
        'Date': record['Date'],
        'Percentage': percentage
    }
    

