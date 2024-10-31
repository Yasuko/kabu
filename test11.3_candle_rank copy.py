import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisCandle import AnalysisCandle
from model.db.RankCandleBase import RankCandleBase

from lib.analysis import ranking, vector

'''
指定日の株価のランキングを計算しデータベースに保存する試験
'''

day = datetime.datetime.now()
day = day - datetime.timedelta(days=6)

db = Industry().DB

today =  day.strftime("%Y-%m-%d")
print('Getting data for : ' + today)



#print('Analysis :', r)




