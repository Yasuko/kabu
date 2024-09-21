'''
企業情報 (industory)

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
'''

class InfoSchema:
    # テーブル作成クエリ
    create_table_query = """
    CREATE TABLE IF NOT EXISTS info (
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
    );
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table info')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()