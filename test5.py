import csv
import time
import yfinance as yf

from model.db.Industry import Industry

from lib.utils import build_date_map

# ファイルパスを指定
company_codes = Industry().get_all_records()
date_map = build_date_map()


for row in company_codes:
    count = 0
    workout = False
    while True:

        try:

            if count > 5:
                print('API Error')
                workout = True
                break

            msft = yf.Ticker(row['companyCode'] + '.T')
            data = msft.history(start="2022-12-10", end="2022-12-20", period="1d")
            #print('Return API Result :', data)
            
            if 'industryKey' in data:
                #print(data)
                break
            print('API Result is None')
            time.sleep(3)
            count += 1
            continue

        except Exception as e:
            print(e)
            time.sleep(3)
            count += 1
            continue
    
    if workout:
        print('Unable to get data for : ' + row['company_code'])
        continue


    time.sleep(3)