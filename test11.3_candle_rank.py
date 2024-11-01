import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisCandle import AnalysisCandle
from model.db.RankCandleBase import RankCandleBase
from model.db.RankUnderCandleBase import RankUnderCandleBase

from lib.analysis import rankingAnalysisType1

'''
指定日の株価のランキングを計算しデータベースに保存する試験
'''

day = datetime.datetime.now()
day = day - datetime.timedelta(days=4)

db = Industry().DB

today =  day.strftime("%Y-%m-%d")
print('Getting data for : ' + today)

# ランキング取得
up, down = rankingAnalysisType1(today, db)

# print('Up :', up)
# print('Down :', down)

# DBにランキング情報を保存

up['Date'] = today
down['Date'] = today

RankCandleBase(db).add_exists_by_date(today, up)
RankUnderCandleBase(db).add_exists_by_date(today, down)


