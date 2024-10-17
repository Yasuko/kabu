import time
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.Vector30 import Vector30

from lib.utils import normalize

'''
株価情報から、ベクトルデータを作成しDBに登録する試験
'''

company_codes = Industry().get_all_records()
db = Industry().DB

#print(company_codes)
#print(date_map)

dimension = 30

for row in company_codes:
    historys = HistoryDate(db).get_all_data_by_company_code(row[1])
    for i in range(len(historys) - dimension):
        v = normalize(historys[i:i+dimension])

        # 空の場合はスキップ
        if len(v) == 0:
            continue

        # 指定の日付から、10日前までのベクトルデータを保存
        _r = Vector30(db).insert_exists_by_date_and_company_code(
                            historys[i+dimension][2],
                            historys[i+dimension][1],
                            {
                                'Date': historys[i+dimension][2],
                                'companyCode': historys[i+dimension][1],
                                'Vec': v
                            }
                        )
        # 保存が成功した場合、ベクトルデータを表示
        #if _r:


