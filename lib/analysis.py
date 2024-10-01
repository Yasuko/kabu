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
    record: list,
):
    print(record)
    open_price = record[3]
    close_price = record[6]
    high_price = record[4]
    low_price = record[5]

    if close_price > open_price:  # 陽線の場合
        upper_wick = high_price - close_price
        lower_wick = open_price - low_price
    else:  # 陰線の場合
        upper_wick = high_price - open_price
        lower_wick = close_price - low_price
    
    wick_difference = upper_wick - lower_wick

    if wick_difference < 0: # ローソク足が負の場合
        percentage = (wick_difference / (10 * low_price)) * 100
    else: # ローソク足が正の場合
        percentage = (wick_difference / (10 * high_price)) * 100

    return {
        'Date': record[1],
        'Percentage': percentage
    }
    

def rate_by_one_day(
    company_code: str,
):
    # 今日の日付を取得
    today = pd.Timestamp.today().normalize()
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        today - pd.DateOffset(days=1),
        today
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    rate = ((df[1][6] - df[0][3]) / df[0][3]) * 100
    pressure1 = convert_pressure(df[0])
    pressure2 = convert_pressure(df[1])

    return {
        'Rate': rate,
        #pressureの平均値を返す
        'Pressure': (pressure1['Percentage'] + pressure2['Percentage']) / 2
    }

def rate_by_two_day(
    company_code: str,
):
    # 今日の日付を取得
    today = pd.Timestamp.today().normalize()
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        today - pd.DateOffset(days=2),
        today
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    rate = ((df[2][6] - df[0][3]) / df[0][3]) * 100

    return rate

def rate_by_three_day(
    company_code: str,
):
    # 今日の日付を取得
    today = pd.Timestamp.today().normalize()
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        today - pd.DateOffset(days=3),
        today
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    rate = ((df[3][6] - df[0][3]) / df[0][3]) * 100

    return rate

def rate_by_one_week(
    company_code: str,
):
    # 今日の日付を取得
    today = pd.Timestamp.today().normalize()
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        today - pd.DateOffset(weeks=1),
        today
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    rate = ((df[1][6] - df[0][3]) / df[0][3]) * 100

    return rate

def rate_by_two_week(
    company_code: str,
):
    # 今日の日付を取得
    today = pd.Timestamp.today().normalize()
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        today - pd.DateOffset(weeks=2),
        today
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    rate = ((df[2][6] - df[0][3]) / df[0][3]) * 100

    return rate

def rate_by_one_month(
    company_code: str,
):
    # 今日の日付を取得
    today = pd.Timestamp.today().normalize()
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        today - pd.DateOffset(months=1),
        today
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    rate = ((df[1][6] - df[0][3]) / df[0][3]) * 100

    return rate

def rate_by_three_month(
    company_code: str,
):
    # 今日の日付を取得
    today = pd.Timestamp.today().normalize()
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        today - pd.DateOffset(months=3),
        today
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    rate = ((df[1][6] - df[0][3]) / df[0][3]) * 100

    return rate

def rate_by_six_month(
    company_code: str,
):
    # 今日の日付を取得
    today = pd.Timestamp.today().normalize()
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        today - pd.DateOffset(months=6),
        today
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    rate = ((df[1][6] - df[0][3]) / df[0][3]) * 100

    return rate