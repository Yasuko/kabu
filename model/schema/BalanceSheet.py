'''
市場情報 (MarketInfo)
'''

from lib.utils import validate

'''
'''
class BalanceSheetType:
    companyCode: str
    Date: str
    TreasurySharesNumber: float
    OrdinarySharesNumber: float
    ShareIssued: float
    NetDebt: float
    TotalDebt: float
    TangibleBookValue: float
    InvestedCapital: float
    WorkingCapital: float
    NetTangibleAssets: float
    CapitalLeaseObligations: float
    CommonStockEquity: float
    TotalCapitalization: float
    TotalEquityGrossMinorityInterest: float
    MinorityInterest: float
    StockholdersEquity: float
    TreasuryStock: float
    RetainedEarnings: float
    AdditionalPaidInCapital: float
    CapitalStock: float
    CommonStock: float
    PreferredStock: float
    PreferredSecuritiesOutsideStockEquity: float
    TotalLiabilitiesNetMinorityInterest: float
    TotalNonCurrentLiabilitiesNetMinorityInterest: float
    OtherNonCurrentLiabilities: float
    NonCurrentPensionAndOtherPostretirementBenefitPlans: float
    TradeandOtherPayablesNonCurrent: float
    CurrentDeferredTaxesLiabilities: float
    NonCurrentDeferredTaxesLiabilities: float
    LongTermDebtAndCapitalLeaseObligation: float
    LongTermCapitalLeaseObligation: float
    LongTermDebt: float
    LongTermProvisions: float
    LongTermEquityInvestment: float
    LiabilitiesHeldforSaleNonCurrent: float
    CurrentLiabilities: float
    OtherCurrentLiabilities: float
    CurrentDebtAndCapitalLeaseObligation: float
    CurrentCapitalLeaseObligation: float
    CurrentDebt: float
    PensionandOtherPostRetirementBenefitPlansCurrent: float
    DefinedPensionBenefit: float
    Payables: float
    OtherPayable: float
    TotalTaxPayable: float
    AccountsPayable: float
    DividendsPayable: float
    CurrentNotesPayable: float
    TotalAssets: float
    TotalNonCurrentAssets: float
    OtherNonCurrentAssets: float
    CurrentDeferredTaxesAssets: float
    NonCurrentDeferredTaxesAssets: float
    InvestmentinFinancialAssets: float
    InvestmentsinSubsidiariesatCost: float
    InvestmentProperties: float
    InvestmentsinJointVenturesatCost: float
    InvestmentsinAssociatesatCost: float
    InvestmentsInOtherVenturesUnderEquityMethod: float
    OtherInvestments: float
    AvailableForSaleSecurities: float
    GoodwillAndOtherIntangibleAssets: float
    OtherIntangibleAssets: float
    Goodwill: float
    NetPPE: float
    GrossPPE: float
    ConstructionInProgress: float
    OtherProperties: float
    MachineryFurnitureEquipment: float
    BuildingsAndImprovements: float
    LandAndImprovements: float
    Properties: float
    CurrentAssets: float
    CurrentProvisions: float
    OtherCurrentAssets: float
    Inventory: float
    FinishedGoods: float
    WorkInProcess: float
    RawMaterials: float
    AccountsReceivable: float
    NonCurrentAccountsReceivable: float
    GrossAccountsReceivable: float
    TaxesReceivable: float
    CashCashEquivalentsAndShortTermInvestments: float
    CashCashEquivalentsAndFederalFundsSold: float
    CashEquivalents: float
    CashFinancial: float
    CashAndCashEquivalents: float
    OtherShortTermInvestments: float
    AccumulatedDepreciation: float
    OtherEquityInterest: float
    OtherEquityAdjustments: float
    AssetsHeldForSaleCurrent: float
    Receivables: float
    NotesReceivable: float
    OtherReceivables: float
    NonCurrentPrepaidAssets: float
    PrepaidAssets: float
    OtherInventories: float
    ImpairmentOfCapitalAssets: float
    FixedAssetsRevaluationReserve: float
    CurrentDeferredAssets: float
    NonCurrentDeferredAssets: float
    HeldToMaturitySecurities: float
    RestrictedCash: float
    DerivativeProductLiabilities: float
    CurrentDeferredRevenue: float
    NonCurrentDeferredRevenue: float
    FinancialAssets: float
    FinancialAssetsDesignatedasFairValueThroughProfitorLossTotal: float
    HedgingAssetsCurrent: float
    AllowanceForDoubtfulAccountsReceivable: float
    CurrentAccruedExpenses: float
    NonCurrentAccruedExpenses: float
    PayablesAndAccruedExpenses: float
    EmployeeBenefits: float
    CurrentDeferredLiabilities: float
    NonCurrentDeferredLiabilities: float
    OtherCurrentBorrowings: float
    IncomeTaxPayable: float
    InvestmentsAndAdvances: float
    ReceivablesAdjustmentsAllowances: float
    GainsLossesNotAffectingRetainedEarnings: float
    Leases: float
    TradingSecurities: float
    ForeignCurrencyTranslationAdjustments: float
    MinimumPensionLiabilities: float
    UnrealizedGainLoss: float
    CommercialPaper: float

class BalanceSheetDBType(BalanceSheetType):
    id: str
    createdAt: str

def ConvertToBalanceSheetType(data: dict) -> BalanceSheetType:
    result = {}
    keys = BalanceSheetType.__annotations__.keys()

    for key in data.keys():
        _key = key.replace(" ", "")
        if _key in keys:
            result[_key] = validate(data[key], BalanceSheetType.__annotations__[_key])
        else:
            result[_key] = validate('', BalanceSheetType.__annotations__[_key])

    for key in keys:
        if key not in result.keys():
            result[key] = 0.0
    return result

class BalanceSheet:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS balance_sheet (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20) NOT NULL,
    Date DATE NOT NULL,
    TreasurySharesNumber FLOAT NOT NULL,
    OrdinarySharesNumber FLOAT NOT NULL,
    ShareIssued FLOAT NOT NULL,
    NetDebt FLOAT NOT NULL,
    TotalDebt FLOAT NOT NULL,
    TangibleBookValue FLOAT NOT NULL,
    InvestedCapital FLOAT NOT NULL,
    WorkingCapital FLOAT NOT NULL,
    NetTangibleAssets FLOAT NOT NULL,
    CapitalLeaseObligations FLOAT NOT NULL,
    CommonStockEquity FLOAT NOT NULL,
    TotalCapitalization FLOAT NOT NULL,
    TotalEquityGrossMinorityInterest FLOAT NOT NULL,
    MinorityInterest FLOAT NOT NULL,
    StockholdersEquity FLOAT NOT NULL,
    TreasuryStock FLOAT NOT NULL,
    RetainedEarnings FLOAT NOT NULL,
    AdditionalPaidInCapital FLOAT NOT NULL,
    CapitalStock FLOAT NOT NULL,
    CommonStock FLOAT NOT NULL,
    PreferredStock FLOAT NOT NULL,
    PreferredSecuritiesOutsideStockEquity FLOAT NOT NULL,
    TotalLiabilitiesNetMinorityInterest FLOAT NOT NULL,
    TotalNonCurrentLiabilitiesNetMinorityInterest FLOAT NOT NULL,
    OtherNonCurrentLiabilities FLOAT NOT NULL,
    NonCurrentPensionAndOtherPostretirementBenefitPlans FLOAT NOT NULL,
    DefinedPensionBenefit FLOAT NOT NULL,
    TradeandOtherPayablesNonCurrent FLOAT NOT NULL,
    CurrentDeferredTaxesLiabilities FLOAT NOT NULL,
    NonCurrentDeferredTaxesLiabilities FLOAT NOT NULL,
    LongTermDebtAndCapitalLeaseObligation FLOAT NOT NULL,
    LongTermCapitalLeaseObligation FLOAT NOT NULL,
    LongTermDebt FLOAT NOT NULL,
    LongTermProvisions FLOAT NOT NULL,
    LongTermEquityInvestment FLOAT NOT NULL,
    LiabilitiesHeldforSaleNonCurrent FLOAT NOT NULL,
    CurrentLiabilities FLOAT NOT NULL,
    OtherCurrentLiabilities FLOAT NOT NULL,
    CurrentDebtAndCapitalLeaseObligation FLOAT NOT NULL,
    CurrentCapitalLeaseObligation FLOAT NOT NULL,
    CurrentDebt FLOAT NOT NULL,
    PensionandOtherPostRetirementBenefitPlansCurrent FLOAT NOT NULL,
    Payables FLOAT NOT NULL,
    OtherPayable FLOAT NOT NULL,
    TotalTaxPayable FLOAT NOT NULL,
    AccountsPayable FLOAT NOT NULL,
    DividendsPayable FLOAT NOT NULL,
    CurrentNotesPayable FLOAT NOT NULL,
    TotalAssets FLOAT NOT NULL,
    TotalNonCurrentAssets FLOAT NOT NULL,
    OtherNonCurrentAssets FLOAT NOT NULL,
    CurrentDeferredTaxesAssets FLOAT NOT NULL,
    NonCurrentDeferredTaxesAssets FLOAT NOT NULL,
    InvestmentinFinancialAssets FLOAT NOT NULL,
    InvestmentsinSubsidiariesatCost FLOAT NOT NULL,
    InvestmentProperties FLOAT NOT NULL,
    InvestmentsinJointVenturesatCost FLOAT NOT NULL,
    InvestmentsinAssociatesatCost FLOAT NOT NULL,
    InvestmentsInOtherVenturesUnderEquityMethod FLOAT NOT NULL,
    OtherInvestments FLOAT NOT NULL,
    AvailableForSaleSecurities FLOAT NOT NULL,
    GoodwillAndOtherIntangibleAssets FLOAT NOT NULL,
    OtherIntangibleAssets FLOAT NOT NULL,
    Goodwill FLOAT NOT NULL,
    NetPPE FLOAT NOT NULL,
    GrossPPE FLOAT NOT NULL,
    ConstructionInProgress FLOAT NOT NULL,
    OtherProperties FLOAT NOT NULL,
    MachineryFurnitureEquipment FLOAT NOT NULL,
    BuildingsAndImprovements FLOAT NOT NULL,
    LandAndImprovements FLOAT NOT NULL,
    Properties FLOAT NOT NULL,
    CurrentAssets FLOAT NOT NULL,
    CurrentProvisions FLOAT NOT NULL,
    OtherCurrentAssets FLOAT NOT NULL,
    Inventory FLOAT NOT NULL,
    FinishedGoods FLOAT NOT NULL,
    WorkInProcess FLOAT NOT NULL,
    RawMaterials FLOAT NOT NULL,
    AccountsReceivable FLOAT NOT NULL,
    NonCurrentAccountsReceivable FLOAT NOT NULL,
    GrossAccountsReceivable FLOAT NOT NULL,
    TaxesReceivable FLOAT NOT NULL,
    CashCashEquivalentsAndShortTermInvestments FLOAT NOT NULL,
    CashCashEquivalentsAndFederalFundsSold FLOAT NOT NULL,
    CashEquivalents FLOAT NOT NULL,
    CashFinancial FLOAT NOT NULL,
    CashAndCashEquivalents FLOAT NOT NULL,
    OtherShortTermInvestments FLOAT NOT NULL,
    AccumulatedDepreciation FLOAT NOT NULL,
    OtherEquityInterest FLOAT NOT NULL,
    OtherEquityAdjustments FLOAT NOT NULL,
    AssetsHeldForSaleCurrent FLOAT NOT NULL,
    Receivables FLOAT NOT NULL,
    NotesReceivable FLOAT NOT NULL,
    OtherReceivables FLOAT NOT NULL,
    NonCurrentPrepaidAssets FLOAT NOT NULL,
    PrepaidAssets FLOAT NOT NULL,
    OtherInventories FLOAT NOT NULL,
    ImpairmentOfCapitalAssets FLOAT NOT NULL,
    FixedAssetsRevaluationReserve FLOAT NOT NULL,
    CurrentDeferredAssets FLOAT NOT NULL,
    NonCurrentDeferredAssets FLOAT NOT NULL,
    HeldToMaturitySecurities FLOAT NOT NULL,
    RestrictedCash FLOAT NOT NULL,
    DerivativeProductLiabilities FLOAT NOT NULL,
    CurrentDeferredRevenue FLOAT NOT NULL,
    NonCurrentDeferredRevenue FLOAT NOT NULL,
    FinancialAssets FLOAT NOT NULL,
    FinancialAssetsDesignatedasFairValueThroughProfitorLossTotal FLOAT NOT NULL,
    HedgingAssetsCurrent FLOAT NOT NULL,
    AllowanceForDoubtfulAccountsReceivable FLOAT NOT NULL,
    CurrentAccruedExpenses FLOAT NOT NULL,
    NonCurrentAccruedExpenses FLOAT NOT NULL,
    PayablesAndAccruedExpenses FLOAT NOT NULL,
    EmployeeBenefits FLOAT NOT NULL,
    CurrentDeferredLiabilities FLOAT NOT NULL,
    NonCurrentDeferredLiabilities FLOAT NOT NULL,
    OtherCurrentBorrowings FLOAT NOT NULL,
    IncomeTaxPayable FLOAT NOT NULL,
    InvestmentsAndAdvances FLOAT NOT NULL,
    ReceivablesAdjustmentsAllowances FLOAT NOT NULL,
    GainsLossesNotAffectingRetainedEarnings FLOAT NOT NULL,
    Leases FLOAT NOT NULL,
    TradingSecurities FLOAT NOT NULL,
    ForeignCurrencyTranslationAdjustments FLOAT NOT NULL,
    MinimumPensionLiabilities FLOAT NOT NULL,
    UnrealizedGainLoss FLOAT NOT NULL,
    CommercialPaper FLOAT NOT NULL,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON balance_sheet (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table balance_sheet')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()

