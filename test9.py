import datetime
import time
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.AnalysisDate import AnalysisDate


from lib.analysis import rate, vector_angle

'''
１日前、２日前、３日前、１週間前、２週間前からの株価から
変動率を計算しデータベースに保存する試験
'''

company_codes = Industry().get_all_records()
day = datetime.datetime.now()
print(company_codes)
#print(date_map)

for row in company_codes:
    print('Getting data for : ' + row[1])
    r = rate(row[1], day)
    if r == None:
        print('Unable to get data for : ' + row[1])
        continue
    v = vector_angle(row[1], day)
    if v == None:
        print('Unable to get data for : ' + row[1])
        continue
    r = AnalysisDate().add_exists_by_date_and_company_code(
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
            'Rad1': v[0],
            'Rad2': v[1],
            'Rad3': v[2],
            'Rad4': v[3],
            'Rad5': v[4],
            'Rad6': v[5],
            'Rad7': v[6],
            'Rad8': v[7],
            'Rad9': v[8],
            'Rad10': v[9]
        })
    #print('Analysis :', r)
    #time.sleep(20)





#print(r, v)
"""
historys = HistoryDate().get_data_by_date_range('1301', day - datetime.timedelta(days=15), day)
i = len(historys) - 1
print(historys)
# 1日前のOpen値と当日のOpen値の差を計算
rate = ((historys[i][3] - historys[i-1][3]) / historys[i-1][3]) * 100

# 2日前のOpen値と当日のOpen値の差を計算
rate2 = ((historys[i][3] - historys[i-2][3]) / historys[i-2][3]) * 100

# 3日前のOpen値と当日のOpen値の差を計算
rate3 = ((historys[i][3] - historys[i-3][3]) / historys[i-3][3]) * 100

# 1週間前のOpen値と当日のOpen値の差を計算
rate4 = ((historys[i][3] - historys[i-5][3]) / historys[i-5][3]) * 100

# 2週間前のOpen値と当日のOpen値の差を計算
rate5 = ((historys[i][3] - historys[i-10][3]) / historys[i-10][3]) * 100
    
print(rate, rate2, rate3, rate4, rate5)
"""

