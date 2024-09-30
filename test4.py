import csv
import time
import yfinance as yf

from model.db.Industry import Industry
from model.db.CompanyOfficers import CompanyOfficers
from model.db.RiskInfo import RiskInfo
from model.db.MarketInfo import MarketInfo
from model.db.FinancialInfo import FinancialInfo
from model.db.DividendInfo import DividendInfo
from model.db.OtherInformation import OtherInformation

from model.schema.Industry import IndustryType, IndustryDBType, ConvertToIndustryType
from model.schema.CompanyOfficers import CompanyOfficersType, CompanyOfficersDBType, ConvertToCompanyOfficersType
from model.schema.RiskInfo import RiskInfoType, RiskInfoDBType, ConvertToRiskInfoType
from model.schema.MarketInfo import MarketInfoType, MarketInfoDBType, ConvertToMarketInfoType
from model.schema.FinancialInfo import FinancialInfoType, FinancialInfoDBType, ConvertToFinancialInfoType
from model.schema.DividendInfo import DividendInfoType, DividendInfoDBType, ConvertToDividendInfoType
from model.schema.OtherInformation import OtherInformationType, OtherInformationDBType, ConvertToOtherInformationType


def read_csv_as_dict(file_path):
    result = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, fieldnames=["company_code", "company_name", "market_cap", "price", "high", "low", "industry"])
        for row in csv_reader:
            result.append({
                "company_code": row["company_code"],
                "company_name": row["company_name"]
            })
    return result

# ファイルパスを指定
file_path = 'company_codes.csv'
data = read_csv_as_dict(file_path)

for row in data:
    count = 0
    workout = False
    while True:
        try:

            if count > 5:
                print('API Error')
                workout = True
                break

            msft = yf.Ticker(row['company_code'] + '.T')
            print(msft.session)
            data = msft.info
            #print('Return API Result :', data)
            
            if 'industryKey' in data:
                data['companyCode'] = row['company_code']
                #print(data)
                break
            print('API Result is None')
            time.sleep(3)
            count += 1
            continue

        except Exception as e:
            print(e)
            time.sleep(3)
            count += 1
            continue
    
    if workout:
        print('Unable to get data for : ' + row['company_code'])
        continue

    print('Inserting Industry : ' + row['company_code'])
    Industry().insert_record(ConvertToIndustryType(data))
    #print('Inserting CompanyOfficers')
    if 'companyOfficers' in data:
        CompanyOfficers().insert_record(ConvertToCompanyOfficersType(data['companyCode'], data['companyOfficers']))
    #print('Inserting RiskInfo')
    RiskInfo().insert_record(ConvertToRiskInfoType(data))
    #print('Inserting MarketInfo')
    MarketInfo().insert_record(ConvertToMarketInfoType(data))
    #print('Inserting FinancialInfo')
    FinancialInfo().insert_record(ConvertToFinancialInfoType(data))
    #print('Inserting DividendInfo')
    DividendInfo().insert_record(ConvertToDividendInfoType(data))
    #print('Inserting OtherInformation')
    OtherInformation().insert_record(ConvertToOtherInformationType(data))

    time.sleep(3)