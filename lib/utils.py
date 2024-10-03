import datetime
import calendar
import math
from typing import Tuple

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