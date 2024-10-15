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


def query_convert(
    data: dict,
    types: dict,
) -> Tuple[str, str, list]:
    query = ''
    values = ''
    insert = []
    print(data)
    for key in types.__annotations__.keys():
        query += f"{key}, "
        values += f"%s, "
        insert.append(data[key])
    return query[:-2], values[:-2], insert


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
指定された年月の日付範囲を作成し、返す
'''
def build_date_map(
    start: int = 2010,
    end: int = 2024,
):
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