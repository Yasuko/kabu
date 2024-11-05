import datetime
import calendar
import math
import math
from typing import Tuple

'''
タイプヒントの型情報と、引数のデータが一致しているかを検証し
一致している場合はデータを返し
一致していない場合は型に合わせた最小のデータを返す

Args:
    data (int | float | str | list | dict | set | bool | None): 検証するデータ
    data_type (int | float | str | list | dict | set | bool | None): 検証するデータの型

Returns:
    int | float | str | list | dict | set | bool | None: 検証したデータ

'''
def validate(
    data: int | float | str | list | dict | set | bool | None,
    data_type: int | float | str | list | dict | set | bool | None
) -> int | float | str | list | dict | set | bool | None:
    # データがNoneでないかつ型が一致する場合
    if data is not None and isinstance(data, data_type):
        return data
    # 型に合わせた最小のデータを返す
    if data_type == int:
        return 0
    elif data_type == float:
        return 0.0
    elif data_type == str:
        return ""
    elif data_type == list:
        return []
    elif data_type == dict:
        return {}
    elif data_type == set:
        return set()
    elif data_type == bool:
        return False
    else:
        return None

'''
データと型情報から
クエリのカラム名、値、値のリストを返す
'''
def query_convert(
    data: dict,
    types: dict,
) -> Tuple[str, str, list]:
    query = ''
    values = ''
    insert = []
    for key in types.__annotations__.keys():
        query += f"{key}, "
        values += f"%s, "
        insert.append(data[key])
    return query[:-2], values[:-2], insert

'''
欠損データをチェックし、float型であるかを返す
'''
def chek_float(data: any) -> bool:
    if math.isnan(data):
        return False
    if data is None:
        return False
    if isinstance(data, float):
        return True
    if data.__class__.__name__ == 'Decimal':
        return True
    return False


'''
指定された年月から
1月単位の日付リストを作成し、返す
'''
def build_date_map(
    start: int = 2010,
    end: int = 2024,
) -> list:
    date_ranges = []

    for year in range(start, end + 1):
        for month in range(1, 13):
            start_date = datetime.date(year, month, 1)
            end_date = datetime.date(year, month, calendar.monthrange(year, month)[1])

            # 日付が現在の日付よりも未来の場合は処理を終了
            if end_date > datetime.date.today():
                break
            date_ranges.append({
                "start": start_date.strftime("%Y-%m-%d"),
                "end": end_date.strftime("%Y-%m-%d")
            })
    
    return date_ranges

'''
指定された年から
1年単位の日付リストを作成し、返す
'''
def build_month_map(
    start: int = 2010,
    end: int = 2024,
):
    date_ranges = []

    for year in range(start, end + 1):
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 12, 31)

        # 日付が現在の日付よりも未来の場合は処理を終了
        if start_date > datetime.date.today():
            break
        date_ranges.append({
            "start": start_date.strftime("%Y-%m-%d"),
            "end": end_date.strftime("%Y-%m-%d")
        })
    
    return date_ranges

'''
指定された日付と、指定された日数分前の日付から
その間の日付のリストを作成し、返す
'''
def date_map_before_date(
    date: datetime.date,
    days: int,
):
    date_list = []

    for i in range(days):
        date_list.append(date - datetime.timedelta(days=i))

    return date_list

'''
値動きから角度を計算し、返す
'''
def angle(data: list) -> list:
    angles = []
    for i in range(1, len(data)):
        x_diff = 1
        y_diff = data[i] - data[i-1]
        angle = math.atan2(y_diff, x_diff)
        angles.append(angle)

    return angles


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
    decimal: int = 18,
    vec: int = 10
) -> list:
    # recordsに数値以外の値が含まれている場合は空のリストを返す

    # Open値の最大値と最小値を取得
    open_values = [float(record[3]) for record in records]
    # High値の最大値と最小値を取得
    high_values = [float(record[4]) for record in records]
    # Low値の最大値と最小値を取得
    low_values = [float(record[5]) for record in records]
    # Close値の最大値と最小値を取得
    close_values = [float(record[6]) for record in records]
    # Volume値の最大値と最小値を取得
    volume_values = [float(record[7]) for record in records]

    # 配列が空の場合は0を返す
    if len(open_values) == 0:
        return [0]

    # 正規化
    normalized_open_values = build_normalize_list(open_values, decimal, vec)
    normalized_high_values = build_normalize_list(high_values, decimal, vec)
    normalized_low_values = build_normalize_list(low_values, decimal, vec)
    normalized_close_values = build_normalize_list(close_values, decimal, vec)
    normalized_volume_values = build_normalize_list(volume_values, decimal, vec)

    # 全ての配列を結合して返す
    return normalized_open_values + normalized_high_values + normalized_low_values + normalized_close_values + normalized_volume_values

def build_normalize_list(
    records: list[list],
    decimal: int = 18,
    vec: int = 10
) -> list:
    max_record = max(records)
    min_record = min(records)

    # 正規化

    normalized_values = []
    
    for i in range(vec):
        # 分母が0の場合は0を返す
        if max_record - min_record == 0:
            normalized_values.append(0)
        else:
            r = (records[i] - min_record) / (max_record - min_record)
            # 数値以外の場合は0を返す
            if math.isnan(r):
                normalized_values.append(0)
            else:
                # 小数点以下をdecimalで指定された桁数に丸める
                normalized_values.append(round(r, decimal))
    
    return normalized_values

'''
ローソク足から、上げ下げの圧力を計算する
'''
def convert_pressure(
    record: list
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


'''
日毎のローソク足データを指定された期間で集約し、返す
'''
def aggregate_stock_data(
    data: list,
    interval: int
) -> list:
    aggregated_data = []
    
    for i in range(0, len(data), interval):
        chunk = data[i:i+interval]
        if not chunk:
            continue
        open_price = chunk[0][3]
        high_price = max(day[4] for day in chunk)
        low_price = min(day[5] for day in chunk)
        close_price = chunk[-1][6]
        aggregated_data.append({
            "open": open_price,
            "high": high_price,
            "low": low_price,
            "close": close_price
        })
    
    # 配列の後ろから20件までを返す
    return aggregated_data[-20:]
