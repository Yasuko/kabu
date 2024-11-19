import sys
import time
import datetime
import yfinance as yf

from model.db.Information import Information
from model.db.Industry import Industry
from model.schema.Information import InformationType, ConvertToInformationType

'''
企業情報を取得し、DBに登録する
'''

company_codes = Industry().get_all_records()
#company_codes = Industry().get_records_by_company_code('2206')
db = Industry().DB
day = datetime.datetime.now()

for code in company_codes:
    try:
        msft = yf.Ticker(code[1] + '.T')
        data = msft.info
        
        if 'industryKey' in data:
            data['companyCode'] = code[1]
            data['Date'] = day.strftime("%Y-%m-%d")

            print('Inserting Industry', code[1])
            (Information(db).
                insert_exists_by_date_and_company_code(
                    day.strftime("%Y-%m-%d"),
                    code[1],
                    ConvertToInformationType(data)
                ))
            time.sleep(1.8)
            continue
        print('API Result is None ', code[1])
        time.sleep(1.8)

        continue

    except Exception as e:
        print('Error : ', code[1])
        print(data)
        print(e)
        time.sleep(1.8)
        continue

