import time
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.Vector10 import Vector10
from model.db.Vector20 import Vector20
from model.db.Vector30 import Vector30

from lib.analysis import normalize

'''
株価情報から、ベクトルデータを作成しDBに登録する試験
'''

def saveVectorData(historys: list, dimension: int):

    if dimension == 10:
        cur = Vector10(db)
    elif dimension == 20:
        cur = Vector20(db)
    elif dimension == 30:
        cur = Vector30(db)

    for i in range(len(historys) - dimension):
        v = normalize(historys[i:i+dimension])

        # 空の場合はスキップ
        if len(v) == 0:
            logMiss('Vector', str(historys[i+dimension][2]) + ' ' + str(historys[i+dimension][1]))
            continue

        _r = cur.insert_exists_by_date_and_company_code(
                            historys[i+dimension][2],
                            historys[i+dimension][1],
                            {
                                'Date': historys[i+dimension][2],
                                'companyCode': historys[i+dimension][1],
                                'Vec': v
                            }
                        )
        if _r == False:
            logMiss('Vector', str(historys[i+dimension][2]) + ' ' + str(historys[i+dimension][1]))
        # 保存が成功した場合、ベクトルデータを表示
        #if _r:

def logMiss (message1: str, message2: str):
    print('Miss conver ', message1, message2)
    print('---------------------------------')


#company_codes = Industry().get_all_records()
company_codes = Industry().get_records_by_company_code('6300')
db = Industry().DB

#print(company_codes)
#print(date_map)

dimension = 10

for row in company_codes:
    historys = HistoryDate(db).get_all_data_by_company_code(row[1])
    saveVectorData(historys, 10)
    saveVectorData(historys, 20)
    saveVectorData(historys, 30)


