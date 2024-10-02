import lib.pgsql as pgsql

"""
IDトークン取得 auth_refresh

id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
refreshtoken VARCHAR(255) NOT NULL,
createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""

class AuthUser:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    # データを追加する関数
    def add(self, refreshtoken: str):
        insert_query = """
        INSERT INTO auth_user (refreshtoken)
        VALUES (%s);
        """
        try:
            pgsql.execute(insert_query, (refreshtoken,))
            print("AuthUser added successfully")
        except Exception as e:
            print(f"Error adding AuthUser: {e}")

    # データを更新する関数
    def update(self, id, refreshtoken: str):
        update_query = """
        UPDATE auth_user
        SET
            refreshtoken = %s,
        WHERE id = %s;
        """
        try:
            pgsql.execute(update_query, (refreshtoken, id))
            print("AuthUser updated successfully")
        except Exception as e:
            print(f"Error updating AuthUser: {e}")

    # データを削除する関数
    def delete(self, id):
        delete_query = "DELETE FROM auth_user WHERE id = %s;"
        try:
            pgsql.execute(delete_query, (id, ))
            print("AuthUser deleted successfully")
        except Exception as e:
            print(f"Error deleting AuthUser: {e}")

    # データを全件取得し、作成日時の降順で返す関数
    def fetch_sort_by_created(self):
        select_query = "SELECT * FROM auth_user ORDER BY createdAt DESC;"
        try:
            result = pgsql.fetch(select_query, (id, ))
            return result
        except Exception as e:
            print(f"Error fetching AuthUser: {e}")
            return None


    # 作成日時が1週間以上前のデータを削除する関数
    def delete_old_data(self):
        delete_query = "DELETE FROM auth_refresh WHERE createdAt < NOW() - INTERVAL '1 week';"
        try:
            pgsql.execute(delete_query)
            print("Old AuthRefresh data deleted successfully")
        except Exception as e:
            print(f"Error deleting old AuthRefresh data: {e}")




"""
Sample Doc

https://jpx.gitbook.io/j-quants-ja/api-reference/idtoken



"""