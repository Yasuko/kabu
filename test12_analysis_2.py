import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisDate import AnalysisDate

from lib.explain import press_converter
from lib.candle_pattern import detect_three_soldiers, detect_three_gaps

'''
１日前、２日前、３日前、１週間前、２週間前からの株価から
変動率を計算しデータベースに保存する試験
'''

company_codes = Industry().get_all_records()
day = datetime.datetime.now()
#day = day - datetime.timedelta(days=4)

db = Industry().DB
#print(date_map)

for row in company_codes:
    print('Getting data for : ' + row[1])
    
    candles = press_converter(row[1], day, db)
    
    # candles要素の数をカウント
    print('Candle count : ', len(candles))
    for index in range(len(candles) - 2):
        print('Candle : ', candles[index])

        # 三兵のパターンを検出
        three_soldiers = detect_three_soldiers(candles, candles[index])
        time.sleep(5)
    

    



    #print('Analysis :', r)
    #time.sleep(20)


