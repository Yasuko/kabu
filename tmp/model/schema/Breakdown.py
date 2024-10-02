"""
 売買内訳データ breakdown

"""

class BreakdownSchema:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS breakdown (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        industry_id UUID NOT NULL REFERENCES industry(id),
        Date DATE,
        Code VARCHAR(10),
        LongSellValue NUMERIC,
        ShortSellWithoutMarginValue NUMERIC,
        MarginSellNewValue NUMERIC,
        MarginSellCloseValue NUMERIC,
        LongBuyValue NUMERIC,
        MarginBuyNewValue NUMERIC,
        MarginBuyCloseValue NUMERIC,
        LongSellVolume NUMERIC,
        ShortSellWithoutMarginVolume NUMERIC,
        MarginSellNewVolume NUMERIC,
        MarginSellCloseVolume NUMERIC,
        LongBuyVolume NUMERIC,
        MarginBuyNewVolume NUMERIC,
        MarginBuyCloseVolume NUMERIC,
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
