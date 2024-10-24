import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisDate import AnalysisDate

from lib.explain import press_converter
from lib.trend_pattern_base import (
    detect_bullish_engulfing, 
    detect_bearish_engulfing, 
    detect_bullish_harami, 
    detect_bearish_harami,
    is_dark_cloud_cover,
    detect_piercing_pattern,
    detect_harami_pattern,
    detect_in_neck_pattern,
    detect_on_neck_pattern,
    detect_meeting_lines_pattern,
    detect_bearish_meeting_lines_pattern,
    detect_separating_lines_pattern,
    detect_bearish_separating_lines_pattern,
    detect_tasukigap_pattern,
    detect_bearish_tasukigap_pattern,
    detect_tweezer_top_pattern,
    detect_tweezer_bottom_pattern
)

from lib.utils import aggregate_stock_data


'''
株価情報からローソクの種別を判定し
トレンドパターンとの一致度をスコアリングする
'''

def trend_pattern_analysis(prices1, prices2):
    score = 0
    trendos = []
    scores = []

    # 陽の包み線を検出
    if detect_bullish_engulfing(prices1, prices2):
        score += 2
        trendos.append('陽の包み線')
        scores.append(2)
    # 陰の包み線を検出
    if detect_bearish_engulfing(prices1, prices2):
        score -= 2
        trendos.append('陰の包み線')
        scores.append(-2)
    # 陽のハラミを検出
    if detect_bullish_harami(prices1, prices2):
        score -= 2
        trendos.append('陽のハラミ')
        scores.append(-2)
    # 陰のハラミを検出
    if detect_bearish_harami(prices1, prices2):
        score += 2
        trendos.append('陰のハラミ')
        scores.append(2)
    # かぶせ線を検出
    if is_dark_cloud_cover(prices1, prices2):
        score -= 4
        trendos.append('かぶせ線')
        scores.append(-4)
    # 切り込み線を検出
    if detect_piercing_pattern(prices1, prices2):
        score += 2
        trendos.append('切り込み線')
        scores.append(2)
    # 差し込み線を検出
    if detect_harami_pattern(prices1, prices2):
        score -= 2
        trendos.append('差し込み線')
        scores.append(-2)
    # 入り首を検出
    if detect_in_neck_pattern(prices1, prices2):
        score += 1
        trendos.append('入り首')
        scores.append(1)
    # あて首線を検出
    if detect_on_neck_pattern(prices1, prices2):
        score -= 4
        trendos.append('あて首線')
        scores.append(-4)
    # 出会い線陽を検出
    if detect_meeting_lines_pattern(prices1, prices2):
        score -= 1
        trendos.append('出会い線陽')
        scores.append(-1)
    # 出会い線陰を検出
    if detect_bearish_meeting_lines_pattern(prices1, prices2):
        score += 1
        trendos.append('出会い線陰')
        scores.append(1)
    # 振り分け線陽を検出
    if detect_separating_lines_pattern(prices1, prices2):
        score += 1
        trendos.append('振り分け線陽')
        scores.append(1)
    # 振り分け線陰を検出
    if detect_bearish_separating_lines_pattern(prices1, prices2):
        score -= 1
        trendos.append('振り分け線陰')
        scores.append(-1)
    # たすき線陽を検出
    if detect_tasukigap_pattern(prices1, prices2):
        score -= 1
        trendos.append('たすき陽')
        scores.append(-1)
    # たすき線陰を検出
    if detect_bearish_tasukigap_pattern(prices1, prices2):
        score += 1
        trendos.append('たすき陰')
        scores.append(1)
    # 毛抜き天井を検出
    if detect_tweezer_top_pattern(prices1, prices2):
        score -= 1
        trendos.append('毛抜き天井')
        scores.append(-1)
    # 毛抜き底を検出
    if detect_tweezer_bottom_pattern(prices1, prices2):
        score += 1
        trendos.append('毛抜き底')
        scores.append(1)
    
    return score, trendos, scores



company_codes = Industry().get_all_records()
day = datetime.datetime.now()
#day = day - datetime.timedelta(days=4)

db = Industry().DB
#print(date_map)

ranks = []

for row in company_codes:
    print('Getting data for : ' + row[1])
    
    candles = press_converter(row[1], day, db)

    score = 0
    trendos = []
    scores = []

    # candles要素の数をカウント
    print('Candle count : ', len(candles))
    for index in range(18):
        #print('Candle : ', candles[index])

        s, t, ss = trend_pattern_analysis(candles[index]['price'], candles[index + 1]['price'])
        score += s
        trendos.extend(t)
        scores.extend(ss)

    print('Score :', score)
    print('Trendos :', trendos)
    print('Scores :', scores)

    # ranks内の
    ranks.append([row[1], score])
    #time.sleep(0.3)

ranks.sort(key=lambda x: x[1], reverse=True)
print(ranks)
def score_ranking(ranks):
    # スコアを降順にソート
    ranks.sort(key=lambda x: x[1], reverse=True)
    return ranks

