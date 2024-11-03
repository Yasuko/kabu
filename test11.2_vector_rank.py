import datetime
import time
from model.db.Industry import Industry
from model.db.HistoryDate import HistoryDate
from model.db.AnalysisVector import AnalysisVector
from model.db.RankVector50 import RankVector50
from model.db.RankVector100 import RankVector100

from lib.analysis import rankingAnalysisVector, vector

'''
指定日の価格の動きをベクトル化し、過去の近似データを元に
未来の価格を予測する
'''

day = datetime.datetime.now()
day = day - datetime.timedelta(days=6)

db = Industry().DB

today =  day.strftime("%Y-%m-%d")
print('Getting data for : ' + today)

rank = rankingAnalysisVector(today, db)

rank['Date'] = today

print('Rank :', rank)



#print('Analysis :', r)




