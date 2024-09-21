import lib.pgsql as pgsql

"""
 売買内訳データ breakdown


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
MarginBuyCloseVolume NUMERIC
createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP

"""

class HistoryDate:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    # データの追加
    def add_data(self, industry_id, date, open, high, low, close, volume, dividends, stock_splits):
        cursor.execute("""
            INSERT INTO history_date (industry_id, Date, Open, High, Low, Close, Volume, Dividends, StockSplits)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (industry_id, date, open, high, low, close, volume, dividends, stock_splits))
        conn.commit()

    # データの更新
    def update_data(id, industry_id, date, open, high, low, close, volume, dividends, stock_splits):
        cursor.execute("""
            UPDATE history_date
            SET industry_id = %s, Date = %s, Open = %s, High = %s, Low = %s, Close = %s, Volume = %s, Dividends = %s, StockSplits = %s
            WHERE id = %s
        """, (industry_id, date, open, high, low, close, volume, dividends, stock_splits, id))
        conn.commit()

    # データの削除
    def delete_data(id):
        cursor.execute("DELETE FROM history_date WHERE id = %s", (id,))
        conn.commit()

    # Dateに重複がない場合のみ、データの追加
    def add_data_if_not_exists(industry_id, date, open, high, low, close, volume, dividends, stock_splits):
        cursor.execute("SELECT COUNT(*) FROM history_date WHERE Date = %s", (date,))
        if cursor.fetchone()[0] == 0:
            add_data(industry_id, date, open, high, low, close, volume, dividends, stock_splits)

    # idからデータを抜き出し
    def get_data_by_id(id):
        cursor.execute("SELECT * FROM history_date WHERE id = %s", (id,))
        return cursor.fetchone()

    # Dateで絞り込み、industry_idからデータを抜き出し
    def get_data_by_date_and_industry_id(date, industry_id):
        cursor.execute("SELECT * FROM history_date WHERE Date = %s AND industry_id = %s", (date, industry_id))
        return cursor.fetchall()

    # Dateで絞り込んだデータを抜き出し
    def get_data_by_date(date):
        cursor.execute("SELECT * FROM history_date WHERE Date = %s", (date,))
        return cursor.fetchall()




