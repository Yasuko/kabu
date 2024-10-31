import os
import numpy as np
import pandas as pd
import time

from model.db.Enterprise import Enterprise

Enterprise().get_all_records()
db = Enterprise().DB


if not os.path.isfile('data_j.csv'):
    print(f"{os.getcwd()}\n file not found")
    exit()

df_data_j = pd.read_csv('data_j.csv', index_col=None)
df_data_j = df_data_j[~df_data_j['市場・商品区分'].isin(['REIT・ベンチャーファンド・カントリーファンド・インフラファンド', 'ETF・ETN'])]
df_data_j = df_data_j[df_data_j['コード'] != 25935]

total_codes = len(df_data_j['コード'])
start_index, end_index = 0, int(np.ceil(total_codes * 1))

for ticker in df_data_j['コード'][start_index:end_index]:
    try:
        print(ticker)

        r = Enterprise(db).add_exists_by_company_code(
            ticker,
            {
                'companyCode': ticker,
                'stockName': df_data_j[df_data_j['コード'] == ticker]['銘柄名'].values[0],
                'marketProductCategory': df_data_j[df_data_j['コード'] == ticker]['市場・商品区分'].values[0],
                'industryCode33': df_data_j[df_data_j['コード'] == ticker]['33業種コード'].values[0],
                'industryCategory33': df_data_j[df_data_j['コード'] == ticker]['33業種区分'].values[0],
                'industryCode17': df_data_j[df_data_j['コード'] == ticker]['17業種コード'].values[0],
                'industryCategory17': df_data_j[df_data_j['コード'] == ticker]['17業種区分'].values[0],
                'scaleCode': df_data_j[df_data_j['コード'] == ticker]['規模コード'].values[0],
                'scaleCategory': df_data_j[df_data_j['コード'] == ticker]['規模区分'].values[0],
            }
        )
        print(f'Result : {ticker} : ' , r)
    except Exception as e:
        print(f'証券コード {ticker} のデータ取得中にエラーが発生しました: {e}')
    
    #time.sleep(5)
