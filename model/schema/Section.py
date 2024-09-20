"""
市場名を管理するテーブル

市場一部        : TSE1st
市場二部        : TSE2nd
マザーズ        : TSEMothers
JASDAQ          : TSEJASDAQ
プライム        : TSEPrime
スタンダード    : TSEStandard
グロース        : TSEGrowth
東証および名証  : TokyoNagoya

CREATE TABLE IF NOT EXISTS section (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    code VARCHAR(20) NOT NULL
);
"""

class SectionSchema:
    # テーブル作成クエリ
    create_table_query = """
    CREATE TABLE IF NOT EXISTS section (
        id SERIAL PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        code VARCHAR(20) NOT NULL
    );
    """

    # マスターデータ
    section_data = [
        ("001", "市場一部", "TSE1st"),
        ("002", "市場二部", "TSE2nd"),
        ("003", "マザーズ", "TSEMothers"),
        ("004", "JASDAQ", "TSEJASDAQ"),
        ("005", "プライム", "TSEPrime"),
        ("006", "スタンダード", "TSEStandard"),
        ("007", "グロース", "TSEGrowth"),
        ("008", "東証および名証", "TokyoNagoya")
    ]

    # データ挿入クエリ
    insert_query = """
    INSERT INTO section (id, name, code) VALUES (%s, %s, %s);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table section')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
    
    def insert_section_data(self):
        print('Inserting section data')
        try:
            self.DB.execute(self.insert_query, self.section_data)
        except Exception as e:
            print(e)
            exit()