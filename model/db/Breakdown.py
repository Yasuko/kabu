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

class Breakdown:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    # データを追加する関数
    def add(self, data):
        insert_query = """
        INSERT INTO breakdown (
            industry_id, Date, Code, LongSellValue,
            ShortSellWithoutMarginValue, MarginSellNewValue,
            MarginSellCloseValue, LongBuyValue, MarginBuyNewValue,
            MarginBuyCloseValue, LongSellVolume,
            ShortSellWithoutMarginVolume, MarginSellNewVolume,
            MarginSellCloseVolume, LongBuyVolume, MarginBuyNewVolume,
            MarginBuyCloseVolume
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
        """
        try:
            pgsql.execute(insert_query, (data,))
            print("Breakdown added successfully")
        except Exception as e:
            print(f"Error adding breakdown: {e}")

    # データを更新する関数
    def update(self, id, data):
        update_query = """
        UPDATE breakdown
        SET industry_id = %s, Date = %s, Code = %s, LongSellValue = %s, ShortSellWithoutMarginValue = %s, MarginSellNewValue = %s, MarginSellCloseValue = %s, LongBuyValue = %s, MarginBuyNewValue = %s, MarginBuyCloseValue = %s, LongSellVolume = %s, ShortSellWithoutMarginVolume = %s, MarginSellNewVolume = %s, MarginSellCloseVolume = %s, LongBuyVolume = %s, MarginBuyNewVolume = %s, MarginBuyCloseVolume = %s
        WHERE id = %s;
        """
        try:
            pgsql.execute(update_query, (*data, id))
            print("Breakdown updated successfully")
        except Exception as e:
            print(f"Error updating breakdown: {e}")

    # データを削除する関数
    def delete(self, id):
        delete_query = "DELETE FROM breakdown WHERE id = %s;"
        try:
            pgsql.execute(delete_query, (id, ))
            print("Breakdown deleted successfully")
        except Exception as e:
            print(f"Error deleting breakdown: {e}")

    # IDでデータを検索する関数
    def search_by_id(self, id):
        search_query = "SELECT * FROM breakdown WHERE id = %s;"
        try:
            result = pgsql.fetch_one(search_query, (id, ))
            return result
        except Exception as e:
            print(f"Error searching breakdown by ID: {e}")

    # industry_idの重複を排除しつつ、industry_idで検索する関数
    def search_unique_industry_id(self, industry_id):
        search_query = """
        SELECT DISTINCT ON (industry_id) * FROM breakdown
        WHERE industry_id = %s;
        """
        try:
            result = pgsql.fetch_all(search_query, (industry_id,))
            return result
        except Exception as e:
            print(f"Error searching unique industry_id: {e}")

    # industry_idの重複を排除しつつ、Dateで検索する関数
    def search_unique_industry_id_by_date(self, date):
        search_query = """
        SELECT DISTINCT ON (industry_id) * FROM breakdown
        WHERE Date = %s;
        """
        try:
            result = pgsql.fetch_all(search_query, (date,))
            return result
        except Exception as e:
            print(f"Error searching unique industry_id by date: {e}")

    # industry_idの重複を排除しつつ、Codeで検索する関数
    def search_unique_industry_id_by_code(self, code):
        search_query = """
        SELECT DISTINCT ON (industry_id) * FROM breakdown
        WHERE Code = %s;
        """
        try:
            result = pgsql.fetch_all(search_query, (code,))
            return result
        except Exception as e:
            print(f"Error searching unique industry_id by code: {e}")







"""
Sample Doc

https://jpx.gitbook.io/j-quants-ja/api-reference/breakdown

Date 売買日 String YYYY-MM-DD
Code 銘柄コード String
LongSellValue 実売りの約定代金 Number 売りの約定代金の内訳
ShortSellWithoutMarginValue 空売り(信用新規売りを除く)の約定代金 Number 同上
MarginSellNewValue 信用新規売り(新たな信用売りポジションを作るための売り注文)の約定代金 Number 同上
MarginSellCloseValue  信用返済売り(既存の信用買いポジションを閉じるための売り注文)の約定代金 Number 同上
LongBuyValue 現物買いの約定代金 Number 買いの約定代金の内訳
MarginBuyNewValue 信用新規買い(新たな信用買いポジションを作るための買い注文)の約定代金 Number 同上
MarginBuyCloseValue 信用返済買い(既存の信用売りポジションを閉じるための買い注文)の約定代金 Number 同上
LongSellVolume 実売りの約定株数 Number 売りの約定株数の内訳
ShortSellWithoutMarginVolume 空売り(信用新規売りを除く)の約定株数 Number 同上
MarginSellNewVolume 信用新規売り(新たな信用売りポジションを作るための売り注文)の約定株数 Number 同上
MarginSellCloseVolume 信用返済売り(既存の信用買いポジションを閉じるための売り注文)の約定株数 Number 同上
LongBuyVolume 現物買いの約定株数 Number 買いの約定株数の内訳
MarginBuyNewVolume 信用新規買い(新たな信用買いポジションを作るための買い注文)の約定株数 Number 同上
MarginBuyCloseVolume  信用返済買い(既存の信用売りポジションを閉じるための買い注文)の約定株数 Number 上　


"""