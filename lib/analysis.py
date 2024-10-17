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
    # ノーマライズ
    v10 = normalize(df[0:10])
    v20 = normalize(df[0:20])
    v30 = normalize(df[0:30])
    
    # 内積計算で近似べクトルデータを取得
    r10 = Vector10(DB).get_dot_by_vec(v10, 10)
    r20 = Vector20(DB).get_dot_by_vec(v20, 10)
    r30 = Vector30(DB).get_dot_by_vec(v30, 10)

    resultsv10 = []
    resultsv20 = []
    resultsv30 = []

    for idx, _r in enumerate([r10, r20, r30]):

        for v in _r:

            # 近似ベクトルデータトップ１０から、５日後までの株価情報を取得
            sdate = v[0].strftime('%Y-%m-%d')
            edate = (v[0] + datetime.timedelta(days=15)).strftime('%Y-%m-%d')
            h = HistoryDate(DB).get_data_by_date_range(v[1], sdate, edate)
            r = {
                'VecVolume': [item[7] for item in h],
                'VecPrice': normalize(h),
                'Date': date,
                'companyCode': company_code,
            }
            if idx == 0:
                resultsv10.append(r)
            elif idx == 1:
                resultsv20.append(r)
            else:
                resultsv30.append(r)

    return resultsv10, resultsv20, resultsv30

"""
指定された日付に基づいて、上昇幅および下降幅の高い順にデータを取得し、ランキングを生成します。
Args:
    date (datetime.date): 解析対象の日付。
    DB: データベース接続オブジェクト（省略可能）。
Returns:
    list: 上昇幅の高い順のデータと下降幅の高い順のデータを含むリスト。
"""
def ranking(
    date: datetime.date,
    DB = None
) -> list:
    targets = ['Day', 'DayOne', 'DayTwo', 'DayThree', 'WeekOne', 'WeekTwo']
    resultsUpper = {}
    resultsLower = {}
    # 上昇幅の高い順にデータを取得
    for target in targets:
        # 与えられた日付の解析データを取得
        df = AnalysisDate(DB).get_by_day_and_target(
            date, target, 'DESC'
        )

        historys = []
        moves = []

        for record in df:
            h = HistoryDate(DB).get_latest_by_company_code(record[1], 30)
            historys.append([float(item[3]) for item in h])
            moves.append(normalize(h, 4))

        resultsUpper[target] = json.dumps({
            'Rank': [item[1] for item in df],
            'History': historys,
            'Move': moves
        }, ensure_ascii=False)

    # 下降幅の高い順にデータを取得
    for target in targets:
        # 与えられた日付のデータを取得
        df = AnalysisDate(DB).get_by_day_and_target(
            date, target, 'ASC'
        )

        historys = []
        moves = []

        for record in df:
            h = HistoryDate(DB).get_latest_by_company_code(record[1], 30)
            historys.append([float(item[3]) for item in h])
            moves.append(normalize(h, 4))

        resultsLower[target] = json.dumps({
            'Rank': [item[1] for item in df],
            'History': historys,
            'Move': moves
        }, ensure_ascii=False)

    return resultsUpper, resultsLower


