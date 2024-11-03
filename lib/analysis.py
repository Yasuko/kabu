import pandas as pd
import datetime
import math
import json

from model.db.HistoryDate import HistoryDate
from model.db.AnalysisDate import AnalysisDate
from model.db.AnalysisCandle import AnalysisCandle
from model.db.AnalysisVector import AnalysisVector
from model.db.Vector50 import Vector50
from model.db.Vector100 import Vector100

from lib.utils import angle, normalize

'''
指定期間の株価情報を取得し
株価の変動率と出来高の変動を計算する
'''
def rate(
    company_code: str,
    date: pd.Timestamp,
    DB = None
):
    
    df = HistoryDate(DB).get_data_by_date_range(
        company_code,
        date - datetime.timedelta(days=30),
        date,
        'DESC'
    )

    # データが存在しない場合
    if len(df) == 0 or len(df) <= 9:
        return None
    # math.isnoneが含まれている場合はNoneを返す
    for record in df:
        if math.isnan(record[3]) or math.isnan(record[6]) or math.isnan(record[4]) or math.isnan(record[5]):
            return None
    results = []

    # 今日のOpenとCloseの差、Volumeの差を計算
    r = diff_rate1(df[0])
    results.append({
        'rate': r,
        'volume': r[4]
    })

    # 1日前のOpen値と当日のOpen値の差、Volumeの差を計算
    r = diff_rate2(df, 1)
    results.append({
        'rate': r,
        'volume': r[4]
    })
    # 2日間の平均と当日の差、Volumeの差を計算
    r = diff_rate2(df, 2)
    results.append({
        'rate': r,
        'volume': r[4]
    })
    # 3日前のOpen値と当日のOpen値の差、Volumeの差を計算
    r = diff_rate2(df, 3)
    results.append({
        'rate': r,
        'volume': r[4]
    })
    # 1週間前のOpen値と当日のOpen値の差、Volumeの差を計算
    r = diff_rate2(df, 5)
    results.append({
        'rate': r,
        'volume': r[4]
    })
    # 2週間前のOpen値と当日のOpen値の差、Volumeの差を計算
    r = diff_rate2(df, 10)
    results.append({
        'rate': r,
        'volume': r[4]
    })

    return results

# OpenとCloseの差の変動率を計算
def diff_rate1(
    df: list
) -> tuple:
    _o = round(((df[3] - df[6]) / df[6]) * 100, 4)
    _h = round(((df[4] - df[6]) / df[6]) * 100, 4)
    _l = round(((df[5] - df[6]) / df[6]) * 100, 4)
    _c = round(((df[6] - df[6]) / df[6]) * 100, 4)

    return float(_o), float(_h), float(_l), float(_c), df[7]
    

# 指定期間内のOpenの平均とHighの平均の差と当日のOpenの差の変動率を計算
def diff_rate2(
    df: list,
    num: int
) -> tuple:
    _num = 1 + num
    open = sum([item[3] for item in df[1:_num]]) / len(df[1:_num])
    high = sum([item[4] for item in df[1:_num]]) / len(df[1:_num])
    low = sum([item[5] for item in df[1:_num]]) / len(df[1:_num])
    close = sum([item[6] for item in df[1:_num]]) / len(df[1:_num])

    _o = round(((df[0][3] - open) / open) * 100, 4)
    _h = round(((df[0][4] - high) / high) * 100, 4)
    _l = round(((df[0][5] - low) / low) * 100, 4)
    _c = round(((df[0][6] - close) / close) * 100, 4)

    #num で指定された日数分のvolumeの平均を計算
    _v = sum([item[7] for item in df[1:_num]]) / len(df[1:_num])
    return float(_o), float(_h), float(_l), float(_c), _v


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
    if len(df) <= 49:
        return None
    # ノーマライズ
    v30 = normalize(df[0:30])
    v40 = normalize(df[0:40])
    v50 = normalize(df[0:50])
    
    # 内積計算で近似べクトルデータを取得
    r30 = Vector30(DB).get_dot_by_vec(v30, 10)
    r40 = Vector40(DB).get_dot_by_vec(v40, 10)
    r50 = Vector50(DB).get_dot_by_vec(v50, 10)

    resultsv30 = []
    resultsv40 = []
    resultsv50 = []

    for idx, _r in enumerate([r30, r40, r50]):

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
                resultsv30.append(r)
            elif idx == 1:
                resultsv40.append(r)
            else:
                resultsv50.append(r)

    return resultsv30, resultsv40, resultsv50

"""
指定された日付に基づいて、上昇幅および下降幅の高い順にデータを取得し、ランキングを生成します。
Args:
    date (datetime.date): 解析対象の日付。
    DB: データベース接続オブジェクト（省略可能）。
Returns:
    list: 上昇幅の高い順のデータと下降幅の高い順のデータを含むリスト。
"""
def ranking(
    day: str,
    DB = None
) -> list:
    targets = ['Day', 'DayOne', 'DayTwo', 'DayThree', 'WeekOne', 'WeekTwo']
    resultsUpper = {}
    resultsLower = {}
    # 上昇幅の高い順にデータを取得
    for target in targets:
        # 与えられた日付の解析データを取得
        df = AnalysisDate(DB).get_by_day_and_target(day, target, 'DESC')

        resultsUpper[target] = buildHistoryList(df, day, DB)

    # 下降幅の高い順にデータを取得
    for target in targets:
        # 与えられた日付のデータを取得
        df = AnalysisDate(DB).get_by_day_and_target(day, target, 'ASC')

        resultsLower[target] = buildHistoryList(df, day, DB)

    return resultsUpper, resultsLower


"""
指定された日付に基づいて、ローソク図の解析結果を取得し、ランキングを生成します。
Args:
    date (datetime.date): 解析対象の日付。
    DB: データベース接続オブジェクト（省略可能）。
Returns:
    list: 上昇幅の高い順のデータと下降幅の高い順のデータを含むリスト。
"""
def rankingAnalysisType1(
    day: str,
    DB = None
) -> list:
    targets = ['Day', 'DayOne', 'DayTwo', 'DayThree', 'WeekOne']
    resultsUpper = {}
    resultsLower = {}

    # 上昇幅の高い順にデータを取得
    for target in targets:
        # 与えられた日付の解析データを取得
        df = AnalysisCandle(DB).get_rank(day, target, 'DESC')
        # ランク表示用のリスト作成
        resultsUpper[target] = buildHistoryList(df, day, DB)

    # 下降幅の高い順にデータを取得
    for target in targets:
        # 与えられた日付のデータを取得
        df = AnalysisCandle(DB).get_rank(day, target, 'ASC')
        # ランク表示用のリスト作成
        resultsLower[target] = buildHistoryList(df, day, DB)

    return resultsUpper, resultsLower

def rankingAnalysisVector(
    day: str,
    DB = None
) -> list:
    targets = ['DayOne', 'DayTwo', 'DayThree', 'WeekOne']
    results = {}

    # 上昇幅の高い順にデータを取得
    for target in targets:
        # 与えられた日付の解析データを取得
        df = AnalysisVector(DB).get_rank(day, target)
        # ランク表示用のリスト作成
        resultsUpper[target] = buildHistoryList(df, day, DB)

    return results

def buildHistoryList(
    df: list,
    day: str,
    DB = None
) -> list:
    historys = []
    volumes = []
    moves = []

    for record in df:
        h = HistoryDate(DB).get_latest_by_company_code(record[1], day, 30)
        historys.append([float(item[3]) for item in h])
        volumes.append([float(item[7]) for item in h])
        moves.append(normalize(h, 4))

    return json.dumps({
        'Rank': [item[1] for item in df],
        'History': historys,
        'Volume': volumes,
        'Move': moves
    }, ensure_ascii=False)
