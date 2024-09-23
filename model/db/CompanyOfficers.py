'''
役員情報 (company_officers) テーブルのスキーマを定義するモジュール

CREATE TABLE IF NOT EXISTS company_officers (
    id SERIAL PRIMARY KEY,
    max_age INTEGER,
    name VARCHAR(255),
    age INTEGER,
    title VARCHAR(255),
    year_born INTEGER,
    fiscal_year INTEGER,
    total_pay BIGINT,
    exercised_value BIGINT,
    unexercised_value BIGINT
);

'''

class CompanyOfficers:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS company_officers (
    id SERIAL PRIMARY KEY,
    max_age INTEGER,
    name VARCHAR(255),
    age INTEGER,
    title VARCHAR(255),
    year_born INTEGER,
    fiscal_year INTEGER,
    total_pay BIGINT,
    exercised_value BIGINT,
    unexercised_value BIGINT
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