import time
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.VectorDate import VectorDate

from lib.analysis import convert_vector


'''
株価情報から、ベクトルデータを作成しDBに登録する試験
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

historys = HistoryDate().get_all_data_by_company_code(1815)


for i in range(len(historys) - 9):
    r = convert_vector(historys[i:i+10], historys[i+10][2])
    print(r)
    _r = VectorDate().get_dot_by_vec(r['Vec'], 10)
    print(_r)

    time.sleep(30)