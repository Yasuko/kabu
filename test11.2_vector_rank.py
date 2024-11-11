import datetime
from model.db.Industry import Industry

from lib.analysis_vector import vector_rank

'''
指定日の価格の動きをベクトル化し、過去の近似データを元に
未来の価格を予測する
'''

day = datetime.datetime.now()
day = day - datetime.timedelta(days=2)

db = Industry().DB

today =  day.strftime("%Y-%m-%d")
print('Getting data for : ' + today)

dayone, daytwo, daythree, weekone = vector_rank(day, db)

print('Analysis :', dayone)
print('Analysis :', daytwo)
print('Analysis :', daythree)
print('Analysis :', weekone)



#print('Analysis :', r)




