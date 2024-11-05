import pandas as pd
import datetime
import math
import json

from model.db.HistoryDate import HistoryDate
from model.db.AnalysisVector50 import AnalysisVector50
from model.db.AnalysisVector100 import AnalysisVector100
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
    #v100 = normalize(df[0:20], 18, 20)
    
    # 内積計算で近似べクトルデータを取得
    r50 = Vector50(DB).get_dot_by_vec(v50, 50)
    #r100 = Vector100(DB).get_dot_by_vec(v100, 100)
    
    resultsv50 = []
    #resultsv100 = []

    #for idx, _r in enumerate([r50, r100]):
    for idx, _r in enumerate([r50]):
        
        for i in range(len(_r)):

            print(_r[i])
            try:

                # 近似ベクトルデータトップ１０から、５日後までの株価情報を取得
                sdate = _r[i][0].strftime('%Y-%m-%d')
                edate = (_r[i][0] + datetime.timedelta(days=15)).strftime('%Y-%m-%d')
                
                h = HistoryDate(DB).get_data_by_date_range(_r[i][1], sdate, edate)

                r = {
                    'Rate': rate(h),
                    #'VecPrice': normalize(h),
                    'Vec': _r[i][2],
                    'Date': _r[i][0],
                    'companyCode': _r[i][1],
                }
                if idx == 0:
                    resultsv50.append(r)
                #else:
                    #resultsv100.append(r)
                # print(resultsv50)

            except Exception as e:
                print('ERROR!!  ', e)

    #print('resultsv50 :', resultsv50)
    #print('resultsv100 :', resultsv100)

    hoge50 = rate_average(resultsv50)
    #hoge100 = rate_average(resultsv100)
    
    return resultsv50, hoge50

'''
配列の1番目のOpen価格と、1日後、2日後、3日後、5日後の
Open価格を比較し、比率を計算し返す
'''
def rate(
    df: list,
) -> list:
    # 1日後、2日後、3日後、5日後のOpen価格を取得
    rate = []
    for i in range(1, 6):
        rate.append({
            'rate': (df[i][3] - df[0][3]) / df[0][3],
            'volume': df[i][7]
        })

    return rate

'''
6日間の価格の変動率が入った10個の配列から
平均を求めた配列を作成し返す
'''
def rate_average(
    df: list,
) -> list:
    _a1 = sum([item['Rate'][0]['rate'] for item in df]) / len(df)
    _a2 = sum([item['Rate'][1]['rate'] for item in df]) / len(df)
    _a3 = sum([item['Rate'][2]['rate'] for item in df]) / len(df)
    _a4 = sum([item['Rate'][3]['rate'] for item in df]) / len(df)
    _a5 = sum([item['Rate'][4]['rate'] for item in df]) / len(df)
    
    return [_a1, _a2, _a3, _a4, _a5]

