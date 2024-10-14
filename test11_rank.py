import datetime
import time
from model.db.Industry import Industry
from model.db.Rank import Rank


from lib.analysis import rate, vector_angle

'''
１日前、２日前、３日前、１週間前、２週間前からの株価から
変動率を計算しデータベースに保存する試験
'''

company_codes = Industry().get_all_records()
day = datetime.datetime.now()
day = day - datetime.timedelta(days=5)

db = Industry().DB
#print(date_map)

for row in company_codes:
    print('Getting data for : ' + row[1])
    
    r = rate(row[1], day, db)
    if r == None:
        print('Unable to get data for : ' + row[1])
        continue
    """
    v = vector_angle(row[1], day, db)
    if v == None:
        print('Unable to get data for : ' + row[1])
        continue

    print(v)
    """

    r = AnalysisDate(db).add_exists_by_date_and_company_code(
        day.strftime("%Y-%m-%d"),
        row[1],
        {
            'companyCode': row[1],
            'Date': day,
            'Day': r[0]['rate'],
            'DayOne': r[1]['rate'],
            'DayTwo': r[2]['rate'],
            'DayThree': r[3]['rate'],
            'WeekOne': r[4]['rate'],
            'WeekTwo': r[5]['rate'],
            'PressDay': r[0]['pressure'],
            'PressOne': r[1]['pressure'],
            'PressTwo': r[2]['pressure'],
            'PressThree': r[3]['pressure'],
            'PressWeekOne': r[4]['pressure'],
            'PressWeekTwo': r[5]['pressure'],
        })

    #print('Analysis :', r)
    #time.sleep(20)



