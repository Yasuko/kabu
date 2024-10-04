import time
import datetime
import math
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.VectorDate import VectorDate

from lib.analysis import normalize
from lib.utils import angle


'''
ベクトルデータを検索し、近似データを取得する試験
'''
'''
company_codes = Industry().get_all_records()

#print(company_codes)
#print(date_map)

for row in company_codes:
    historys = HistoryDate().get_all_data_by_company_code(row[1])
    #print(historys[1+10:1+20])

    for i in range(len(historys) - 9):
        # ベクトルデータに変換
        v = normalize(historys[i:i+10])
        #print(v)
        # 内積計算で近似べクトルデータを取得
        r = VectorDate().get_dot_by_vec(v, 10)
        #print(r)

        results = []
        for _r in r:
            # 近似ベクトルデータトップ１０から、５日後までの株価情報を取得
            h = HistoryDate().get_data_by_date_range(_r[1], _r[0], _r[0] + datetime.timedelta(days=15))
            print(h)
            # 価格の変動を角度に変換
            results.append(angle([item[3] for item in h]))

        print(results)

'''
historys = HistoryDate().get_all_data_by_company_code(1815)
#print(historys[1+10:1+20])

for i in range(len(historys) - 9):
    # ノーマライズ
    v = normalize(historys[i:i+10])
    #print(v)
    # 内積計算で近似べクトルデータを取得
    r = VectorDate().get_dot_by_vec(v, 10)
    #print(r)

    results = []
    for _r in r:
        # 近似ベクトルデータトップ１０から、５日後までの株価情報を取得
        h = HistoryDate().get_data_by_date_range(_r[1], _r[0], _r[0] + datetime.timedelta(days=15))
        print(h)
        # 価格の変動を角度に変換
        results.append(angle([item[3] for item in h]))

    print(results)

    time.sleep(30)


