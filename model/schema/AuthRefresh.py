import lib.pgsql as pgsql

"""
IDトークン取得 auth_refresh

id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
idToken VARCHAR(255) NOT NULL,
createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""

class OptionsType:
    refreshtoken: str = ""
    idToken: str = ""

class AuthRefresh:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    # データを追加する関数
    def add(self, idToken: str):
        insert_query = """
        INSERT INTO auth_refresh (idToken)
        VALUES (%s);
        """
        try:
            pgsql.execute(insert_query, (idToken,))
            print("AuthRefresh added successfully")
        except Exception as e:
            print(f"Error adding AuthRefresh: {e}")

    # データを更新する関数
    def update(self, id, data: OptionsType):
        update_query = """
        UPDATE auth_refresh
        SET
            refreshtoken = %s,
             idToken = %s
        WHERE id = %s;
        """
        try:
            pgsql.execute(update_query, (*data, id))
            print("AuthRefresh updated successfully")
        except Exception as e:
            print(f"Error updating AuthRefresh: {e}")

    # データを削除する関数
    def delete(self, id):
        delete_query = "DELETE FROM auth_refresh WHERE id = %s;"
        try:
            pgsql.execute(delete_query, (id, ))
            print("AuthRefresh deleted successfully")
        except Exception as e:
            print(f"Error deleting AuthRefresh: {e}")

    # データを全件取得し、作成日時の降順で返す関数
    def fetch_sort_by_created(self):
        select_query = "SELECT * FROM auth_refresh ORDER BY createdAt DESC;"
        try:
            result = pgsql.fetch(select_query, (id, ))
            return result
        except Exception as e:
            print(f"Error fetching AuthRefresh: {e}")
            return None


    # 作成日時が23時間以上前のデータを削除する関数
    def delete_old_data(self):
        delete_query = "DELETE FROM auth_refresh WHERE createdAt < NOW() - INTERVAL '23 hours';"
        try:
            pgsql.execute(delete_query)
            print("Old AuthRefresh data deleted successfully")
        except Exception as e:
            print(f"Error deleting AuthRefresh: {e}")




"""
Sample Doc

https://jpx.gitbook.io/j-quants-ja/api-reference/idtoken



"""