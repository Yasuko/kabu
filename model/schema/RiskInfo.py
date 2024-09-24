'''
リスク情報 (RiskInfo) テーブルのスキーマを定義する

CREATE TABLE IF NOT EXISTS risk_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(7),
    audit_risk INTEGER,
    board_risk INTEGER,
    compensation_risk INTEGER,
    shareholder_rights_risk INTEGER,
    overall_risk INTEGER,
    governance_epoch_date BIGINT,
    compensation_as_of_epoch_date BIGINT,
    max_age INTEGER,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON industry (company_code);
'''

class RiskInfo:
    # テーブル作成クエリ
    create_table_query = """
CREATE TABLE IF NOT EXISTS risk_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_code VARCHAR(7),
    audit_risk INTEGER,
    board_risk INTEGER,
    compensation_risk INTEGER,
    shareholder_rights_risk INTEGER,
    overall_risk INTEGER,
    governance_epoch_date BIGINT,
    compensation_as_of_epoch_date BIGINT,
    max_age INTEGER,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON risk_info (company_code);
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table risk info')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()