import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisDate import AnalysisDate


from lib.analysis import rate

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
    
    r = rate(row[1], day, db)
    if r == None:
        print('Unable to get data for : ' + row[1])
        continue

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
            'VolumeDay': r[0]['volume'],
            'VolumeOne': r[1]['volume'],
            'VolumeTwo': r[2]['volume'],
            'VolumeThree': r[3]['volume'],
            'VolumeWeekOne': r[4]['volume'],
            'VolumeWeekTwo': r[5]['volume'],
        })

    #print('Analysis :', r)
    #time.sleep(20)


