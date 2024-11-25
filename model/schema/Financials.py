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
    SpecialIncomeCharges: float     # 特別収益費用
    OtherSpecialCharges: float      # その他の特別費用
    WriteOff: float                 # 償却
    NetNonOperatingInterestIncomeExpense: float # 非営業利息収益費用
    InterestExpenseNonOperating: float  # 非営業利息費用
    InterestIncomeNonOperating: float   # 非営業利息収益
    OperatingIncome: float          # 営業利益
    OperatingExpense: float         # 営業費用
    OtherOperatingExpenses: float   # その他の営業費用
    SellingGeneralAndAdministration: float      # 販売一般管理費
    SellingAndMarketingExpense: float           # 販売マーケティング費用
    GeneralAndAdministrativeExpense: float      # 一般管理費
    GrossProfit: float              # 粗利益
    CostOfRevenue: float            # 売上原価
    TotalRevenue: float             # 売上高
    OperatingRevenue: float         # 営業収益
    RentExpenseSupplemental: float  # 補足賃貸費用
    RentAndLandingFees: float       # 賃貸着陸料
    RestructuringAndMergernAcquisition: float   # 再編成と合併費用
    DepreciationAndAmortizationInIncomeStatement: float # 減価償却費
    DepreciationIncomeStatement: float          # 減価償却費
    DepreciationAmortizationDepletionIncomeStatement: float # 減価償却費
    ImpairmentOfCapitalAssets: float            # 資本資産の減損
    ResearchAndDevelopment: float           # 研究開発
    TotalOtherFinanceCost: float            # その他の財務費用
    Amortization: float                     # 減価償却費
    AmortizationOfIntangiblesIncomeStatement: float # 無形資産の減価償却費
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



'''
1. TaxEffectOfUnusualItems - 特殊項目の税効果
2. TaxRateForCalcs - 計算用税率
3. NormalizedEBITDA - 正常化後EBITDA
4. TotalUnusualItems - 特殊項目の合計
5. TotalUnusualItemsExcludingGoodwill - のれんを除く特殊項目の合計
6. NetIncomeFromContinuingOperationNetMinorityInterest - 少数株主持分を除く継続事業からの純利益
7. ReconciledDepreciation - 修正後減価償却費
8. ReconciledCostOfRevenue - 修正後売上原価
9. EBITDA - EBITDA（利息・税金・償却前利益）
10. EBIT - EBIT（利息・税金控除前利益）
11. NetInterestIncome - 純利息収入
12. InterestExpense - 利息費用
13. OtherNonInterestExpense - その他の無利息費用
14. InterestIncome - 利息収入
15. NormalizedIncome - 正常化後純利益
16. NetIncomeFromContinuingAndDiscontinuedOperation - 継続および中止事業からの純利益
17. TotalExpenses - 総費用
18. TotalOperatingIncomeAsReported - 報告されている営業利益総計
19. DilutedAverageShares - 希薄化後平均株式数
20. BasicAverageShares - 基本平均株式数
21. DilutedEPS - 希薄化後EPS
22. BasicEPS - 基本EPS
23. DilutedNIAvailtoComStockholders - コモン株主に帰属する希薄化後純利益
24. NetIncomeCommonStockholders - コモン株主に帰属する純利益
25. OtherunderPreferredStockDividend - 優先株配当の下のその他
26. NetIncome - 純利益
27. MinorityInterests - 少数株主持分
28. NetIncomeIncludingNoncontrollingInterests - 非支配持分を含む純利益
29. NetIncomeContinuousOperations - 継続事業からの純利益
30. NetIncomeDiscontinuousOperations - 中止事業からの純利益
31. NetIncomeFromTaxLossCarryforward - 繰越税損からの純利益
32. TaxProvision - 税引当金
33. PretaxIncome - 税引前利益
34. OtherNonOperatingIncomeExpenses - その他の営業外損益
35. SpecialIncomeCharges - 特別収益費用
36. OtherSpecialCharges - その他の特別費用
37. WriteOff - 減損
38. NetNonOperatingInterestIncomeExpense - 純営業外利息損益
39. InterestExpenseNonOperating - 営業外利息費用
40. InterestIncomeNonOperating - 営業外利息収入
41. OperatingIncome - 営業利益
42. OperatingExpense - 営業費用
43. OtherOperatingExpenses - その他営業費用
44. SellingGeneralAndAdministration - 販売費及び一般管理費
45. SellingAndMarketingExpense - 販売及びマーケティング費用
46. GeneralAndAdministrativeExpense - 一般及び管理費用
47. GrossProfit - 粗利益
48. CostOfRevenue - 売上原価
49. TotalRevenue - 総収入
50. OperatingRevenue - 営業収入
51. RentExpenseSupplemental - 補足賃料費用
52. RentAndLandingFees - 賃料及び着陸料
53. RestructuringAndMergernAcquisition - リストラクチャリング及び合併・買収
54. DepreciationAndAmortizationInIncomeStatement - 損益計算書における減価償却及び償却費
55. DepreciationIncomeStatement - 損益計算書の減価償却費
56. DepreciationAmortizationDepletionIncomeStatement - 損益計算書の減価償却・償却・枯渇費
57. ImpairmentOfCapitalAssets - 資本資産の減損
58. ResearchAndDevelopment - 研究開発費
59. TotalOtherFinanceCost - その他の金融費用総計
60. Amortization - 償却
61. AmortizationOfIntangiblesIncomeStatement - 損益計算書における無形資産の償却
62. OtherIncomeExpense - その他収益費用
63. GainOnSaleOfPpe - 有形固定資産売却益
64. GainOnSaleOfBusiness - 事業売却益
65. GainOnSaleOfSecurity - 証券売却益
66. EarningsFromEquityInterest - 持分利益
67. EarningsFromEquityInterestNetOfTax - 税引後持分利益
68. AverageDilutionEarnings - 希薄化平均利益
69. OtherGandA - その他の一般及び管理費
70. NetPolicyholderBenefitsAndClaims - 保険契約者利益及びクレームの純額
71. InsuranceAndClaims - 保険及びクレーム
72. SalariesAndWages - 給与及び賃金
73. OccupancyAndEquipment - 占有及び設備費
'''