import sys
import yfinance as yf

from model.db.HistoryDate import HistoryDate
#from model.schema.HistoryDate import HistoryDateType, HistoryDateDBType, ConvertToHistoryDateType

'''
株価情報を取得するサンプル
'''


while True:
    try:
        msft = yf.Ticker("9984.T")
        data = msft.history(start="2010-12-01", end="2010-12-31", period="1d")
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

    #HistoryDate().add_data_if_not_exists(d['Date'], d)
#r = msft.history(start="2022-12-10", end="2022-12-20", period="1d")

### Return Example ###
"""
{'Open': 1307.2576481450096, 'High': 1312.2162116379734, 'Low': 1282.4648306801905, 'Close': 1288.324951171875, 'Volume': 14686000, 'Dividends': 0.0, 'companyCode': '9984', 'Date': '2010-12-22', 'StockSplits': 0.0}
{'Open': 1280.210760975489, 'High': 1289.2263297147529, 'Low': 1273.899862858004, 'Close': 1279.3092041015625, 'Volume': 7171800, 'Dividends': 0.0, 'companyCode': '9984', 'Date': '2010-12-24', 'StockSplits': 0.0}
{'Open': 1279.7602268938522, 'High': 1286.0711262163297, 'Low': 1277.0555557556474, 'Close': 1283.366455078125, 'Volume': 7000600, 'Dividends': 0.0, 'companyCode': '9984', 'Date': '2010-12-27', 'StockSplits': 0.0}
{'Open': 1274.801608278533, 'High': 1276.1539437894367, 'Low': 1269.8430447385529, 'Close': 1270.2938232421875, 'Volume': 5889600, 'Dividends': 0.0, 'companyCode': '9984', 'Date': '2010-12-28', 'StockSplits': 0.0}
{'Open': 1278.4081900167785, 'High': 1281.5636404152685, 'Low': 1273.9004037332215, 'Close': 1276.154296875, 'Volume': 5338200, 'Dividends': 0.0, 'companyCode': '9984', 'Date': '2010-12-29', 'StockSplits': 0.0}
{'Open': 1274.3506385697372, 'High': 1276.153752313734, 'Low': 1264.4335129777548, 'Close': 1267.13818359375, 'Volume': 7367600, 'Dividends': 0.0, 'companyCode': '9984', 'Date': '2010-12-30', 'StockSplits': 0.0}
"""