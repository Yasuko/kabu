
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate

from lib.analysis import convert_date_to_week, convert_date_to_month
from lib.analysis import convert_date_to_3month, convert_date_to_year
from lib.analysis import convert_pressure

# ファイルパスを指定
company_codes = Industry().get_all_records()

#print(company_codes)
#print(date_map)

for row in company_codes:
    historys = HistoryDate().get_all_data_by_company_code(row[1])
    results = []
    for history in historys:
        results.append(convert_pressure(history))
    print(results)
        
    


    