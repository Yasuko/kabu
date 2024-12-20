import csv
import math
import time
import yfinance as yf

from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate

from lib.utils import build_month_map

'''
DBに保存された企業情報から、株価情報を取得し、DBに登録する試験
'''


# ファイルパスを指定
# company_codes = Industry().get_all_records()
company_codes = Industry().get_records_by_company_code('8076')
date_map = build_month_map(2020, 2024)

#print(company_codes)
#print(date_map)

intervalTime = 1.8

for row in company_codes:
    count = 0
    workout = False
    print('Getting data for : ' + row[1])
    for date in date_map:
        while True:
            try:

                if count > 3:
                    print('API Error')
                    workout = True
                    break

                msft = yf.Ticker(row[1] + '.T')
                data = msft.history(start=date['start'], end=date['end'], period="1d")
                #data = msft.history(start='2020-01-01', end='2020-12-31', period="1d")
                #print('Return API Result :', data)
                
                if 'Open' in data:
                    #print(data)
                    break
                print('API Result is None')
                time.sleep(intervalTime)
                count += 1
                continue

            except Exception as e:
                print(e)
                time.sleep(intervalTime)
                count += 1
                continue
        
        if workout:
            print('Unable to get data for : ' + row[1])
            workout = False
            continue
        for timestamp, d in data.to_dict(orient='index').items():

            # Open, High, Low, Closeのいずれかが数値以外か、math.isnanがFalseの場合はスキップ
            for key in ['Open', 'High', 'Low', 'Close']:
                if type(d[key]) is not float or math.isnan(d[key]):
                    continue
                
             

            d['companyCode'] = row[1]
            d['Date'] = timestamp.strftime('%Y-%m-%d')
            d['StockSplits'] = d['Stock Splits']
            del d['Stock Splits']

            HistoryDate().add_data_if_not_exists_by_date_and_company_code(
                d['Date'],
                d['companyCode'],
                d
            )
        
        time.sleep(intervalTime)


    time.sleep(intervalTime)
    