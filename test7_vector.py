import time
import datetime
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.Vector50 import Vector50
from model.db.Vector100 import Vector100

from lib.utils import normalize

'''
株価情報から、ベクトルデータを作成しDBに登録する試験
'''

def saveVectorData(historys: list, dimension: int):

    if dimension == 50:
        cur = Vector50(db)
        vec = 10

    elif dimension == 100:
        cur = Vector100(db)
        vec = 20

    for i in range(len(historys) - dimension):
        v = normalize(historys[i:i+dimension], 18, vec)

        # 空の場合はスキップ
        if len(v) == 0:
            logMiss('Vector', str(historys[i+dimension][2]) + ' ' + str(historys[i+dimension][1]))
            continue
        #print('Vector:', v)
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
        print('Vector Success:', )

def logMiss (message1: str, message2: str):
    print('Miss conver ', message1, message2)
    print('---------------------------------')


company_codes = Industry().get_all_records()
# company_codes = Industry().get_records_by_company_code('6300')
db = Industry().DB

#print(company_codes)
#print(date_map)

# 今日の日付取得
day = datetime.datetime.now()
# 30日前の日付取得
day = day - datetime.timedelta(days=30)

for row in company_codes:
    #historys = HistoryDate(db).get_all_data_by_company_code(row[1])
    historys = HistoryDate(db).get_data_by_date_before(row[1], day)
    # saveVectorData(historys, 30)
    saveVectorData(historys, 50)
    saveVectorData(historys, 100)


