import datetime
import time
import yfinance as yf
from model.db.Industry import Industry
from model.db.BalanceSheet import BalanceSheet
from model.db.Financials import Financials

from model.schema.BalanceSheet import BalanceSheetType, ConvertToBalanceSheetType
from model.schema.Financials import FinancialsType, ConvertToFinancialsType


from lib.analysis import rate

'''
'''

#company_codes = Industry().get_all_records()
company_codes = Industry().get_records_by_company_code('2437')
day = datetime.datetime.now()
day = day - datetime.timedelta(days=1)

db = Industry().DB
#print(date_map)

for code in company_codes:
    print('Getting data for : ' + code[1])
    
    ticker = yf.Ticker(code[1] + '.T')
    #hist = ticker.history(period="max")
    financials = ticker.financials
    balance_sheet = ticker.balance_sheet

    #print('Financials :', financials)
    
    for record in balance_sheet:
        # print('Record :', balance_sheet[record])
        _data = ConvertToBalanceSheetType(balance_sheet[record])
        print('Data :', _data)
        print('Balarance :', code[1] , record)
        
        _data['companyCode'] = code[1]
        _data['Date'] = record.strftime("%Y-%m-%d")

        BalanceSheet(db).insert_exists_by_date_and_company_code(
            record.strftime("%Y-%m-%d"),
            code[1],
            _data
        )
        #time.sleep(10)
    
    for record in financials:
        # print('Record :', financials[record])
        _data = ConvertToFinancialsType(financials[record])
        print('Financials :', code[1] , record)
        
        _data['companyCode'] = code[1]
        _data['Date'] = record.strftime("%Y-%m-%d")

        Financials(db).insert_exists_by_date_and_company_code(
            record.strftime("%Y-%m-%d"),
            code[1],
            _data
        )
        #time.sleep(10)

    time.sleep(1.2)


