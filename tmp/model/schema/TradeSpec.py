"""
投資部門別情報 (trade_spec) テーブルのスキーマ情報を保持するモジュール


"""


class TradeSpecSchema:
    # テーブル作成クエリ
    create_table_query = """
    CREATE TABLE IF NOT EXISTS trade_spec (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        PublishedDate DATE,
        StartDate DATE,
        EndDate DATE,
        Section integer,
        ProprietarySales NUMERIC,
        ProprietaryPurchases NUMERIC,
        ProprietaryTotal NUMERIC,
        ProprietaryBalance NUMERIC,
        BrokerageSales NUMERIC,
        BrokeragePurchases NUMERIC,
        BrokerageTotal NUMERIC,
        BrokerageBalance NUMERIC,
        TotalSales NUMERIC,
        TotalPurchases NUMERIC,
        TotalTotal NUMERIC,
        TotalBalance NUMERIC,
        IndividualsSales NUMERIC,
        IndividualsPurchases NUMERIC,
        IndividualsTotal NUMERIC,
        IndividualsBalance NUMERIC,
        ForeignersSales NUMERIC,
        ForeignersPurchases NUMERIC,
        ForeignersTotal NUMERIC,
        ForeignersBalance NUMERIC,
        SecuritiesCosSales NUMERIC,
        SecuritiesCosPurchases NUMERIC,
        SecuritiesCosTotal NUMERIC,
        SecuritiesCosBalance NUMERIC,
        InvestmentTrustsSales NUMERIC,
        InvestmentTrustsPurchases NUMERIC,
        InvestmentTrustsTotal NUMERIC,
        InvestmentTrustsBalance NUMERIC,
        BusinessCosSales NUMERIC,
        BusinessCosPurchases NUMERIC,
        BusinessCosTotal NUMERIC,
        BusinessCosBalance NUMERIC,
        OtherCosSales NUMERIC,
        OtherCosPurchases NUMERIC,
        OtherCosTotal NUMERIC,
        OtherCosBalance NUMERIC,
        InsuranceCosSales NUMERIC,
        InsuranceCosPurchases NUMERIC,
        InsuranceCosTotal NUMERIC,
        InsuranceCosBalance NUMERIC,
        CityBKsRegionalBKsEtcSales NUMERIC,
        CityBKsRegionalBKsEtcPurchases NUMERIC,
        CityBKsRegionalBKsEtcTotal NUMERIC,
        CityBKsRegionalBKsEtcBalance NUMERIC,
        TrustBanksSales NUMERIC,
        TrustBanksPurchases NUMERIC,
        TrustBanksTotal NUMERIC,
        TrustBanksBalance NUMERIC,
        OtherFinancialInstitutionsSales NUMERIC,
        OtherFinancialInstitutionsPurchases NUMERIC,
        OtherFinancialInstitutionsTotal NUMERIC,
        OtherFinancialInstitutionsBalance NUMERIC
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table trade_spec')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()