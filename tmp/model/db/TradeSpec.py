import lib.pgsql as pgsql


"""
投資部門別情報

trade_spec (
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
);
"""


class TradeSpec:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    def insert (self, data):
        insert_query = """
        INSERT INTO breakdown (industry_id, Date, Code, LongSellValue, ShortSellWithoutMarginValue, MarginSellNewValue, MarginSellCloseValue, LongBuyValue, MarginBuyNewValue, MarginBuyCloseValue, LongSellVolume, ShortSellWithoutMarginVolume, MarginSellNewVolume, MarginSellCloseVolume, LongBuyVolume, MarginBuyNewVolume, MarginBuyCloseVolume)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        pgsql.execute(insert_query, data)

    def select (self, id):
        select_query = "SELECT * FROM trade_spec WHERE id = %s;"
        return pgsql.fetch_one(select_query, (id,))

    def update (self, id, data):
        update_query = """
        UPDATE breakdown
        SET industry_id = %s, Date = %s, Code = %s, LongSellValue = %s, ShortSellWithoutMarginValue = %s, MarginSellNewValue = %s, MarginSellCloseValue = %s, LongBuyValue = %s, MarginBuyNewValue = %s, MarginBuyCloseValue = %s, LongSellVolume = %s, ShortSellWithoutMarginVolume = %s, MarginSellNewVolume = %s, MarginSellCloseVolume = %s, LongBuyVolume = %s, MarginBuyNewVolume = %s, MarginBuyCloseVolume = %s
        WHERE id = %s;
        """
        pgsql.execute(update_query, (*data, id))

    def delete (self, id):
        delete_query = "DELETE FROM breakdown WHERE id = %s;"
        pgsql.execute(delete_query, (id,))

    def search_by_id (self, trade_id):
        select_query = "SELECT * FROM trade_spec WHERE trade_id = %s;"
        return pgsql.fetch_all(select_query, (trade_id,))

    def search_unique_industry_id (self, trade_id):
        select_query = """
        SELECT DISTINCT ON (industry_id) * FROM breakdown
        WHERE industry_id = %s;
        """
        return pgsql.fetch_all(select_query, (trade_id, ))


'''
https://jpx.gitbook.io/j-quants-ja/api-reference/trades_spec

投資部門別情報

変数名          	                説明	            型	    備考
PublishedDate                       公表日              String YY-MM-DD
StartDate                           開始日              String YY-MM-DD
EndDate                             終了日              String YY-MM-DD
Section                             市場名              String 市場名を参照
ProprietarySales                    自己計_売           Number
ProprietaryPurchases                自己計_買           Number
ProprietaryTotal                    自己計_合計         Number
ProprietaryBalance                  自己計_差引         Number
BrokerageSales                      委託計_売           Number
BrokeragePurchases                  委託計_買           Number
BrokerageTotal                      委託計_合計         Number
BrokerageBalance                    委託計_差引         Number
TotalSales                          総計_売             Number
TotalPurchases                      総計_買             Number
TotalTotal                          総計_合計           Number
TotalBalance                        総計_差引           Number
IndividualsSales                    個人_売             Number
IndividualsPurchases                個人_買             Number
IndividualsTotal                    個人_合計           Number
IndividualsBalance                  個人_差引           Number
ForeignersSales                     海外投資家_売       Number
ForeignersPurchases                 海外投資家_買       Number
ForeignersTotal                     海外投資家_合計     Number
ForeignersBalance                   海外投資家_差引     Number
SecuritiesCosSales                  証券会社_売         Number
SecuritiesCosPurchases              証券会社_買         Number
SecuritiesCosTotal                  証券会社_合計       Number
SecuritiesCosBalance                証券会社_差引       Number
InvestmentTrustsSales               投資信託_売         Number
InvestmentTrustsPurchases           投資信託_買         Number
InvestmentTrustsTotal               投資信託_合計       Number
InvestmentTrustsBalance             投資信託_差引       Number
BusinessCosSales                    事業法人_売         Number
BusinessCosPurchases                事業法人_買         Number
BusinessCosTotal                    事業法人_合計       Number
BusinessCosBalance                  事業法人_差引       Number
OtherCosSales                       その他法人_売       Number
OtherCosPurchases                   その他法人_買       Number
OtherCosTotal                       その他法人_合計     Number
OtherCosBalance                     その他法人_差引     Number
InsuranceCosSales                   生保・損保_売       Number
InsuranceCosPurchases               生保・損保_買       Number
InsuranceCosTotal                   生保・損保_合計     Number
InsuranceCosBalance                 生保・損保_差引     Number
CityBKsRegionalBKsEtcSales          都銀・地銀等_売     Number
CityBKsRegionalBKsEtcPurchases      都銀・地銀等_買     Number
CityBKsRegionalBKsEtcTotal          都銀・地銀等_合計   Number
CityBKsRegionalBKsEtcBalance        都銀・地銀等_差引   Number
TrustBanksSales                     信託銀行_売         Number
TrustBanksPurchases                 信託銀行_買         Number
TrustBanksTotal                     信託銀行_合計       Number
TrustBanksBalance                   信託銀行_差引       Number
OtherFinancialInstitutionsSales     その他金融機関_売   Number
OtherFinancialInstitutionsPurchases その他金融機関_買   Number
OtherFinancialInstitutionsTotal     その他金融機関_合計 Number
OtherFinancialInstitutionsBalance   その他金融機関_差引 Number

'''