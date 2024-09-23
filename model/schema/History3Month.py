"""
3ヶ月 株価データ breakdown

"""

class History3Month:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS history_3month (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        company_code VARCHAR(7) NOT NULL REFERENCES industry(company_code),
        Date DATE NOT NULL,
        Open NUMERIC NOT NULL,
        High NUMERIC NOT NULL,
        Low NUMERIC NOT NULL,
        Close NUMERIC NOT NULL,
        Volume NUMERIC NOT NULL,
        Dividends NUMERIC NOT NULL,
        StockSplits NUMERIC NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    DB = None

    def __init__(self, DB):
        self.DB = DB
    
    def create_table(self):
        print('Creating table history_3month')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
