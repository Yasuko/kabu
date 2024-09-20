import lib.pgsql as pgsql

'''
17業種コード及び業種名

コード	名称
1       食品
2       エネルギー資源
3       建設・資材
4       素材・化学
5       医薬品
6       自動車・輸送機
7       鉄鋼・非鉄
8       機械
9       電機・精密
10      情報通信・サービスその他
11      電気・ガス
12      運輸・物流
13      商社・卸売
14      小売
15      銀行
16      金融（除く銀行）
17      不動産
99      その他
'''

class IndustryCode17Schema:

    # Create a table to store the industry codes
    create_table_query = """
    CREATE TABLE industry_codes17 (
        code INTEGER NOT NULL PRIMARY KEY,
        name VARCHAR(30) NOT NULL
    );
    """

    # Insert industry codes into the table
    industry_codes17 = [
        (1, '食品'),
        (2, 'エネルギー資源'),
        (3, '建設・資材'),
        (4, '素材・化学'),
        (5, '医薬品'),
        (6, '自動車・輸送機'),
        (7, '鉄鋼・非鉄'),
        (8, '機械'),
        (9, '電機・精密'),
        (10, '情報通信・サービスその他'),
        (11, '電気・ガス'),
        (12, '運輸・物流'),
        (13, '商社・卸売'),
        (14, '小売'),
        (15, '銀行'),
        (16, '金融（除く銀行）'),
        (17, '不動産'),
        (99, 'その他')
    ]

    insert_query = """
        INSERT INTO
        industry_codes17 (
            code, name
        ) VALUES (
            %s, %s
        );
        """

    DB = None

    def __init__(self, DB):
        self.DB = DB

    def create_table(self):
        print('Creating table industry_codes17')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()

    def insert_industry_codes(self):
        print('Inserting industry codes')
        try:
            self.DB.execute(self.insert_query, self.industry_codes17)
        except Exception as e:
            print(e)
            exit()





