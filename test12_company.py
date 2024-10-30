import datetime
import time
from model.db.Industry import Industry


'''
企業情報の更新試験
'''

day = datetime.datetime.now()
day = day - datetime.timedelta(days=6)

db = Industry().DB

today =  day.strftime("%Y-%m-%d")
print('Getting data for : ' + today)
