import time
import yfinance as yf
import datetime

from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.AnalysisDate import AnalysisDate
from model.db.Rank import Rank
from model.db.RankUnder import RankUnder

from lib.analysis import ranking, vector
from lib.analysis import rate

# ファイルパスを指定
company_codes = Industry().get_all_records()
db = Industry().DB

# 今日の日付を取得する
day = datetime.datetime.now()

# 30日前の日付を取得する
day_before = day - datetime.timedelta(days=30)

interval = 1.7

'''

最新の株価取得

'''

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


'''

株価解析

'''
time.sleep(5)

for row in company_codes:
    print('Getting data for : ' + row[1])
    
    r = rate(row[1], day, db)
    if r == None:
        print('Unable to get data for : ' + row[1])
        continue

    r = AnalysisDate(db).add_exists_by_date_and_company_code(
        day.strftime("%Y-%m-%d"),
        row[1],
        {
            'companyCode': row[1],
            'Date': day,
            'Day': r[0]['rate'][0],
            'DayOne': r[1]['rate'][0],
            'DayTwo': r[2]['rate'][0],
            'DayThree': r[3]['rate'][0],
            'WeekOne': r[4]['rate'][0],
            'WeekTwo': r[5]['rate'][0],
            'VolumeDay': r[0]['volume'],
            'VolumeOne': r[1]['volume'],
            'VolumeTwo': r[2]['volume'],
            'VolumeThree': r[3]['volume'],
            'VolumeWeekOne': r[4]['volume'],
            'VolumeWeekTwo': r[5]['volume'],
        })


'''

ランキング生成

'''
time.sleep(5)

print('Getting data for : ' + day.strftime("%Y-%m-%d"))
upper, lower = ranking(day.strftime("%Y-%m-%d"), db)

if upper == None or lower == None:
    print('Unable to get data for : ')

upper['Date'] = day.strftime("%Y-%m-%d")
lower['Date'] = day.strftime("%Y-%m-%d")

#print('Upper : ', upper)


Rank(db).add_exists_by_date(day.strftime("%Y-%m-%d"), upper)
RankUnder(db).add_exists_by_date(day.strftime("%Y-%m-%d"), lower)