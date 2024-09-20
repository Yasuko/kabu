'''
市場区分コード及び市場区分名

コード	名称
0101	東証一部
0102	東証二部
0104	マザーズ
0105	TOKYO PRO MARKET
0106	JASDAQ スタンダード
0107	JASDAQ グロース
0109	その他
0111	プライム
0112	スタンダード
0113	ロース
'''

class MarketSchema:
    # テーブル作成クエリ
    create_table_query = """
    CREATE TABLE IF NOT EXISTS market (
        id SERIAL PRIMARY KEY,
        code INTEGER(3) NOT NULL,
        name TEXT NOT NULL
    );
    """

    # マスターデータ
    market_data = [
        (101, "東証一部"),
        (102, "東証二部"),
        (104, "マザーズ"),
        (105, "TOKYO PRO MARKET"),
        (106, "JASDAQ スタンダード"),
        (107, "JASDAQ グロース"),
        (109, "その他"),
        (111, "プライム"),
        (112, "スタンダード"),
        (113, "グロース")
    ]

    # データ挿入クエリ
    insert_query = """
    INSERT INTO
    market (
        code, name
    ) VALUES (
        %s, %s
    );
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table market')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
    
    def insert_market_data(self):
        print('Inserting market data')
        try:
            self.DB.execute(self.insert_query, self.market_data)
        except Exception as e:
            print(e)
            exit()