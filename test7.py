import time
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.VectorDate import VectorDate

from lib.analysis import normalize


'''
株価情報から、ベクトルデータを作成しDBに登録する試験
'''

company_codes = Industry().get_all_records()

#print(company_codes)
#print(date_map)

for row in company_codes:
    historys = HistoryDate().get_all_data_by_company_code(row[1])
    print(row[1])
    for i in range(len(historys) - 10):
        v = normalize(historys[i:i+10])

        # 空の場合はスキップ
        if len(v) == 0:
            continue

        # 指定の日付から、10日前までのベクトルデータを保存
        _r = VectorDate().insert_exists_by_date_and_company_code(
                            historys[i+10][2],
                            historys[i+10][1],
                            {
                                'Date': historys[i+10][2],
                                'companyCode': historys[i+10][1],
                                'Vec': v
                            }
                        )
        # 保存が成功した場合、ベクトルデータを表示
        #if _r:


'''
historys = HistoryDate().get_all_data_by_company_code('165A')

for i in range(len(historys) - 10):
    v = normalize(historys[i:i+10])
    print(v)
    # 空の場合はスキップ
    if len(v) == 0:
        continue

    # 指定の日付から、10日前までのベクトルデータを保存
    _r = VectorDate().insert_exists_by_date_and_company_code(
                        historys[i+10][2],
                        historys[i+10][1],
                        {
                            'Date': historys[i+10][2],
                            'companyCode': historys[i+10][1],
                            'Vec': v
                        }
                    )
                    """
    # 保存が成功した場合、ベクトルデータを表示
    #if _r:
'''