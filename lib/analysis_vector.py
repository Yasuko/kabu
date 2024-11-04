import pandas as pd
import datetime
import math
import json

from model.db.HistoryDate import HistoryDate
from model.db.AnalysisVector import AnalysisVector
from model.db.Vector50 import Vector50
from model.db.Vector100 import Vector100

from lib.utils import normalize


def vector(
    company_code: str,
    date: datetime.date,
    DB = None
) -> list:
    sdate = date - datetime.timedelta(days=50)
    df = HistoryDate(DB).get_data_by_date_range(
        company_code,
        sdate.strftime('%Y-%m-%d'),
        date.strftime('%Y-%m-%d')
    )
    
    # データが存在しない場合, Noneを返す
    if len(df) <= 19:
        return None
    # ノーマライズ
    v50 = normalize(df[0:10], 18, 10)
    v100 = normalize(df[0:20], 18, 20)
    
    # 内積計算で近似べクトルデータを取得
    r50 = Vector50(DB).get_dot_by_vec(v50, 10)
    r100 = Vector100(DB).get_dot_by_vec(v100, 10)

    resultsv50 = []
    resultsv100 = []

    for idx, _r in enumerate([r50, r100]):

        for v in _r:

            # 近似ベクトルデータトップ１０から、５日後までの株価情報を取得
            sdate = v[0].strftime('%Y-%m-%d')
            edate = (v[0] + datetime.timedelta(days=15)).strftime('%Y-%m-%d')
            
            h = HistoryDate(DB).get_data_by_date_range(v[1], sdate, edate)
            r = {
                'VecPrice': normalize(rate(h)),
                'Date': date,
                'companyCode': company_code,
            }
            if idx == 0:
                resultsv50.append(r)
            else:
                resultsv100.append(r)

    print('resultsv50 :', resultsv50)
    print('resultsv100 :', resultsv100)

    hoge50 = rate_average(resultsv50)
    hoge100 = rate_average(resultsv100)

    print('hoge50 :', hoge50)
    print('hoge100 :', hoge100)

    
    return resultsv50, resultsv100

'''
配列の1番目のOpen価格と、1日後、2日後、3日後、5日後の
Open価格を比較し、比率を計算し返す
'''
def rate(
    df: datetime.date,
) -> list:
    print(df)
    # 1日後、2日後、3日後、5日後のOpen価格を取得
    rate = []
    for i in range(1, 6):
        rate.append({
            'rate': [
                (df[i]['open'] - df[0]['open']) / df[0]['open']
            ],
            'volume': df[i]['volume']
        })

    return rate

'''
6日間の価格の変動率が入った10個の配列から
平均を求めた配列を作成し返す
'''
def rate_average(
    df: list,
) -> list:
    _a1 = sum([item['VecPrice'][0] for item in df]) / len(df)
    _a2 = sum([item['VecPrice'][1] for item in df]) / len(df)
    _a3 = sum([item['VecPrice'][2] for item in df]) / len(df)
    _a4 = sum([item['VecPrice'][3] for item in df]) / len(df)
    _a5 = sum([item['VecPrice'][4] for item in df]) / len(df)
    _a6 = sum([item['VecPrice'][5] for item in df]) / len(df)
    
    return [_a1, _a2, _a3, _a4, _a5, _a6]

