
import lib.pgsql as pgsql

'''
33業種コード及び業種名

https://jpx.gitbook.io/j-quants-ja/api-reference/listed_info/sector33code

コード	名称
0050	水産・農林業
1050	鉱業
2050	建設業
3050	食料品
3100	繊維製品
3150	パルプ・紙
3200	化学
3250	医薬品
3300	石油･石炭製品
3350	ゴム製品
3400	ガラス･土石製品
3450	鉄鋼
3500	非鉄金属
3550	金属製品
3600	機械
3650	電気機器
3700	輸送用機器
3750	精密機器
3800	その他製品
4050	電気･ガス業
5050	陸運業
5100	海運業
5150	空運業
5200	倉庫･運輸関連業
5250	情報･通信業
6050	卸売業
6100	小売業
7050	銀行業
7100	証券･商品先物取引業
7150	保険業
7200	その他金融業
8050	不動産業
9050	サービス業
9999	その他
'''

class IndustryCode33:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    def insert (self, code, name):
        insert_query = "INSERT INTO industry_codes33 (code, name) VALUES (%s, %s);"
        pgsql.execute(insert_query, (code, name))

    def select (self, code):
        select_query = "SELECT * FROM industry_codes33 WHERE code = %s;"
        return pgsql.fetch_one(select_query, (code,))
    
    def update (self, code, name):
        update_query = "UPDATE industry_codes33 SET name = %s WHERE code = %s;"
        pgsql.execute(update_query, (name, code))

    def delete (self, code):
        delete_query = "DELETE FROM industry_codes33 WHERE code = %s;"
        pgsql.execute(delete_query, (code,))



