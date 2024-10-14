import csv
import time
import yfinance as yf
import datetime

from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate

from lib.utils import date_map_before_date

'''
DBに保存された企業情報から、株価情報を取得し、DBに登録する試験
'''


# ファイルパスを指定
company_codes = Industry().get_all_records()
db = Industry().DB

# 今日の日付を取得する
day = datetime.datetime.now()
# 3日前の日付を取得する
day = day - datetime.timedelta(days=3)

# 30日前の日付を取得する
day_before = day - datetime.timedelta(days=30)

print(day)
print(day_before)

interval = 1.7

for row in company_codes:
    count = 0
    workout = False
    print('Getting data for : ' + row[1])
    while True:
        try:

            if count > 3:
                print('API Error')
                workout = True
                break

            msft = yf.Ticker(row[1] + '.T')
            data = msft.history(start=day_before, end=day, period="1d")
            #print('Return API Result :', data)
            
            if 'Open' in data:
                #print(data)
                break
            print('API Result is None')
            time.sleep(interval)
            count += 1
            continue

        except Exception as e:
            print(e)
            time.sleep(interval)
            count += 1
            continue
        
    if workout:
        print('Unable to get data for : ' + row[1])
        workout = False
        continue
    for timestamp, d in data.to_dict(orient='index').items():

        d['companyCode'] = row[1]
        d['Date'] = timestamp.strftime('%Y-%m-%d')
        d['StockSplits'] = d['Stock Splits']
        del d['Stock Splits']

        HistoryDate(db).add_data_if_not_exists_by_date_and_company_code(
            d['Date'],
            d['companyCode'],
            d
        )
    
    time.sleep(interval)
