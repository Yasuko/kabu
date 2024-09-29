import sys
import yfinance as yf

from model.db.HistoryDate import HistoryDate
#from model.schema.HistoryDate import HistoryDateType, HistoryDateDBType, ConvertToHistoryDateType

while True:
    try:
        msft = yf.Ticker("9984.T")
        data = msft.history(start="2022-12-10", end="2022-12-20", period="1d")
        #print('Return API Result :', data)
        break
    except Exception as e:
        print(e)
        sys.sleep(5)
        continue

#print('Return API Result :', data.to_dict(orient='index'))
for timestamp, d in data.to_dict(orient='index').items():

    d['companyCode'] = '9984'
    d['Date'] = timestamp.strftime('%Y-%m-%d')
    d['StockSplits'] = d['Stock Splits']
    del d['Stock Splits']
    print(d)

    HistoryDate().add_data_if_not_exists(d['Date'], d)
#r = msft.history(start="2022-12-10", end="2022-12-20", period="1d")

