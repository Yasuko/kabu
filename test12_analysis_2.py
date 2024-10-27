import datetime
import time
from model.db.Industry import Industry
from model.db.AnalysisCandle import AnalysisCandle

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

'''
株価情報からローソクの種別を判定し
トレンドパターンとの一致度をスコアリングする
'''

def trend_pattern_analysis(prices1, prices2):
    up = 0
    down = 0
    score = 0
    trendos = []

    # 陽の包み線を検出
    if detect_bullish_engulfing(prices1, prices2):
        score += 2
        up += 1
        trendos.append('陽の包み線')
    # 陰の包み線を検出
    if detect_bearish_engulfing(prices1, prices2):
        score -= 2
        down += 1
        trendos.append('陰の包み線')
    # 陽のハラミを検出
    if detect_bullish_harami(prices1, prices2):
        score -= 2
        down += 1
        trendos.append('陽のハラミ')
    # 陰のハラミを検出
    if detect_bearish_harami(prices1, prices2):
        score += 2
        up += 1
        trendos.append('陰のハラミ')
    # かぶせ線を検出
    if is_dark_cloud_cover(prices1, prices2):
        score -= 4
        down += 1
        trendos.append('かぶせ線')
    # 切り込み線を検出
    if detect_piercing_pattern(prices1, prices2):
        score += 2
        up += 1
        trendos.append('切り込み線')
    # 差し込み線を検出
    if detect_harami_pattern(prices1, prices2):
        score -= 2
        down += 1
        trendos.append('差し込み線')
    # 入り首を検出
    if detect_in_neck_pattern(prices1, prices2):
        score += 1
        up += 1
        trendos.append('入り首')
    # あて首線を検出
    if detect_on_neck_pattern(prices1, prices2):
        score -= 4
        down += 1
        trendos.append('あて首線')
    # 出会い線陽を検出
    if detect_meeting_lines_pattern(prices1, prices2):
        score -= 1
        down += 1
        trendos.append('出会い線陽')
    # 出会い線陰を検出
    if detect_bearish_meeting_lines_pattern(prices1, prices2):
        score += 1
        up += 1
        trendos.append('出会い線陰')
    # 振り分け線陽を検出
    if detect_separating_lines_pattern(prices1, prices2):
        score += 1
        up += 1
        trendos.append('振り分け線陽')
    # 振り分け線陰を検出
    if detect_bearish_separating_lines_pattern(prices1, prices2):
        score -= 1
        down += 1
        trendos.append('振り分け線陰')
    # たすき線陽を検出
    if detect_tasukigap_pattern(prices1, prices2):
        score -= 1
        down += 1
        trendos.append('たすき陽')
    # たすき線陰を検出
    if detect_bearish_tasukigap_pattern(prices1, prices2):
        score += 1
        up += 1
        trendos.append('たすき陰')
    # 毛抜き天井を検出
    if detect_tweezer_top_pattern(prices1, prices2):
        score -= 1
        down += 1
        trendos.append('毛抜き天井')
    # 毛抜き底を検出
    if detect_tweezer_bottom_pattern(prices1, prices2):
        score += 1
        up += 1
        trendos.append('毛抜き底')
    
    return up, down, score, trendos



company_codes = Industry().get_all_records()
day = datetime.datetime.now()
#day = day - datetime.timedelta(days=4)

db = Industry().DB
#print(date_map)

ScoreColumns = ['DayScore', 'DayOneScore', 'DayTwoScore', 'DayThreeScore', 'WeekOneScore']
UpColumns = ['DayUp', 'DayOneUp', 'DayTwoUp', 'DayThreeUp', 'WeekOneUp']
DownColumns = ['DayDown', 'DayOneDown', 'DayTwoDown', 'DayThreeDown', 'WeekOneDown']
TrendsColumns = ['DayTrends', 'DayOneTrends', 'DayTwoTrends', 'DayThreeTrends', 'WeekOneTrends']

for row in company_codes:
    print('Getting data for : ' + row[1])
    try:    
        candle = press_converter(row[1], day, db)
        scores_dict = {}

        for i, c in enumerate(candle):
            # candles要素の数をカウント
            # print('Candle count : ', len(c))

            score = 0
            up = 0
            down = 0
            trendos = []

            for index in range(9):
                u, d, s, t = trend_pattern_analysis(c[index]['price'], c[index + 1]['price'])
                
                up += u
                down += d
                score += s
                trendos.extend(t)

            # 集計結果を辞書形式で格納
            scores_dict[UpColumns[i]] = up
            scores_dict[DownColumns[i]] = down
            scores_dict[ScoreColumns[i]] = score
            scores_dict[TrendsColumns[i]] = trendos
            
            print('Score :', score)
            #print('Trendos :', trendos)
            #print('Scores :', scores)
            #print('Scores Dict :', scores_dict)
            #time.sleep(0.3)

        # time.sleep(0.3)
        scores_dict['companyCode'] = row[1]
        scores_dict['Date'] = day.strftime('%Y-%m-%d')
        #(AnalysisCandle(db)
        #    .add_exists_by_date_and_company_code(day.strftime('%Y-%m-%d'), row[1], scores_dict))
    except Exception as e:
        print(candle)
        print(e)
        
        
    

