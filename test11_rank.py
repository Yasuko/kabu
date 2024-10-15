import datetime
import time
from model.db.Industry import Industry
from model.db.Rank import Rank
from model.db.RankUnder import RankUnder


from lib.analysis import ranking, vector

'''
指定日の株価のランキングを計算しデータベースに保存する試験
'''

day = datetime.datetime.now()
day = day - datetime.timedelta(days=5)

db = Industry().DB

print('Getting data for : ' + day.strftime("%Y-%m-%d"))
upper, lower = ranking(day.strftime("%Y-%m-%d"), db)

if upper == None or lower == None:
    print('Unable to get data for : ')

for row in upper:

    print('Upper : ', row)


    time.sleep(10)
    for r in row['data']:
        print('Upper : ', r)
        v10, v20, v30 = vector(r, day, db)

        print('Vectore : ', v10)
        print('Vectore : ', v20)
        print('Vectore : ', v30)


"""
v = vector_angle(row[1], day, db)
if v == None:
    print('Unable to get data for : ' + row[1])
    continue

print(v)
"""


#print('Analysis :', r)




