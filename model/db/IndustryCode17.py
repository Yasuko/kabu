
import lib.pgsql as pgsql

'''
17業種コード及び業種名

https://jpx.gitbook.io/j-quants-ja/api-reference/listed_info/sector17code

コード	名称
1       食品
2       エネルギー資源
3       建設・資材
4       素材・化学
5       医薬品
6       自動車・輸送機
7       鉄鋼・非鉄
8       機械
9       電機・精密
10      情報通信・サービスその他
11      電気・ガス
12      運輸・物流
13      商社・卸売
14      小売
15      銀行
16      金融（除く銀行）
17      不動産
99      その他
'''


class IndustryCode17:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    def insert (self, code, name):
        insert_query = "INSERT INTO industry_codes17 (code, name) VALUES (%s, %s);"
        pgsql.execute(insert_query, (code, name))

    def select (self, code):
        select_query = "SELECT * FROM industry_codes17 WHERE code = %s;"
        return pgsql.fetch_one(select_query, (code,))
    
    def update (self, code, name):
        update_query = "UPDATE industry_codes17 SET name = %s WHERE code = %s;"
        pgsql.execute(update_query, (name, code))

    def delete (self, code):
        delete_query = "DELETE FROM industry_codes17 WHERE code = %s;"
        pgsql.execute(delete_query, (code,))

