import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisCandle import AnalysisCandle

from lib.explain import press_converter
from lib.trend_pattern_base import (
    trend_pattern_analysis
)


company_codes = Industry().get_all_records()
day = datetime.datetime.now()
day = day - datetime.timedelta(days=1)

db = Industry().DB
#print(date_map)

ScoreColumns = ['DayScore', 'DayOneScore', 'DayTwoScore', 'DayThreeScore', 'WeekOneScore']
UpColumns = ['DayUp', 'DayOneUp', 'DayTwoUp', 'DayThreeUp', 'WeekOneUp']
DownColumns = ['DayDown', 'DayOneDown', 'DayTwoDown', 'DayThreeDown', 'WeekOneDown']
TrendsColumns = ['DayTrends', 'DayOneTrends', 'DayTwoTrends', 'DayThreeTrends', 'WeekOneTrends']

for row in company_codes:
    print('Getting data for : ' + row[1])
    try:    
        candle = press_converter(row[1], day, db)
        scores_dict = {}

        for i, c in enumerate(candle):
            # candles要素の数をカウント
            # print('Candle count : ', len(c))

            score = 0
            up = 0
            down = 0
            trendos = []

            for index in range(9):
                u, d, s, t = trend_pattern_analysis(c[index]['price'], c[index + 1]['price'])
                
                up += u
                down += d
                score += s
                trendos.extend(t)

            # 集計結果を辞書形式で格納
            scores_dict[UpColumns[i]] = up
            scores_dict[DownColumns[i]] = down
            scores_dict[ScoreColumns[i]] = score
            scores_dict[TrendsColumns[i]] = trendos
            
            print('Score :', score)
            #print('Trendos :', trendos)
            #print('Scores :', scores)
            #print('Scores Dict :', scores_dict)
            #time.sleep(0.3)

        # time.sleep(0.3)
        scores_dict['companyCode'] = row[1]
        scores_dict['Date'] = day.strftime('%Y-%m-%d')
        (AnalysisCandle(db)
            .add_exists_by_date_and_company_code(day.strftime('%Y-%m-%d'), row[1], scores_dict))
    except Exception as e:
        print(candle)
        print(e)
        
        
    

