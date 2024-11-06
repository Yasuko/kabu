import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisVector50 import AnalysisVector50
#from model.db.AnalysisVector100 import AnalysisVector100

from lib.explain import press_converter
import json
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
        analysis, average = vector(row[1], day, db)
        print('Analysis :', row[1])
        '''
        data = {
            'companyCode': row[1],
            'Date': day.strftime("%Y-%m-%d"),
            'DayOne': average[0],
            'DayOneResult': json.dumps(analysis[0]),
            'DayTwo': average[1],
            'DayTwoResult': json.dumps(analysis[1]),
            'DayThree': average[2],
            'DayThreeResult': json.dumps(analysis[2]),
            'WeekOne': average[3],
            'WeekOneResult': json.dumps(analysis[3]),
        }
        (AnalysisVector50(db).
            add_exists_by_date_and_company_code(
                day.strftime("%Y-%m-%d"),
                row[1],
                data
            ))
        '''
        
    except Exception as e:
        print(e)

    #time.sleep(60)
        
        
    

