import time
import datetime
import math
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.Vector50 import Vector50
from model.db.Vector100 import Vector100

from lib.utils import angle, normalize

'''
ベクトルデータを検索し、近似データを取得する試験
'''

date = datetime.datetime.now()
date = date - datetime.timedelta(days=6)

#historys = HistoryDate().get_all_data_by_company_code(1815)
historys = HistoryDate().get_latest_by_company_code('1815', date)
#print(historys[1+10:1+20])

for i in range(len(historys) - 29):
    # ノーマライズ
    v = normalize(historys[i:i+30])
    #print(v)
    # 内積計算で近似べクトルデータを取得
    r = Vector50().get_similarity_by_vec(v, 100)
    print(r)

    results = []
    '''
    for _r in r:
        # 近似ベクトルデータトップ１０から、５日後までの株価情報を取得
        h = HistoryDate().get_data_by_date_range(_r[1], _r[0], _r[0] + datetime.timedelta(days=15))
        print(h)
        # 価格の変動を角度に変換
        results.append(angle([item[3] for item in h]))

    print(results)
    '''

    time.sleep(30)


