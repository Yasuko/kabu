import lib.pgsql as pgsql

"""
上場銘柄一覧

id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
Date DATE,
Code VARCHAR(6),
CompanyName VARCHAR(150),
CompanyNameEnglish VARCHAR(150),
Sector17Code INTEGER(3),
Sector17CodeName VARCHAR(30),
Sector33Code INTEGER(4),
Sector33CodeName VARCHAR(30),
ScaleCategory VARCHAR(50),
MarketCode INTEGER(4),
MarketCodeName VARCHAR(30)
createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""


class Info:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    def insert (self, data):
        insert_query = """
        INSERT INTO info (
            Date, Code, CompanyName, CompanyNameEnglish, Sector17Code, Sector17CodeName, Sector33Code, Sector33CodeName, ScaleCategory, MarketCode, MarketCodeName
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
        """
        pgsql.execute(insert_query, data)

    def select (self, id):
        select_query = "SELECT * FROM info WHERE id = %s;"
        return pgsql.fetch_one(select_query, (id,))

    def update (self, id, data):
        update_query = """
        UPDATE info
        SET Date = %s, Code = %s, CompanyName = %s, CompanyNameEnglish = %s, Sector17Code = %s, Sector17CodeName = %s, Sector33Code = %s, Sector33CodeName = %s, ScaleCategory = %s, MarketCode = %s, MarketCodeName = %s
        WHERE id = %s;
        """
        pgsql.execute(update_query, (*data, id))

    def delete (self, id):
        delete_query = "DELETE FROM info WHERE id = %s;"
        pgsql.execute(delete_query, (id,))

    def search_by_code_sorted (self, code):
        search_query = "SELECT * FROM info WHERE Code = %s ORDER BY createdAt;"
        return pgsql.fetch_all(search_query, (code,))

    def get_unique_codes_sorted (self):
        search_query = """
        SELECT DISTINCT ON (Code) * FROM info
        ORDER BY Code, createdAt;
        """
        return pgsql.fetch_all(search_query, )





"""
https://jpx.gitbook.io/j-quants-ja/api-reference/listed_info

データ項目概要
変数名			説明		型	備考
Date 			情報適用年月日 	String YYYY-MM-DD
Code 			銘柄コード 	String
CompanyName 		会社名 		String
CompanyNameEnglish 	会社名（英語） 	String
Sector17Code 		17業種コード 	String 17業種コード及び業種名を参照
Sector17CodeName 	17業種コード名 	String 17業種コード及び業種名を参照
Sector33Code 		33業種コード 	String 33業種コード及び業種名を参照
Sector33CodeName 	33業種コード名 	String 33業種コード及び業種名を参照
ScaleCategory 		規模コード 	String
MarketCode 		市場区分コード 	String 市場区分コード及び市場区分を参照
MarketCodeName 		市場区分名 	String 市場区分コード及び市場区分を参照
MarginCode 		貸借信用区分 	String 1: 信用、2: 貸借、3: その他 ※1
MarginCodeName 		貸借信用区分名 	String ※1

※1  StandardおよびPremiumプランで取得可能な項目です
"""