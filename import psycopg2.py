import psycopg2
from psycopg2 import sql

# データベース接続設定
db_config = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

# データを追加する関数
def add_breakdown(data):
    insert_query = """
    INSERT INTO breakdown (industry_id, Date, Code, LongSellValue, ShortSellWithoutMarginValue, MarginSellNewValue, MarginSellCloseValue, LongBuyValue, MarginBuyNewValue, MarginBuyCloseValue, LongSellVolume, ShortSellWithoutMarginVolume, MarginSellNewVolume, MarginSellCloseVolume, LongBuyVolume, MarginBuyNewVolume, MarginBuyCloseVolume)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(insert_query, data)
        conn.commit()
        cur.close()
        conn.close()
        print("Breakdown added successfully")
    except Exception as e:
        print(f"Error adding breakdown: {e}")

# データを更新する関数
def update_breakdown(id, data):
    update_query = """
    UPDATE breakdown
    SET industry_id = %s, Date = %s, Code = %s, LongSellValue = %s, ShortSellWithoutMarginValue = %s, MarginSellNewValue = %s, MarginSellCloseValue = %s, LongBuyValue = %s, MarginBuyNewValue = %s, MarginBuyCloseValue = %s, LongSellVolume = %s, ShortSellWithoutMarginVolume = %s, MarginSellNewVolume = %s, MarginSellCloseVolume = %s, LongBuyVolume = %s, MarginBuyNewVolume = %s, MarginBuyCloseVolume = %s
    WHERE id = %s;
    """
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(update_query, (*data, id))
        conn.commit()
        cur.close()
        conn.close()
        print("Breakdown updated successfully")
    except Exception as e:
        print(f"Error updating breakdown: {e}")

# データを削除する関数
def delete_breakdown(id):
    delete_query = "DELETE FROM breakdown WHERE id = %s;"
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(delete_query, (id,))
        conn.commit()
        cur.close()
        conn.close()
        print("Breakdown deleted successfully")
    except Exception as e:
        print(f"Error deleting breakdown: {e}")

# IDでデータを検索する関数
def search_breakdown_by_id(id):
    search_query = "SELECT * FROM breakdown WHERE id = %s;"
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(search_query, (id,))
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        print(f"Error searching breakdown by ID: {e}")

# industry_idの重複を排除しつつ、industry_idで検索する関数
def search_unique_industry_id(industry_id):
    search_query = """
    SELECT DISTINCT ON (industry_id) * FROM breakdown
    WHERE industry_id = %s;
    """
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(search_query, (industry_id,))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        print(f"Error searching unique industry_id: {e}")

# industry_idの重複を排除しつつ、Dateで検索する関数
def search_unique_industry_id_by_date(date):
    search_query = """
    SELECT DISTINCT ON (industry_id) * FROM breakdown
    WHERE Date = %s;
    """
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(search_query, (date,))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        print(f"Error searching unique industry_id by date: {e}")

# 使用例
data = (
    'your_industry_id', '2023-10-01', '1234', 1000.0, 500.0, 200.0, 100.0, 1500.0, 300.0, 200.0, 1000.0, 500.0, 200.0, 100.0, 1500.0, 300.0, 200.0
)
add_breakdown(data)

update_breakdown('your_uuid', data)

delete_breakdown('your_uuid')

print(search_breakdown_by_id('your_uuid'))

print(search_unique_industry_id('your_industry_id'))

print(search_unique_industry_id_by_date('2023-10-01'))