import sys
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


while True:
    try:
        msft = yf.Ticker("9984.T")
        print(msft.session)
        data = msft.info
        data['companyCode'] = '9984'
        #print(data)
        break
    except Exception as e:
        print(e)
        sys.sleep(5)
        continue
#r = msft.history(start="2022-12-10", end="2022-12-20", period="1d")

"""
_industory = ConvertToIndustryType(data)
print(_industory)
_companyOfficers = ConvertToCompanyOfficersType(data['companyCode'], data['companyOfficers'])
print(_companyOfficers)
_riskInfo = ConvertToRiskInfoType(data)
print(_riskInfo)
_marketInfo = ConvertToMarketInfoType(data)
print(_marketInfo)
_financialInfo = ConvertToFinancialInfoType(data)
print(_financialInfo)
_dividendInfo = ConvertToDividendInfoType(data)
print(_dividendInfo)
_otherInformation = ConvertToOtherInformationType(data)
print(_otherInformation)
"""

print('Inserting Industry')
Industry().insert_record(ConvertToIndustryType(data))
print('Inserting CompanyOfficers')
CompanyOfficers().insert_record(ConvertToCompanyOfficersType(data['companyCode'], data['companyOfficers']))
print('Inserting RiskInfo')
RiskInfo().insert_record(ConvertToRiskInfoType(data))
print('Inserting MarketInfo')
MarketInfo().insert_record(ConvertToMarketInfoType(data))
print('Inserting FinancialInfo')
FinancialInfo().insert_record(ConvertToFinancialInfoType(data))
print('Inserting DividendInfo')
DividendInfo().insert_record(ConvertToDividendInfoType(data))
print('Inserting OtherInformation')
OtherInformation().insert_record(ConvertToOtherInformationType(data))


