import pandas as pd
import datetime

from model.db.HistoryDate import HistoryDate

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
    

def rate(
    company_code: str,
    start_date: pd.Timestamp,
):
    
    df = HistoryDate().get_data_by_date_range(
        company_code,
        datetime.timedelta(days=15),
        start_date
    )

    # データが存在しない場合
    if len(df) == 0:
        return None

    results = []
    i = len(df) - 1

    # 1日前のOpen値と当日のOpen値の差を計算
    results.append({
        'rarte': diff_rate(df[i][3], df[i-1][3]),
        'pressure': convert_pressure(df[i])
    })
    # 2日前のOpen値と当日のOpen値の差を計算
    results.append({
        'rarte': diff_rate(df[i][3], df[i-2][3]),
        'pressure': convert_pressure(df[i-2])
    })
    # 3日前のOpen値と当日のOpen値の差を計算
    results.append({
        'rarte': diff_rate(df[i][3], df[i-3][3]),
        'pressure': convert_pressure(df[i-3])
    })
    # 1週間前のOpen値と当日のOpen値の差を計算
    results.append({
        'rarte': diff_rate(df[i][3], df[i-5][3]),
        'pressure': convert_pressure(df[i-5])
    })
    # 2週間前のOpen値と当日のOpen値の差を計算
    results.append({
        'rarte': diff_rate(df[i][3], df[i-10][3]),
        'pressure': convert_pressure(df[i-10])
    })

    return results

def diff_rate(
    data1: float,
    data2: float
) -> float:
    return ((data1 - data2) / data2) * 100

def convert_vector(
    records: list[list],
) -> float:

    # Open値の最大値と最小値を取得
    open_values = [record[3] for record in records]
    max_open = max(open_values)
    min_open = min(open_values)

    # 正規化
    normalized_open_values = [(open - min_open) / (max_open - min_open) for open in open_values]

    # 結果を辞書形式で返す
    return normalized_open_values

