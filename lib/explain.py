import pandas as pd
import datetime
import math
import json

from model.db.HistoryDate import HistoryDate
from model.db.AnalysisDate import AnalysisDate
from model.db.Vector10 import Vector10
from model.db.Vector20 import Vector20
from model.db.Vector30 import Vector30

from lib.utils import angle, normalize


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

    # 今日のOpenとCloseの差、Volumeの差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i][6]),
        'volume': df[i][7] - df[i-1][7] 
    })

    # 1日前のOpen値と当日のOpen値の差、Volumeの差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-1][3]),
        'volume': df[i][7] - df[i-1][7]
    })
    # 2日前のOpen値と当日のOpen値の差、Volumeの差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-2][3]),
        'volume': df[i][7] - df[i-2][7]
    })
    # 3日前のOpen値と当日のOpen値の差、Volumeの差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-3][3]),
        'volume': df[i][7] - df[i-3][7]
    })
    # 1週間前のOpen値と当日のOpen値の差、Volumeの差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-5][3]),
        'volume': df[i][7] - df[i-5][7]
    })
    # 2週間前のOpen値と当日のOpen値の差、Volumeの差を計算
    results.append({
        'rate': diff_rate(df[i][3], df[i-10][3]),
        'volume': df[i][7] - df[i-10][7]
    })

    return results

def diff_rate(
    data1: float,
    data2: float
) -> float:
    return ((data1 - data2) / data2) * 100



def vector(
    company_code: str,
    date: datetime.date,
    DB = None
) -> list:
    sdate = date - datetime.timedelta(days=60)
    df = HistoryDate(DB).get_data_by_date_range(
        company_code,
        sdate.strftime('%Y-%m-%d'),
        date.strftime('%Y-%m-%d')
    )
    
    # データが存在しない場合, Noneを返す
    if len(df) <= 29:
        return None

    for idx, _r in df:
        open = _r[3]
        high = _r[4]
        low = _r[5]
        close = _r[6]

        diff_open = close - open
        diff_high = close - high
        diff_low = close - low
        diff_width = high - low

    return []
