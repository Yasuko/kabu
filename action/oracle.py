import time
import datetime
import yfinance as yf

from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.VectorDate import VectorDate

from lib.utils import angle
from lib.analysis import normalize


historys = HistoryDate().get_all_data_by_company_code(1815)
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

    time.sleep(30)


day = datetime.datetime(2021, 1, 30)
historys = HistoryDate().get_data_by_date_range('1301', day - datetime.timedelta(days=15), day)
i = len(historys) - 1
print(historys)
# 1日前のOpen値と当日のOpen値の差を計算
rate = ((historys[i][3] - historys[i-1][3]) / historys[i-1][3]) * 100

# 2日前のOpen値と当日のOpen値の差を計算
rate2 = ((historys[i][3] - historys[i-2][3]) / historys[i-2][3]) * 100

# 3日前のOpen値と当日のOpen値の差を計算
rate3 = ((historys[i][3] - historys[i-3][3]) / historys[i-3][3]) * 100

# 1週間前のOpen値と当日のOpen値の差を計算
rate4 = ((historys[i][3] - historys[i-5][3]) / historys[i-5][3]) * 100

# 2週間前のOpen値と当日のOpen値の差を計算
rate5 = ((historys[i][3] - historys[i-10][3]) / historys[i-10][3]) * 100
    
print(rate, rate2, rate3, rate4, rate5)


