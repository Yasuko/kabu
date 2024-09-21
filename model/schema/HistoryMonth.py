"""
 株価データ breakdown

"""

class BreakdownSchema:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS history_week (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        industry_id UUID NOT NULL REFERENCES industry(id),
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
        print('Creating table breakdown')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()
