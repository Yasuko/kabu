"""
 株価データ breakdown

"""

class HistoryMonth:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    # データの追加
    def add_data(self, industry_id, date, open, high, low, close, volume, dividends, stock_splits):
        self.cursor.execute("""
            INSERT INTO history_month (industry_id, Date, Open, High, Low, Close, Volume, Dividends, StockSplits)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (industry_id, date, open, high, low, close, volume, dividends, stock_splits))

    # データの更新
    def update_data(self, id, industry_id, date, open, high, low, close, volume, dividends, stock_splits):
        self.cursor.execute("""
            UPDATE history_month
            SET industry_id = %s, Date = %s, Open = %s, High = %s, Low = %s, Close = %s, Volume = %s, Dividends = %s, StockSplits = %s
            WHERE id = %s
        """, (industry_id, date, open, high, low, close, volume, dividends, stock_splits, id))

    # データの削除
    def delete_data(self, id):
        return self.cursor.execute("DELETE FROM history_month WHERE id = %s", (id,))

    # Dateに重複がない場合のみ、データの追加
    def add_data_if_not_exists(self, industry_id, date, open, high, low, close, volume, dividends, stock_splits):
        if self.cursor.execute("SELECT COUNT(*) FROM history_month WHERE Date = %s", (date,)) == 0:
            self.add_data(industry_id, date, open, high, low, close, volume, dividends, stock_splits)
            return True
        return None

    # idからデータを抜き出し
    def get_data_by_id(self, id):
        return self.cursor.fetchone("SELECT * FROM history_month WHERE id = %s", (id,))

    # Dateで絞り込み、industry_idからデータを抜き出し
    def get_data_by_date_and_industry_id(self, date, industry_id):
        return self.cursor.fetchall("SELECT * FROM history_month WHERE Date = %s AND industry_id = %s", (date, industry_id))

    # Dateで絞り込んだデータを抜き出し
    def get_data_by_date(self, date):
        return self.cursor.fetchall("SELECT * FROM history_month WHERE Date = %s", (date,))



