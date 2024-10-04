import datetime
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.AnalysisDate import AnalysisDate
from model.db.VectorDate import VectorDate

from lib.analysis import rate, vector_angle

'''
１日前、２日前、３日前、１週間前、２週間前からの株価から
変動率を計算しデータベースに保存する試験
'''
'''
company_codes = Industry().get_all_records()

#print(company_codes)
#print(date_map)

for row in company_codes:
    historys = HistoryDate().get_all_data_by_company_code(row[1])
    results = []
    for history in historys:
        results.append(convert_pressure(history))
    print(results)
'''

day = datetime.datetime(2021, 1, 30)
r = rate('1301', day)
v = vector_angle('1301', day)

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

