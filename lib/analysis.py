import pandas as pd
import datetime
import math

from model.db.HistoryDate import HistoryDate
from model.db.VectorDate import VectorDate

from lib.utils import angle

'''
ローソク足から、上げ下げの圧力を計算する
'''
def convert_pressure(
    record: list,
) -> float:

    open_price = record[3]
    close_price = record[6]
    high_price = record[4]
    low_price = record[5]

    # nanがいずれかに含まれている場合は0を返す
    if math.isnan(open_price) or math.isnan(close_price) or math.isnan(high_price) or math.isnan(low_price):
        return 0

    # ローソクの足の上下の長さが、どちら方向に大きいかを計算
    if close_price > open_price:  # 陽線の場合
        upper_wick = high_price - close_price
        lower_wick = open_price - low_price
    else:  # 陰線の場合
        upper_wick = high_price - open_price
        lower_wick = close_price - low_price
    
    wick_difference = upper_wick - lower_wick

    # ローソク足の伸び率を計算
    if wick_difference < 0: # ローソク足が負の場合
        percentage = ((low_price / close_price) * 100) - 100
    else: # ローソク足が正の場合
        percentage = ((high_price / close_price) * 100) - 100

    return percentage
    

def rate(
    company_code: str,
    date: pd.Timestamp,
    DB = None
):
    
    df = HistoryDate(DB).get_data_by_date_range(
        company_code,
        date - datetime.timedelta(days=30),
        date
    )

    # データが存在しない場合
    if len(df) == 0 or len(df) <= 9:
        return None
    # math.isnoneが含まれている場合はNoneを返す
    for record in df:
        if math.isnan(record[3]) or math.isnan(record[6]) or math.isnan(record[4]) or math.isnan(record[5]):
            return None

    results = []
    i = len(df) - 1

    # 今日のOpenとCloseの差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i][6]),
        'pressure': convert_pressure(df[i])
    })

    # 1日前のOpen値と当日のOpen値の差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-1][3]),
        'pressure': (convert_pressure(df[i]) + convert_pressure(df[i-1])) / 2
    })
    # 2日前のOpen値と当日のOpen値の差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-2][3]),
        'pressure': (convert_pressure(df[i]) + convert_pressure(df[i-2])) / 2
    })
    # 3日前のOpen値と当日のOpen値の差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-3][3]),
        'pressure': (convert_pressure(df[i]) + convert_pressure(df[i-3])) / 2
    })
    # 1週間前のOpen値と当日のOpen値の差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-5][3]),
        'pressure': (convert_pressure(df[i]) + convert_pressure(df[i-5])) / 2
    })
    # 2週間前のOpen値と当日のOpen値の差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-10][3]),
        'pressure': (convert_pressure(df[i]) + convert_pressure(df[i-10])) / 2
    })

    return results

def diff_rate(
    data1: float,
    data2: float
) -> float:
    return ((data1 - data2) / data2) * 100

"""
与えられたレコードの「Open」値を正規化します。
この関数は、各レコードがさまざまな財務データを含むリストであるレコードのリストを受け取ります。
各レコードのインデックス3にあると仮定される「Open」値を抽出し、
データセット内の最小および最大の「Open」値に基づいてこれらの値を0から1の範囲に正規化します。
最大および最小の「Open」値が同じ場合、ゼロ除算を避けるためにすべての正規化された値に0を返します。
引数:
    records (list[list]): 各レコードが財務データを含むリストであるレコードのリスト。
                        「Open」値はインデックス3にある必要があります。
戻り値:
    dict: 正規化された「Open」値を含む辞書。
"""
def normalize(
    records: list[list],
) -> list:
    # recordsに数値以外の値が含まれている場合は空のリストを返す

    # Open値の最大値と最小値を取得
    open_values = [float(record[3]) for record in records]
    # 配列が空の場合は0を返す
    if len(open_values) == 0:
        return [0]
    max_open = max(open_values)
    min_open = min(open_values)

    # 正規化
    #normalized_open_values = [(open - min_open) / (max_open - min_open) for open in open_values]
    normalized_open_values = []
    for open in open_values:
        # 分母が0の場合は0を返す
        if max_open - min_open == 0:
            normalized_open_values.append(0)
        else:
            r = (open - min_open) / (max_open - min_open)
            # 数値以外の場合は0を返す
            if math.isnan(r):
                normalized_open_values.append(0)
            else:
                normalized_open_values.append(r)


    # 結果を辞書形式で返す
    return normalized_open_values


def vector_angle(
    company_code: str,
    date: datetime.date,
    DB = None
) -> list:
    df = HistoryDate(DB).get_data_by_date_range(
        company_code,
        date - datetime.timedelta(days=30),
        date
    )
    # データが存在しない場合, Noneを返す
    if len(df) <= 9:
        return None
    # ノーマライズ
    v = normalize(df[0:10])
    # 内積計算で近似べクトルデータを取得
    r = VectorDate(DB).get_dot_by_vec(v, 10)

    results = []
    for _r in r:
        # 近似ベクトルデータトップ１０から、５日後までの株価情報を取得
        h = HistoryDate(DB).get_data_by_date_range(_r[1], _r[0], _r[0] + datetime.timedelta(days=15))
        # 価格の変動を角度に変換
        # results.append(angle([item[3] for item in h]))

        # Open価格の動きと、圧力を計算
        results.append({
            'pressure': ([convert_pressure(item) for item in h]),
            'price': normalize(h)
        })

    return results

