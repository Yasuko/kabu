import lib.pgsql as pgsql

'''
市場区分コード及び市場区分名

https://jpx.gitbook.io/j-quants-ja/api-reference/listed_info/marketcode

コード	名称
0101	東証一部
0102	東証二部
0104	マザーズ
0105	TOKYO PRO MARKET
0106	JASDAQ スタンダード
0107	JASDAQ グロース
0109	その他
0111	プライム
0112	スタンダード
0113	ロース
'''

class Market:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    def insert (self, code, name):
        insert_query = """
        INSERT INTO market (code, name)
        VALUES (%s, %s);
        """
        pgsql.execute(insert_query, (code, name))

    def select (self, id):
        select_query = "SELECT * FROM market WHERE id = %s;"
        return pgsql.fetch_one(select_query, (id,))

    def update (self, id, code, name):
        update_query = """
        UPDATE market
        SET code = %s, name = %s
        WHERE id = %s;
        """
        pgsql.execute(update_query, (code, name, id))

    def delete (self, id):
        delete_query = "DELETE FROM market WHERE id = %s;"
        pgsql.execute(delete_query, (id,))
