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



'''
1. TreasurySharesNumber - 自己株式数
2. OrdinarySharesNumber - 普通株式数
3. ShareIssued - 発行株式数
4. NetDebt - 純負債
5. TotalDebt - 総負債
6. TangibleBookValue - 有形簿価
7. InvestedCapital - 投下資本
8. WorkingCapital - 運転資本
9. NetTangibleAssets - 純有形資産
10. CapitalLeaseObligations - 資本リース義務
11. CommonStockEquity - 普通株式持分
12. TotalCapitalization - 総資本化
13. TotalEquityGrossMinorityInterest - 少数株主持分控除前純資産
14. MinorityInterest - 少数株主持分
15. StockholdersEquity - 株主資本
16. TreasuryStock - 自己株式
17. RetainedEarnings - 利益剰余金
18. AdditionalPaidInCapital - 資本剰余金
19. CapitalStock - 資本金
20. CommonStock - 普通株
21. PreferredStock - 優先株
22. PreferredSecuritiesOutsideStockEquity - 株式持分外の優先証券
23. TotalLiabilitiesNetMinorityInterest - 少数株主持分控除後総負債
24. TotalNonCurrentLiabilitiesNetMinorityInterest - 少数株主持分控除後の長期負債
25. OtherNonCurrentLiabilities - その他の長期負債
26. NonCurrentPensionAndOtherPostretirementBenefitPlans - 長期退職給付引当金
27. TradeandOtherPayablesNonCurrent - 長期売掛金およびその他の債務
28. CurrentDeferredTaxesLiabilities - 短期繰延税金負債
29. NonCurrentDeferredTaxesLiabilities - 長期繰延税金負債
30. LongTermDebtAndCapitalLeaseObligation - 長期負債および資本リース義務
31. LongTermCapitalLeaseObligation - 長期資本リース義務
32. LongTermDebt - 長期負債
33. LongTermProvisions - 長期引当金
34. LongTermEquityInvestment - 長期株式投資
35. LiabilitiesHeldforSaleNonCurrent - 売却予定長期負債
36. CurrentLiabilities - 流動負債
37. OtherCurrentLiabilities - その他の流動負債
38. CurrentDebtAndCapitalLeaseObligation - 流動負債及び資本リース義務
39. CurrentCapitalLeaseObligation - 流動資本リース義務
40. CurrentDebt - 流動負債
41. PensionandOtherPostRetirementBenefitPlansCurrent - 短期退職給付引当金
42. DefinedPensionBenefit - 確定給付年金
43. Payables - 支払債務
44. OtherPayable - その他の支払
45. TotalTaxPayable - 未払税金総額
46. AccountsPayable - 買掛金
47. DividendsPayable - 未払い配当金
48. CurrentNotesPayable - 短期借入金
49. TotalAssets - 総資産
50. TotalNonCurrentAssets - 総非流動資産
51. OtherNonCurrentAssets - その他の非流動資産
52. CurrentDeferredTaxesAssets - 流動繰延税金資産
53. NonCurrentDeferredTaxesAssets - 非流動繰延税金資産
54. InvestmentinFinancialAssets - 金融資産への投資
55. InvestmentsinSubsidiariesatCost - 原価計上された子会社への投資
56. InvestmentProperties - 投資不動産
57. InvestmentsinJointVenturesatCost - 原価計上された共同事業への投資
58. InvestmentsinAssociatesatCost - 原価計上された関連会社への投資
59. InvestmentsInOtherVenturesUnderEquityMethod - 持分法適用投資
60. OtherInvestments - その他の投資
61. AvailableForSaleSecurities - 売却可能証券
62. GoodwillAndOtherIntangibleAssets - のれん及びその他の無形資産
63. OtherIntangibleAssets - その他の無形資産
64. Goodwill - のれん
65. NetPPE - 純有形固定資産
66. GrossPPE - 有形固定資産総額
67. ConstructionInProgress - 建設仮勘定
68. OtherProperties - その他の資産
69. MachineryFurnitureEquipment - 機械・家具・設備
70. BuildingsAndImprovements - 建物及び改良
71. LandAndImprovements - 土地及び改良
72. Properties - 資産物件
73. CurrentAssets - 流動資産
74. CurrentProvisions - 流動引当金
75. OtherCurrentAssets - その他の流動資産
76. Inventory - 在庫
77. FinishedGoods - 製品
78. WorkInProcess - 仕掛品
79. RawMaterials - 原材料
80. AccountsReceivable - 売掛金
81. NonCurrentAccountsReceivable - 非流動売掛金
82. GrossAccountsReceivable - 売掛金総額
83. TaxesReceivable - 未収税金
84. CashCashEquivalentsAndShortTermInvestments - 現金及び現金同等物並びに短期投資
85. CashCashEquivalentsAndFederalFundsSold - 現金および現金同等物ならびに連邦基金売却
86. CashEquivalents - 現金同等物
87. CashFinancial - 金融現金
88. CashAndCashEquivalents - 現金及び現金同等物
89. OtherShortTermInvestments - その他の短期投資
90. AccumulatedDepreciation - 減価償却累計額
91. OtherEquityInterest - その他の資本持分
92. OtherEquityAdjustments - その他の資本調整額
93. AssetsHeldForSaleCurrent - 売却予定資産
94. Receivables - 未収金
95. NotesReceivable - 受取手形
96. OtherReceivables - その他の未収金
97. NonCurrentPrepaidAssets - 非流動前払い資産
98. PrepaidAssets - 前払い資産
99. OtherInventories - その他の在庫
100. ImpairmentOfCapitalAssets - 資本資産の減損
101. FixedAssetsRevaluationReserve - 固定資産再評価準備金
102. CurrentDeferredAssets - 流動繰延資産
103. NonCurrentDeferredAssets - 非流動繰延資産
104. HeldToMaturitySecurities - 満期保有証券
105. RestrictedCash - 制限付き現金
106. DerivativeProductLiabilities - デリバティブ商品負債
107. CurrentDeferredRevenue - 流動繰延収益
108. NonCurrentDeferredRevenue - 非流動繰延収益
109. FinancialAssets - 金融資産
110. FinancialAssetsDesignatedasFairValueThroughProfitorLossTotal - 公正価値計上の対象となる金融資産総額
111. HedgingAssetsCurrent - 流動ヘッジ資産
112. AllowanceForDoubtfulAccountsReceivable - 貸倒引当金
113. CurrentAccruedExpenses - 流動未払費用
114. NonCurrentAccruedExpenses - 非流動未払費用
115. PayablesAndAccruedExpenses - 支払債務および未払費用
116. EmployeeBenefits - 従業員給付
117. CurrentDeferredLiabilities - 流動繰延負債
118. NonCurrentDeferredLiabilities - 非流動繰延負債
119. OtherCurrentBorrowings - その他の流動借入
120. IncomeTaxPayable - 未払法人税
121. InvestmentsAndAdvances - 投資および前渡金
122. ReceivablesAdjustmentsAllowances - 未収金調整及び引当金
123. GainsLossesNotAffectingRetainedEarnings - 繰越利益に影響しない損益
124. Leases - リース
125. TradingSecurities - 売買目的証券
126. ForeignCurrencyTranslationAdjustments - 外貨換算調整勘定
127. MinimumPensionLiabilities - 最低年金負債
128. UnrealizedGainLoss - 未実現損益
129. CommercialPaper - コマーシャルペーパー

'''