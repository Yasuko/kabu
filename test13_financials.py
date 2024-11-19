import datetime
import time
import yfinance as yf
from model.db.Industry import Industry
from model.db.AnalysisDate import AnalysisDate


from lib.analysis import rate

'''
'''

company_codes = Industry().get_all_records()
day = datetime.datetime.now()
day = day - datetime.timedelta(days=1)

db = Industry().DB
#print(date_map)

for code in company_codes:
    print('Getting data for : ' + code[1])
    
    ticker = yf.Ticker(code[1] + '.T')
    #hist = ticker.history(period="max")
    #financials = ticker.financials
    balance_sheet = ticker.balance_sheet

    #print('Financials :', financials)
    for record in balance_sheet:
        for key in balance_sheet.T:
            print('Key :', key)
            print('Record :', balance_sheet.T[key])


    time.sleep(20)


