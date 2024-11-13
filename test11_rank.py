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
day = day - datetime.timedelta(days=2)

db = Industry().DB

print('Getting data for : ' + day.strftime("%Y-%m-%d"))
upper, lower = ranking(day.strftime("%Y-%m-%d"), db)

print(upper)
if upper == None or lower == None:
    print('Unable to get data for : ')

upper['Date'] = day.strftime("%Y-%m-%d")
lower['Date'] = day.strftime("%Y-%m-%d")

#print('Upper : ', upper)


Rank(db).add_exists_by_date(day.strftime("%Y-%m-%d"), upper)
RankUnder(db).add_exists_by_date(day.strftime("%Y-%m-%d"), lower)


#print('Analysis :', r)




