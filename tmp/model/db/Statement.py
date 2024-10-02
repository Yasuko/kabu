import lib.pgsql as pgsql

class StatementType:
    id: str
    code: str
    acquisition_date: str
    DisclosedDate: str
    DisclosedTime: str
    LocalCode: int
    DisclosureNumber: int
    TypeOfDocument: str
    TypeOfCurrentPeriod: str
    CurrentPeriodStartDate: str
    CurrentPeriodEndDate: str
    CurrentFiscalYearStartDate: str
    CurrentFiscalYearEndDate: str
    NextFiscalYearStartDate: str
    NextFiscalYearEndDate: str
    NetSales: int
    OperatingProfit: int
    OrdinaryProfit: int
    Profit: int
    EarningsPerShare: float
    DilutedEarningsPerShare: float
    TotalAssets: int
    Equity: int
    EquityToAssetRatio: float
    BookValuePerShare: float
    CashFlowsFromOperatingActivities: int
    CashFlowsFromInvestingActivities: int
    CashFlowsFromFinancingActivities: int
    CashAndEquivalents: int
    ResultDividendPerShare1stQuarter: float
    ResultDividendPerShare2ndQuarter: float
    ResultDividendPerShare3rdQuarter: float
    ResultDividendPerShareFiscalYearEnd: float
    ResultDividendPerShareAnnual: float
    DistributionsPerUnit_REIT: float
    ResultTotalDividendPaidAnnual: float
    ResultPayoutRatioAnnual: float
    ForecastDividendPerShare1stQuarter: float
    ForecastDividendPerShare2ndQuarter: float
    ForecastDividendPerShare3rdQuarter: float
    ForecastDividendPerShareFiscalYearEnd: float
    ForecastDividendPerShareAnnual: float
    ForecastDistributionsPerUnit_REIT: float
    ForecastTotalDividendPaidAnnual: float
    ForecastPayoutRatioAnnual: float
    NextYearForecastDividendPerShare1stQuarter: float
    NextYearForecastDividendPerShare2ndQuarter: float
    NextYearForecastDividendPerShare3rdQuarter: float
    NextYearForecastDividendPerShareFiscalYearEnd: float
    NextYearForecastDividendPerShareAnnual: int
    NextYearForecastDistributionsPerUnit_REIT: int
    NextYearForecastPayoutRatioAnnual: float
    ForecastNetSales2ndQuarter: int
    ForecastOperatingProfit2ndQuarter: int
    ForecastOrdinaryProfit2ndQuarter: int
    ForecastProfit2ndQuarter: int
    ForecastEarningsPerShare2ndQuarter: int
    NextYearForecastNetSales2ndQuarter: int
    NextYearForecastOperatingProfit2ndQuarter: int
    NextYearForecastOrdinaryProfit2ndQuarter: int
    NextYearForecastProfit2ndQuarter: int
    NextYearForecastEarningsPerShare2ndQuarter: int
    ForecastNetSales: int
    ForecastOperatingProfit: int
    ForecastOrdinaryProfit: int
    ForecastProfit: int
    ForecastEarningsPerShare: int
    NextYearForecastNetSales: int
    NextYearForecastOperatingProfit: int
    NextYearForecastOrdinaryProfit: int
    NextYearForecastProfit: int
    NextYearForecastEarningsPerShare: int
    MaterialChangesInSubsidiaries: str
    SignificantChangesInTheScopeOfConsolidation: str
    ChangesBasedOnRevisionsOfAccountingStandard: str
    ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard: str
    ChangesInAccountingEstimates: str
    RetrospectiveRestatement: str
    NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock: int
    NumberOfTreasuryStockAtTheEndOfFiscalYear: int
    AverageNumberOfShares: int
    NonConsolidatedNetSales: int
    NonConsolidatedOperatingProfit: int
    NonConsolidatedOrdinaryProfit: int
    NonConsolidatedProfit: int
    NonConsolidatedEarningsPerShare: float
    NonConsolidatedTotalAssets: int
    NonConsolidatedEquity: int
    NonConsolidatedEquityToAssetRatio: float
    NonConsolidatedBookValuePerShare: float
    ForecastNonConsolidatedNetSales2ndQuarter: int
    ForecastNonConsolidatedOperatingProfit2ndQuarter: int
    ForecastNonConsolidatedOrdinaryProfit2ndQuarter: int
    ForecastNonConsolidatedProfit2ndQuarter: int
    ForecastNonConsolidatedEarningsPerShare2ndQuarter: int
    NextYearForecastNonConsolidatedNetSales2ndQuarter: int
    NextYearForecastNonConsolidatedOperatingProfit2ndQuarter: int
    NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter: int
    NextYearForecastNonConsolidatedProfit2ndQuarter: int
    NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter: int
    ForecastNonConsolidatedNetSales: int
    ForecastNonConsolidatedOperatingProfit: int
    ForecastNonConsolidatedOrdinaryProfit: int
    ForecastNonConsolidatedProfit: int
    ForecastNonConsolidatedEarningsPerShare: int
    NextYearForecastNonConsolidatedNetSales: int
    NextYearForecastNonConsolidatedOperatingProfit: int
    NextYearForecastNonConsolidatedOrdinaryProfit: int
    NextYearForecastNonConsolidatedProfit: int
    NextYearForecastNonConsolidatedEarningsPerShare: int
    createdAt: str


class Statement:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    def insert (self, data: StatementType):
        insert_query = """
        INSERT INTO statement (
            id, code, acquisition_date, DisclosedDate, DisclosedTime, LocalCode, 
            DisclosureNumber, TypeOfDocument, TypeOfCurrentPeriod, CurrentPeriodStartDate, 
            CurrentPeriodEndDate, CurrentFiscalYearStartDate, CurrentFiscalYearEndDate, 
            NextFiscalYearStartDate, NextFiscalYearEndDate, NetSales, OperatingProfit, 
            OrdinaryProfit, Profit, EarningsPerShare, DilutedEarningsPerShare, TotalAssets, 
            Equity, EquityToAssetRatio, BookValuePerShare, CashFlowsFromOperatingActivities, 
            CashFlowsFromInvestingActivities, CashFlowsFromFinancingActivities, CashAndEquivalents, 
            ResultDividendPerShare1stQuarter, ResultDividendPerShare2ndQuarter, 
            ResultDividendPerShare3rdQuarter, ResultDividendPerShareFiscalYearEnd, 
            ResultDividendPerShareAnnual, DistributionsPerUnit_REIT, ResultTotalDividendPaidAnnual, 
            ResultPayoutRatioAnnual, ForecastDividendPerShare1stQuarter, 
            ForecastDividendPerShare2ndQuarter, ForecastDividendPerShare3rdQuarter, 
            ForecastDividendPerShareFiscalYearEnd, ForecastDividendPerShareAnnual, 
            ForecastDistributionsPerUnit_REIT, ForecastTotalDividendPaidAnnual, 
            ForecastPayoutRatioAnnual, NextYearForecastDividendPerShare1stQuarter, 
            NextYearForecastDividendPerShare2ndQuarter, NextYearForecastDividendPerShare3rdQuarter, 
            NextYearForecastDividendPerShareFiscalYearEnd, NextYearForecastDividendPerShareAnnual, 
            NextYearForecastDistributionsPerUnit_REIT, NextYearForecastPayoutRatioAnnual, 
            ForecastNetSales2ndQuarter, ForecastOperatingProfit2ndQuarter, 
            ForecastOrdinaryProfit2ndQuarter, ForecastProfit2ndQuarter, 
            ForecastEarningsPerShare2ndQuarter, NextYearForecastNetSales2ndQuarter, 
            NextYearForecastOperatingProfit2ndQuarter, NextYearForecastOrdinaryProfit2ndQuarter, 
            NextYearForecastProfit2ndQuarter, NextYearForecastEarningsPerShare2ndQuarter, 
            ForecastNetSales, ForecastOperatingProfit, ForecastOrdinaryProfit, ForecastProfit, 
            ForecastEarningsPerShare, NextYearForecastNetSales, NextYearForecastOperatingProfit, 
            NextYearForecastOrdinaryProfit, NextYearForecastProfit, NextYearForecastEarningsPerShare, 
            MaterialChangesInSubsidiaries, SignificantChangesInTheScopeOfConsolidation, 
            ChangesBasedOnRevisionsOfAccountingStandard, ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard, 
            ChangesInAccountingEstimates, RetrospectiveRestatement, 
            NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock, 
            NumberOfTreasuryStockAtTheEndOfFiscalYear, AverageNumberOfShares, 
            NonConsolidatedNetSales, NonConsolidatedOperatingProfit, NonConsolidatedOrdinaryProfit, 
            NonConsolidatedProfit, NonConsolidatedEarningsPerShare, NonConsolidatedTotalAssets, 
            NonConsolidatedEquity, NonConsolidatedEquityToAssetRatio, NonConsolidatedBookValuePerShare, 
            ForecastNonConsolidatedNetSales2ndQuarter, ForecastNonConsolidatedOperatingProfit2ndQuarter, 
            ForecastNonConsolidatedOrdinaryProfit2ndQuarter, ForecastNonConsolidatedProfit2ndQuarter, 
            ForecastNonConsolidatedEarningsPerShare2ndQuarter, NextYearForecastNonConsolidatedNetSales2ndQuarter, 
            NextYearForecastNonConsolidatedOperatingProfit2ndQuarter, NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter, 
            NextYearForecastNonConsolidatedProfit2ndQuarter, NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter, 
            ForecastNonConsolidatedNetSales, ForecastNonConsolidatedOperatingProfit, 
            ForecastNonConsolidatedOrdinaryProfit, ForecastNonConsolidatedProfit, 
            ForecastNonConsolidatedEarningsPerShare, NextYearForecastNonConsolidatedNetSales, 
            NextYearForecastNonConsolidatedOperatingProfit, NextYearForecastNonConsolidatedOrdinaryProfit, 
            NextYearForecastNonConsolidatedProfit, NextYearForecastNonConsolidatedEarningsPerShare, 
            createdAt
        ) VALUES (
            %(id)s, %(code)s, %(acquisition_date)s, %(DisclosedDate)s, %(DisclosedTime)s, %(LocalCode)s, 
            %(DisclosureNumber)s, %(TypeOfDocument)s, %(TypeOfCurrentPeriod)s, %(CurrentPeriodStartDate)s, 
            %(CurrentPeriodEndDate)s, %(CurrentFiscalYearStartDate)s, %(CurrentFiscalYearEndDate)s, 
            %(NextFiscalYearStartDate)s, %(NextFiscalYearEndDate)s, %(NetSales)s, %(OperatingProfit)s, 
            %(OrdinaryProfit)s, %(Profit)s, %(EarningsPerShare)s, %(DilutedEarningsPerShare)s, %(TotalAssets)s, 
            %(Equity)s, %(EquityToAssetRatio)s, %(BookValuePerShare)s, %(CashFlowsFromOperatingActivities)s, 
            %(CashFlowsFromInvestingActivities)s, %(CashFlowsFromFinancingActivities)s, %(CashAndEquivalents)s, 
            %(ResultDividendPerShare1stQuarter)s, %(ResultDividendPerShare2ndQuarter)s, 
            %(ResultDividendPerShare3rdQuarter)s, %(ResultDividendPerShareFiscalYearEnd)s, 
            %(ResultDividendPerShareAnnual)s, %(DistributionsPerUnit_REIT)s, %(ResultTotalDividendPaidAnnual)s, 
            %(ResultPayoutRatioAnnual)s, %(ForecastDividendPerShare1stQuarter)s, 
            %(ForecastDividendPerShare2ndQuarter)s, %(ForecastDividendPerShare3rdQuarter)s, 
            %(ForecastDividendPerShareFiscalYearEnd)s, %(ForecastDividendPerShareAnnual)s, 
            %(ForecastDistributionsPerUnit_REIT)s, %(ForecastTotalDividendPaidAnnual)s, 
            %(ForecastPayoutRatioAnnual)s, %(NextYearForecastDividendPerShare1stQuarter)s, 
            %(NextYearForecastDividendPerShare2ndQuarter)s, %(NextYearForecastDividendPerShare3rdQuarter)s, 
            %(NextYearForecastDividendPerShareFiscalYearEnd)s, %(NextYearForecastDividendPerShareAnnual)s, 
            %(NextYearForecastDistributionsPerUnit_REIT)s, %(NextYearForecastPayoutRatioAnnual)s, 
            %(ForecastNetSales2ndQuarter)s, %(ForecastOperatingProfit2ndQuarter)s, 
            %(ForecastOrdinaryProfit2ndQuarter)s, %(ForecastProfit2ndQuarter)s, 
            %(ForecastEarningsPerShare2ndQuarter)s, %(NextYearForecastNetSales2ndQuarter)s, 
            %(NextYearForecastOperatingProfit2ndQuarter)s, %(NextYearForecastOrdinaryProfit2ndQuarter)s, 
            %(NextYearForecastProfit2ndQuarter)s, %(NextYearForecastEarningsPerShare2ndQuarter)s, 
            %(ForecastNetSales)s, %(ForecastOperatingProfit)s, %(ForecastOrdinaryProfit)s, %(ForecastProfit)s, 
            %(ForecastEarningsPerShare)s, %(NextYearForecastNetSales)s, %(NextYearForecastOperatingProfit)s, 
            %(NextYearForecastOrdinaryProfit)s, %(NextYearForecastProfit)s, %(NextYearForecastEarningsPerShare)s, 
            %(MaterialChangesInSubsidiaries)s, %(SignificantChangesInTheScopeOfConsolidation)s, 
            %(ChangesBasedOnRevisionsOfAccountingStandard)s, %(ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard)s, 
            %(ChangesInAccountingEstimates)s, %(RetrospectiveRestatement)s, 
            %(NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock)s, 
            %(NumberOfTreasuryStockAtTheEndOfFiscalYear)s, %(AverageNumberOfShares)s, 
            %(NonConsolidatedNetSales)s, %(NonConsolidatedOperatingProfit)s, %(NonConsolidatedOrdinaryProfit)s, 
            %(NonConsolidatedProfit)s, %(NonConsolidatedEarningsPerShare)s, %(NonConsolidatedTotalAssets)s, 
            %(NonConsolidatedEquity)s, %(NonConsolidatedEquityToAssetRatio)s, %(NonConsolidatedBookValuePerShare)s, 
            %(ForecastNonConsolidatedNetSales2ndQuarter)s, %(ForecastNonConsolidatedOperatingProfit2ndQuarter)s, 
            %(ForecastNonConsolidatedOrdinaryProfit2ndQuarter)s, %(ForecastNonConsolidatedProfit2ndQuarter)s, 
            %(ForecastNonConsolidatedEarningsPerShare2ndQuarter)s, %(NextYearForecastNonConsolidatedNetSales2ndQuarter)s, 
            %(NextYearForecastNonConsolidatedOperatingProfit2ndQuarter)s, %(NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter)s, 
            %(NextYearForecastNonConsolidatedProfit2ndQuarter)s, %(NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter)s, 
            %(ForecastNonConsolidatedNetSales)s, %(ForecastNonConsolidatedOperatingProfit)s, 
            %(ForecastNonConsolidatedOrdinaryProfit)s, %(ForecastNonConsolidatedProfit)s, 
            %(ForecastNonConsolidatedEarningsPerShare)s, %(NextYearForecastNonConsolidatedNetSales)s, 
            %(NextYearForecastNonConsolidatedOperatingProfit)s, %(NextYearForecastNonConsolidatedOrdinaryProfit)s, 
            %(NextYearForecastNonConsolidatedProfit)s, %(NextYearForecastNonConsolidatedEarningsPerShare)s, 
            %(createdAt)s
        )
        """
        pgsql.execute(insert_query, (data,))


    def update (self, id, data: StatementType):
        update_query = """
        UPDATE statement
        SET
            code = %(code)s,
            acquisition_date = %(acquisition_date)s,
            DisclosedDate = %(DisclosedDate)s,
            DisclosedTime = %(DisclosedTime)s,
            LocalCode = %(LocalCode)s,
            DisclosureNumber = %(DisclosureNumber)s,
            TypeOfDocument = %(TypeOfDocument)s,
            TypeOfCurrentPeriod = %(TypeOfCurrentPeriod)s,
            CurrentPeriodStartDate = %(CurrentPeriodStartDate)s,
            CurrentPeriodEndDate = %(CurrentPeriodEndDate)s,
            CurrentFiscalYearStartDate = %(CurrentFiscalYearStartDate)s,
            CurrentFiscalYearEndDate = %(CurrentFiscalYearEndDate)s,
            NextFiscalYearStartDate = %(NextFiscalYearStartDate)s,
            NextFiscalYearEndDate = %(NextFiscalYearEndDate)s,
            NetSales = %(NetSales)s,
            OperatingProfit = %(OperatingProfit)s,
            OrdinaryProfit = %(OrdinaryProfit)s,
            Profit = %(Profit)s,
            EarningsPerShare = %(EarningsPerShare)s,
            DilutedEarningsPerShare = %(DilutedEarningsPerShare)s,
            TotalAssets = %(TotalAssets)s,
            Equity = %(Equity)s,
            EquityToAssetRatio = %(EquityToAssetRatio)s,
            BookValuePerShare = %(BookValuePerShare)s,
            CashFlowsFromOperatingActivities = %(CashFlowsFromOperatingActivities)s,
            CashFlowsFromInvestingActivities = %(CashFlowsFromInvestingActivities)s,
            CashFlowsFromFinancingActivities = %(CashFlowsFromFinancingActivities)s,
            CashAndEquivalents = %(CashAndEquivalents)s,
            ResultDividendPerShare1stQuarter = %(ResultDividendPerShare1stQuarter)s,
            ResultDividendPerShare2ndQuarter = %(ResultDividendPerShare2ndQuarter)s,
            ResultDividendPerShare3rdQuarter = %(ResultDividendPerShare3rdQuarter)s,
            ResultDividendPerShareFiscalYearEnd = %(ResultDividendPerShareFiscalYearEnd)s,
            ResultDividendPerShareAnnual = %(ResultDividendPerShareAnnual)s,
            DistributionsPerUnit_REIT = %(DistributionsPerUnit_REIT)s,
            ResultTotalDividendPaidAnnual = %(ResultTotalDividendPaidAnnual)s,
            ResultPayoutRatioAnnual = %(ResultPayoutRatioAnnual)s,
            ForecastDividendPerShare1stQuarter = %(ForecastDividendPerShare1stQuarter)s,
            ForecastDividendPerShare2ndQuarter = %(ForecastDividendPerShare2ndQuarter)s,
            ForecastDividendPerShare3rdQuarter = %(ForecastDividendPerShare3rdQuarter)s,
            ForecastDividendPerShareFiscalYearEnd = %(ForecastDividendPerShareFiscalYearEnd)s,
            ForecastDividendPerShareAnnual = %(ForecastDividendPerShareAnnual)s,
            ForecastDistributionsPerUnit_REIT = %(ForecastDistributionsPerUnit_REIT)s,
            ForecastTotalDividendPaidAnnual = %(ForecastTotalDividendPaidAnnual)s,
            ForecastPayoutRatioAnnual = %(ForecastPayoutRatioAnnual)s,
            NextYearForecastDividendPerShare1stQuarter = %(NextYearForecastDividendPerShare1stQuarter)s,
            NextYearForecastDividendPerShare2ndQuarter = %(NextYearForecastDividendPerShare2ndQuarter)s,
            NextYearForecastDividendPerShare3rdQuarter = %(NextYearForecastDividendPerShare3rdQuarter)s,
            NextYearForecastDividendPerShareFiscalYearEnd = %(NextYearForecastDividendPerShareFiscalYearEnd)s,
            NextYearForecastDividendPerShareAnnual = %(NextYearForecastDividendPerShareAnnual)s,
            NextYearForecastDistributionsPerUnit_REIT = %(NextYearForecastDistributionsPerUnit_REIT)s,
            NextYearForecastPayoutRatioAnnual = %(NextYearForecastPayoutRatioAnnual)s,
            ForecastNetSales2ndQuarter = %(ForecastNetSales2ndQuarter)s,
            ForecastOperatingProfit2ndQuarter = %(ForecastOperatingProfit2ndQuarter)s,
            ForecastOrdinaryProfit2ndQuarter = %(ForecastOrdinaryProfit2ndQuarter)s,
            ForecastProfit2ndQuarter = %(ForecastProfit2ndQuarter)s,
            ForecastEarningsPerShare2ndQuarter = %(ForecastEarningsPerShare2ndQuarter)s,
            NextYearForecastNetSales2ndQuarter = %(NextYearForecastNetSales2ndQuarter)s,
            NextYearForecastOperatingProfit2ndQuarter = %(NextYearForecastOperatingProfit2ndQuarter)s,
            NextYearForecastOrdinaryProfit2ndQuarter = %(NextYearForecastOrdinaryProfit2ndQuarter)s,
            NextYearForecastProfit2ndQuarter = %(NextYearForecastProfit2ndQuarter)s,
            NextYearForecastEarningsPerShare2ndQuarter = %(NextYearForecastEarningsPerShare2ndQuarter)s,
            ForecastNetSales = %(ForecastNetSales)s,
            ForecastOperatingProfit = %(ForecastOperatingProfit)s,
            ForecastOrdinaryProfit = %(ForecastOrdinaryProfit)s,
            ForecastProfit = %(ForecastProfit)s,
            ForecastEarningsPerShare = %(ForecastEarningsPerShare)s,
            NextYearForecastNetSales = %(NextYearForecastNetSales)s,
            NextYearForecastOperatingProfit = %(NextYearForecastOperatingProfit)s,
            NextYearForecastOrdinaryProfit = %(NextYearForecastOrdinaryProfit)s,
            NextYearForecastProfit = %(NextYearForecastProfit)s,
            NextYearForecastEarningsPerShare = %(NextYearForecastEarningsPerShare)s,
            MaterialChangesInSubsidiaries = %(MaterialChangesInSubsidiaries)s,
            SignificantChangesInTheScopeOfConsolidation = %(SignificantChangesInTheScopeOfConsolidation)s,
            ChangesBasedOnRevisionsOfAccountingStandard = %(ChangesBasedOnRevisionsOfAccountingStandard)s,
            ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard = %(ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard)s,
            ChangesInAccountingEstimates = %(ChangesInAccountingEstimates)s,
            RetrospectiveRestatement = %(RetrospectiveRestatement)s,
            NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock = %(NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock)s,
            NumberOfTreasuryStockAtTheEndOfFiscalYear = %(NumberOfTreasuryStockAtTheEndOfFiscalYear)s,
            AverageNumberOfShares = %(AverageNumberOfShares)s,
            NonConsolidatedNetSales = %(NonConsolidatedNetSales)s,
            NonConsolidatedOperatingProfit = %(NonConsolidatedOperatingProfit)s,
            NonConsolidatedOrdinaryProfit = %(NonConsolidatedOrdinaryProfit)s,
            NonConsolidatedProfit = %(NonConsolidatedProfit)s,
            NonConsolidatedEarningsPerShare = %(NonConsolidatedEarningsPerShare)s,
            NonConsolidatedTotalAssets = %(NonConsolidatedTotalAssets)s,
            NonConsolidatedEquity = %(NonConsolidatedEquity)s,
            NonConsolidatedEquityToAssetRatio = %(NonConsolidatedEquityToAssetRatio)s,
            NonConsolidatedBookValuePerShare = %(NonConsolidatedBookValuePerShare)s,
            ForecastNonConsolidatedNetSales2ndQuarter = %(ForecastNonConsolidatedNetSales2ndQuarter)s,
            ForecastNonConsolidatedOperatingProfit2ndQuarter = %(ForecastNonConsolidatedOperatingProfit2ndQuarter)s,
            ForecastNonConsolidatedOrdinaryProfit2ndQuarter = %(ForecastNonConsolidatedOrdinaryProfit2ndQuarter)s,
            ForecastNonConsolidatedProfit2ndQuarter = %(ForecastNonConsolidatedProfit2ndQuarter)s,
            ForecastNonConsolidatedEarningsPerShare2ndQuarter = %(ForecastNonConsolidatedEarningsPerShare2ndQuarter)s,
            NextYearForecastNonConsolidatedNetSales2ndQuarter = %(NextYearForecastNonConsolidatedNetSales2ndQuarter)s,
            NextYearForecastNonConsolidatedOperatingProfit2ndQuarter = %(NextYearForecastNonConsolidatedOperatingProfit2ndQuarter)s,
            NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter = %(NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter)s,
            NextYearForecastNonConsolidatedProfit2ndQuarter = %(NextYearForecastNonConsolidatedProfit2ndQuarter)s,
            NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter = %(NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter)s,
            ForecastNonConsolidatedNetSales = %(ForecastNonConsolidatedNetSales)s,
            ForecastNonConsolidatedOperatingProfit = %(ForecastNonConsolidatedOperatingProfit)s,
            ForecastNonConsolidatedOrdinaryProfit = %(ForecastNonConsolidatedOrdinaryProfit)s,
            ForecastNonConsolidatedProfit = %(ForecastNonConsolidatedProfit)s,
            ForecastNonConsolidatedEarningsPerShare = %(ForecastNonConsolidatedEarningsPerShare)s,
            NextYearForecastNonConsolidatedNetSales = %(NextYearForecastNonConsolidatedNetSales)s,
            NextYearForecastNonConsolidatedOperatingProfit = %(NextYearForecastNonConsolidatedOperatingProfit)s,
            NextYearForecastNonConsolidatedOrdinaryProfit = %(NextYearForecastNonConsolidatedOrdinaryProfit)s,
            NextYearForecastNonConsolidatedProfit = %(NextYearForecastNonConsolidatedProfit)s,
            NextYearForecastNonConsolidatedEarningsPerShare = %(NextYearForecastNonConsolidatedEarningsPerShare)s,
            createdAt = %(createdAt)s
        WHERE id = %(id)s
        """
        pgsql.execute(update_query, (data,))

    # IDからデータを取得
    def get_data_by_id(self, id):
        query = "SELECT * FROM statement WHERE id = %s"
        result = pgsql.execute(query, (id,))
        return result

    # codeからデータを取得し、createdAtでソートした結果の内10件を取得
    def get_data_by_code(code):
        query = """
            SELECT * FROM statement 
            WHERE code = %s 
            ORDER BY createdAt DESC 
            LIMIT 10
        """
        result = pgsql.execute(query, (code,))
        return result

    # DATEで日付の範囲を絞り込んで取得
    def get_data_by_date_range(start_date, end_date):
        query = """
            SELECT * FROM statement 
            WHERE acquisition_date BETWEEN %s AND %s
        """
        result = pgsql.execute(query, (start_date, end_date))
        return result