'''
 (Financials)
'''

from lib.utils import validate

'''
'''
class FinancialsType:
    companyCode: str    # 企業コード
    Date: str           # 日付
    TaxEffectOfUnusualItems: float  # 税引き特別項目
    TaxRateForCalcs: float          # 計算用税率
    NormalizedEBITDA: float         # 正常化EBITDA
    TotalUnusualItems: float        # 特別項目の合計
    TotalUnusualItemsExcludingGoodwill: float   # 特別項目の合計（Goodwill除く）
    NetIncomeFromContinuingOperationNetMinorityInterest: float # 継続事業の純利益（少数株主持分を除く）
    ReconciledDepreciation: float   # 調整済み減価償却費
    ReconciledCostOfRevenue: float  # 調整済み売上原価
    EBITDA: float                   # EBITDA (営業利益＋減価償却費)
    EBIT: float                     # EBIT (営業利益)
    NetInterestIncome: float        # 純利息収益
    InterestExpense: float          # 利息費用
    OtherNonInterestExpense: float  # その他の非利息費用
    InterestIncome: float           # 利息収益
    NormalizedIncome: float         # 正常化純利益
    NetIncomeFromContinuingAndDiscontinuedOperation: float   # 継続事業と中断事業からの純利益
    TotalExpenses: float            # 経費の合計
    TotalOperatingIncomeAsReported: float   # 営業利益の合計（報告済み）
    DilutedAverageShares: float     # 普通株式の希釈加重平均数
    BasicAverageShares: float       # 普通株式の基本加重平均数
    DilutedEPS: float               # 希釈EPS
    BasicEPS: float                 # 基本EPS
    DilutedNIAvailtoComStockholders: float  # 希釈後の普通株主に利用可能な純利益
    NetIncomeCommonStockholders: float      # 普通株主に利用可能な純利益
    OtherunderPreferredStockDividend: float # 優先株式配当の他
    NetIncome: float                        # 純利益
    MinorityInterests: float                # 少数株主持分
    NetIncomeIncludingNoncontrollingInterests: float    # 非支配株主持分を含む純利益
    NetIncomeContinuousOperations: float    # 継続事業の純利益 
    NetIncomeDiscontinuousOperations: float  # 中断事業の純利益
    NetIncomeFromTaxLossCarryforward: float  # 繰越税損からの純利益
    TaxProvision: float             # 税金負担
    PretaxIncome: float             # 税引き前利益
    OtherNonOperatingIncomeExpenses: float  # その他の非営業収益費用
    SpecialIncomeCharges: float
    OtherSpecialCharges: float
    WriteOff: float
    NetNonOperatingInterestIncomeExpense: float
    InterestExpenseNonOperating: float
    InterestIncomeNonOperating: float
    OperatingIncome: float
    OperatingExpense: float
    OtherOperatingExpenses: float
    SellingGeneralAndAdministration: float
    SellingAndMarketingExpense: float
    GeneralAndAdministrativeExpense: float
    GrossProfit: float
    CostOfRevenue: float
    TotalRevenue: float
    OperatingRevenue: float
    RentExpenseSupplemental: float
    RentAndLandingFees: float
    RestructuringAndMergernAcquisition: float
    DepreciationAndAmortizationInIncomeStatement: float
    DepreciationIncomeStatement: float
    DepreciationAmortizationDepletionIncomeStatement: float
    ImpairmentOfCapitalAssets: float
    ResearchAndDevelopment: float
    TotalOtherFinanceCost: float
    Amortization: float
    AmortizationOfIntangiblesIncomeStatement: float
    OtherIncomeExpense: float
    GainOnSaleOfPpe: float
    GainOnSaleOfBusiness: float
    GainOnSaleOfSecurity: float
    EarningsFromEquityInterest: float
    EarningsFromEquityInterestNetOfTax: float
    AverageDilutionEarnings: float
    OtherGandA: float
    NetPolicyholderBenefitsAndClaims: float
    InsuranceAndClaims: float
    SalariesAndWages: float
    OccupancyAndEquipment: float

class FinancialsDBType(FinancialsType):
    id: str
    createdAt: str

def ConvertToFinancialsType(data: dict) -> FinancialsType:
    result = {}
    keys = FinancialsType.__annotations__.keys()
    for key in data.keys():
        _key = key.replace(" ", "")
        if _key in keys:
            result[_key] = validate(data[key], FinancialsType.__annotations__[_key])
        else:
            result[_key] = validate('', FinancialsType.__annotations__[_key])
    
    for key in keys:
        if key not in result.keys():
            result[key] = 0.0
    return result

class Financials:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS financials (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    companyCode VARCHAR(20) NOT NULL,
    Date DATE NOT NULL,
    TaxEffectOfUnusualItems FLOAT NOT NULL,
    TaxRateForCalcs FLOAT NOT NULL,
    NormalizedEBITDA FLOAT NOT NULL,
    TotalUnusualItems FLOAT NOT NULL,
    TotalUnusualItemsExcludingGoodwill FLOAT NOT NULL,
    NetIncomeFromContinuingOperationNetMinorityInterest FLOAT NOT NULL,
    ReconciledDepreciation FLOAT NOT NULL,
    ReconciledCostOfRevenue FLOAT NOT NULL,
    EBITDA FLOAT NOT NULL,
    EBIT FLOAT NOT NULL,
    NetInterestIncome FLOAT NOT NULL,
    InterestExpense FLOAT NOT NULL,
    OtherNonInterestExpense FLOAT NOT NULL,
    InterestIncome FLOAT NOT NULL,
    NormalizedIncome FLOAT NOT NULL,
    NetIncomeFromContinuingAndDiscontinuedOperation FLOAT NOT NULL,
    TotalExpenses FLOAT NOT NULL,
    TotalOperatingIncomeAsReported FLOAT NOT NULL,
    DilutedAverageShares FLOAT NOT NULL,
    BasicAverageShares FLOAT NOT NULL,
    DilutedEPS FLOAT NOT NULL,
    BasicEPS FLOAT NOT NULL,
    DilutedNIAvailtoComStockholders FLOAT NOT NULL,
    NetIncomeCommonStockholders FLOAT NOT NULL,
    OtherunderPreferredStockDividend FLOAT NOT NULL,
    NetIncome FLOAT NOT NULL,
    MinorityInterests FLOAT NOT NULL,
    NetIncomeIncludingNoncontrollingInterests FLOAT NOT NULL,
    NetIncomeContinuousOperations FLOAT NOT NULL,
    NetIncomeDiscontinuousOperations FLOAT NOT NULL,
    NetIncomeFromTaxLossCarryforward FLOAT NOT NULL,
    TaxProvision FLOAT NOT NULL,
    PretaxIncome FLOAT NOT NULL,
    OtherNonOperatingIncomeExpenses FLOAT NOT NULL,
    SpecialIncomeCharges FLOAT NOT NULL,
    OtherSpecialCharges FLOAT NOT NULL,
    WriteOff FLOAT NOT NULL,
    NetNonOperatingInterestIncomeExpense FLOAT NOT NULL,
    InterestExpenseNonOperating FLOAT NOT NULL,
    InterestIncomeNonOperating FLOAT NOT NULL,
    OperatingIncome FLOAT NOT NULL,
    OperatingExpense FLOAT NOT NULL,
    OtherOperatingExpenses FLOAT NOT NULL,
    SellingGeneralAndAdministration FLOAT NOT NULL,
    SellingAndMarketingExpense FLOAT NOT NULL,
    GeneralAndAdministrativeExpense FLOAT NOT NULL,
    GrossProfit FLOAT NOT NULL,
    CostOfRevenue FLOAT NOT NULL,
    TotalRevenue FLOAT NOT NULL,
    OperatingRevenue FLOAT NOT NULL,
    RentExpenseSupplemental FLOAT NOT NULL,
    RentAndLandingFees FLOAT NOT NULL,
    RestructuringAndMergernAcquisition FLOAT NOT NULL,
    DepreciationAndAmortizationInIncomeStatement FLOAT NOT NULL,
    DepreciationIncomeStatement FLOAT NOT NULL,
    DepreciationAmortizationDepletionIncomeStatement FLOAT NOT NULL,
    ImpairmentOfCapitalAssets FLOAT NOT NULL,
    ResearchAndDevelopment FLOAT NOT NULL,
    TotalOtherFinanceCost FLOAT NOT NULL,
    Amortization FLOAT NOT NULL,
    AmortizationOfIntangiblesIncomeStatement FLOAT NOT NULL,
    OtherIncomeExpense FLOAT NOT NULL,
    GainOnSaleOfPpe FLOAT NOT NULL,
    GainOnSaleOfBusiness FLOAT NOT NULL,
    GainOnSaleOfSecurity FLOAT NOT NULL,
    EarningsFromEquityInterest FLOAT NOT NULL,
    EarningsFromEquityInterestNetOfTax FLOAT NOT NULL,
    AverageDilutionEarnings FLOAT NOT NULL,
    OtherGandA FLOAT NOT NULL,
    NetPolicyholderBenefitsAndClaims FLOAT NOT NULL,
    InsuranceAndClaims FLOAT NOT NULL,
    SalariesAndWages FLOAT NOT NULL,
    OccupancyAndEquipment FLOAT NOT NULL,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON financials (companyCode);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table financials')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()

