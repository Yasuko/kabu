import datetime
import time
from model.db.Industry import Industry
from model.db.Rank import Rank
from model.db.RankUnder import RankUnder
from model.db.RankVector10 import RankVector10
from model.db.RankVector20 import RankVector20
from model.db.RankVector30 import RankVector30

from lib.analysis import ranking, vector

'''
指定日の株価のランキングを計算しデータベースに保存する試験
'''

day = datetime.datetime.now()
day = day - datetime.timedelta(days=6)

db = Industry().DB

today =  day.strftime("%Y-%m-%d")
print('Getting data for : ' + today)

upper = Rank(db).get_by_date(today)
lower = RankUnder(db).get_by_date(today)

if upper == None or lower == None:
    print('Unable to get data for : ')

for r in upper:
    
    for target in [2,3,4,5,6,7]:
        for _r in r[target]:
            v10, v20, v30 = vector(_r, r[1], db)

            [RankVector10(db).add_data(_v10) for _v10 in v10]
            [RankVector20(db).add_data(_v20) for _v20 in v20]
            [RankVector30(db).add_data(_v30) for _v30 in v30]

            """
            if not RankVector10(db).check_exists_by_date_and_company_code(today, _r):
                print('Upper : ', _r)
                v10, v20, v30 = vector(_r, r[1], db)
                print('Vector : ', v10, v20, v30)
                #RankVector10(db).add_exists_by_date_and_company_code(today, _r, v10)
                #RankVector20(db).add_exists_by_date_and_company_code(today, _r, v20)
                #RankVector30(db).add_exists_by_date_and_company_code(today, _r, v30)
            else:
                print('Upper : ', _r, ' already exists')
            """
            # time.sleep(10)





#print('Analysis :', r)




