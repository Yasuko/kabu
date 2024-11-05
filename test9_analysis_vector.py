import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisVector50 import AnalysisVector50
from model.db.AnalysisVector100 import AnalysisVector100

from lib.explain import press_converter
from lib.analysis_vector import (
    vector
)

company_codes = Industry().get_all_records()
day = datetime.datetime.now()
day = day - datetime.timedelta(days=1)

db = Industry().DB
#print(date_map)

ScoreColumns = ['DayOneScore', 'DayTwoScore', 'DayThreeScore', 'WeekOneScore']

for row in company_codes:
    print('Getting data for : ' + row[1])
    try:    
        analysis = vector(row[1], day, db)
        print('Analysis :', analysis)
    except Exception as e:
        print(e)
    print('Role')
    time.sleep(60)
        
        
    

