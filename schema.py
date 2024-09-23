import lib.pgsql as pgsql

import model.schema.AuthRefresh as AuthRefresh
import model.schema.AuthUser as AuthUser

import model.schema.History3Month as History3Month
import model.schema.History6Month as History6Month
import model.schema.HistoryDate as HistoryDate
import model.schema.HistoryMonth as HistoryMonth
import model.schema.HistoryWeek as HistoryWeek
import model.schema.HistoryYear as HistoryYear
import model.schema.Industry as Industry
import model.schema.RiskInfo as RiskInfo
import model.schema.CompanyOfficers as CompanyOfficers
import model.schema.MarketInfo as MarketInfo
import model.schema.FinancialInfo as FinancialInfo
import model.schema.DividendInfo as DividendInfo
import model.schema.OtherInformation as OtherInformation

import model.schema.Breakdown as Breakdown
import model.schema.IndustryCode17 as IndustryCode17
import model.schema.IndustryCode33 as IndustryCode33
import model.schema.Info as Info
import model.schema.Market as Market
import model.schema.Section as Section
import model.schema.Statement as Statement
import model.schema.TradeSpec as TradeSpec

DB = pgsql.PgSQL()

# Connect to the PostgreSQL database
try:
    DB.connect()
    DB.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    AuthRefresh.AuthRefresh(DB).create_table()
    AuthUser.AuthUser(DB).create_table()
    Industry.Industry(DB).create_table()
    RiskInfo.RiskInfo(DB).create_table()
    CompanyOfficers.CompanyOfficers(DB).create_table()
    MarketInfo.MarketInfo(DB).create_table()
    FinancialInfo.FinancialInfo(DB).create_table()
    DividendInfo.DividendInfo(DB).create_table()
    OtherInformation.OtherInformation(DB).create_table()
    History3Month.History3Month(DB).create_table()
    History6Month.History6Month(DB).create_table()
    HistoryDate.HistoryDate(DB).create_table()
    HistoryMonth.HistoryMonth(DB).create_table()
    HistoryWeek.HistoryWeek(DB).create_table()
    HistoryYear.HistoryYear(DB).create_table()
except Exception as e:
    print('Error connecting to the database')
    print(e)
    exit()


