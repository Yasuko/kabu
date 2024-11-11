import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisVector50 import AnalysisVector50
#from model.db.AnalysisVector100 import AnalysisVector100

from lib.explain import press_converter
import json
from lib.analysis_vector import (
    vector_analysis
)

company_codes = Industry().get_all_records()
day = datetime.datetime.now()
day = day - datetime.timedelta(days=2)

db = Industry().DB
#print(date_map)

ScoreColumns = ['DayOneScore', 'DayTwoScore', 'DayThreeScore', 'WeekOneScore']

for row in company_codes:
    print('Getting data for : ' + row[1])
    try:    
        VecList, average = vector_analysis(row[1], day, db)
        print('Analysis :', row[1])
        
        data = {
            'companyCode': row[1],
            'Date': day.strftime("%Y-%m-%d"),
            'Score': average,
            'VecList': json.dumps(VecList),
        }
        (AnalysisVector50(db).
            add_exists_by_date_and_company_code(
                day.strftime("%Y-%m-%d"),
                row[1],
                data
            ))
        
    except Exception as e:
        print('Error : ', row[1], e)

    #time.sleep(60)
        
        
    

