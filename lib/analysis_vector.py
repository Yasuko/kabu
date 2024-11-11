import datetime
import json

from model.db.HistoryDate import HistoryDate
from model.db.AnalysisVector50 import AnalysisVector50
from model.db.Vector50 import Vector50

from lib.utils import normalize


def vector_analysis(
    company_code: str,
    date: datetime.date,
    DB = None
) -> tuple:
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
    r50 = Vector50(DB).get_dot_by_vec(v50, 10)
    #r100 = Vector100(DB).get_dot_by_vec(v100, 100)

    # Cosine類似度計算で近似べクトルデータを取得
    #r50 = Vector50(DB).get_similarity_by_vec(v50, 10)

    # ユークリッド距離で近似べクトルデータを取得
    # r50 = Vector50(DB).get_distance_by_vec(v50, 50)

    average = sum([vec[2] for vec in r50]) / len(r50)
    veclist = []

    for i in range(len(r50)):
        veclist.append([r50[i][0].strftime('%Y-%m-%d'), r50[i][1], r50[i][2]])

    return veclist, average



def vector_rank(
    date: datetime.date,
    DB = None
) -> list:
    df = AnalysisVector50(DB).get_nonzero_rank(
        date.strftime('%Y-%m-%d')
    )
    
    r50DayOne = []
    r50DayTwo = []
    r50DayThree = []
    r50WeekOne = []
    #resultsv100 = []

    #for idx, _r in enumerate([r50, r100]):
    for _r in df:
        # jsonをデコード
        _v = json.loads(_r[4])

        for v in _v:
            try:
                # 近似ベクトルデータトップ１０から、５日後までの株価情報を取得

                # yyyy-mm-dd形式の日付文字列をdatetime型に変換
                _date = datetime.datetime.strptime(v[0], '%Y-%m-%d')
                sdate = v[0]
                edate = (_date + datetime.timedelta(days=15)).strftime('%Y-%m-%d')
                
                h = HistoryDate(DB).get_data_by_date_range(v[1], sdate, edate)

                _rate = rate(h)

                r50DayOne.append({
                    'Rate': _rate[0],
                    'Date': v[0],
                    'companyCode': v[1],
                    'companyCodeOrg': _r[1],
                })
                r50DayTwo.append({
                    'Rate': _rate[1],
                    'Date': v[0],
                    'companyCode': v[1],
                    'companyCodeOrg': _r[1],
                })
                r50DayThree.append({
                    'Rate': _rate[2],
                    'Date': v[0],
                    'companyCode': v[1],
                    'companyCodeOrg': _r[1],
                })
                r50WeekOne.append({
                    'Rate': _rate[4],
                    'Date': v[0],
                    'companyCode': v[1],
                    'companyCodeOrg': _r[1],
                })
                
            except Exception as e:
                print('ERROR!!  ', e)

    # 各配列をRateの降順にソート
    r50DayOne = sorted(r50DayOne, key=lambda x: x['Rate'], reverse=True)
    r50DayTwo = sorted(r50DayTwo, key=lambda x: x['Rate'], reverse=True)
    r50DayThree = sorted(r50DayThree, key=lambda x: x['Rate'], reverse=True)
    r50WeekOne = sorted(r50WeekOne, key=lambda x: x['Rate'],  reverse=True)

    # 上位10件を返す
    r50DayOne = r50DayOne[:10]
    r50DayTwo = r50DayTwo[:10]
    r50DayThree = r50DayThree[:10]
    r50WeekOne = r50WeekOne[:10]
     
    return r50DayOne, r50DayTwo, r50DayThree, r50WeekOne


'''
配列の1番目のOpen価格と、1日後、2日後、3日後、5日後の
Open価格を比較し、比率を計算し返す
'''
def rate(
    df: list,
) -> list:
    # 1日後、2日後、3日後、5日後のOpen価格を取得
    rate = []
    for i in range(5):
        rate.append(float((df[i + 1][3] - df[0][3]) / df[0][3]))
    return rate

