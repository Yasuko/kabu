import time
import datetime
import yfinance as yf

from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.VectorDate import VectorDate

from lib.utils import build_date_map
from lib.analysis import normalize

'''
DBに保存された企業情報から、株価情報を取得し、DBに登録する試験
'''

# ファイルパスを指定
company_codes = Industry().get_all_records()
# 今日の日付を取得
day = time.strftime('%Y-%m-%d', time.localtime())
# 20日前の日付を取得
day_20 = day - datetime.timedelta(days=20)

for row in company_codes:
    count = 0
    workout = False
    print('Getting data for : ' + row[1])
    while True:
        try:
            # 連続3回失敗した場合は、エラーとして処理を終了
            if count > 3:
                print('API Error')
                workout = True
                break

            # 株価情報を取得
            msft = yf.Ticker(row[1] + '.T')
            data = msft.history(start=day_20, end=day, period="1d")
            
            # 取得したデータが正常であれば、ループを抜ける
            if 'Open' in data:
                #print(data)
                break
            print('API Result is None')
            time.sleep(2)
            count += 1
            continue

        except Exception as e:
            print(e)
            time.sleep(2)
            count += 1
            continue
    
    # ループを抜けた原因がAPIエラーの場合、次の企業情報を取得
    if workout:
        print('Unable to get data for : ' + row[1])
        workout = False
        continue

    # 取得したデータをDBに登録
    for timestamp, d in data.to_dict(orient='index').items():
        d['companyCode'] = row[1]
        d['Date'] = day
        d['StockSplits'] = d['Stock Splits']
        del d['Stock Splits']

        HistoryDate().add_data_if_not_exists_by_date_and_company_code(
            d['Date'],
            d['companyCode'],
            d
        )

    time.sleep(2)


for row in company_codes:
    historys = HistoryDate().get_latest_data(row[1])
    for i in range(len(historys) - 9):
        # ベクトルデータに変換
        r = normalize(historys[i:i+10], historys[i+10][2])

        # 指定の日付から、10日前までのベクトルデータを保存
        _r = VectorDate().insert_exists_by_date_and_company_code(
                            historys[i+10][2],
                            historys[i+10][1],
                            r
                        )
        # 保存が成功した場合、ベクトルデータを表示
        if _r:
            print(r)
    