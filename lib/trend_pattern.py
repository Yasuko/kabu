
'''
三兵のパターンを検出する
'''
def detect_three_soldiers(
    prices1,
    prices2,
    prices3
):
    patterns = []

    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']

    score = 0
    
    # 陽の三兵の条件
    if (day1['close'] > day1['open'] and
        day2['close'] > day2['open'] and
        day3['close'] > day3['open'] and
        day2['open'] > day1['open'] and
        day2['close'] > day1['close'] and
        day3['open'] > day2['open'] and
        day3['close'] > day2['close']):
        
        if prices1['candle']['key'] == 'srong_hummer_sun': score -= 3
        if prices2['candle']['key'] == 'srong_hummer_sun': score -= 3
    
    # 陰の三兵の条件
    if (day1['close'] < day1['open'] and
        day2['close'] < day2['open'] and
        day3['close'] < day3['open'] and
        day2['open'] < day1['open'] and
        day2['close'] < day1['close'] and
        day3['open'] < day2['open'] and
        day3['close'] < day2['close']):
        print('陰の三兵')
    
    return patterns

'''
三空のパターンを検出する
'''
def detect_three_gaps_ups(
    prices1,
    prices2,
    prices3
):
    patterns = []

    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']
    
    # 上昇三空の条件
    if (day2['Low'] > day1['High'] and
        day3['Low'] > day2['High']):
        print('上昇三空')
    
    return patterns

def detect_three_gaps_down(
    prices1,
    prices2,
    prices3
):
    patterns = []

    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']
    
    # 下降三空の条件
    if (day2['High'] < day1['Low'] and
        day3['High'] < day2['Low']):
        print('下降三空')
    
    return patterns

def detect_tweezers_bottom(
    prices1,
    prices2
) -> bool:
    prev_day = prices1['price']
    curr_day = prices2['price']
    
    # 「毛抜き底」パターンの条件をチェック
    if (abs(prev_day['low'] - curr_day['low']) < 1
        and curr_day['close'] > prev_day['close']):
        print('毛抜き底')
        return True
    
    return False

def detect_tweezers_top(
    prices1,
    prices2
) -> bool:
    prev_day = prices1['price']
    curr_day = prices2['price']
        
    # 「毛抜き天井」パターンの条件をチェック
    if (abs(prev_day['high'] - curr_day['high']) < 1
        and curr_day['close'] < prev_day['close']):
        print('毛抜き天井')
        return True
    
    return False


def detect_morning_star(
    prices1,
    prices2,
    prices3
) -> bool:
    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']
        
    # 「明けの明星」パターンの条件をチェック
    if (day1['close'] < day1['open'] and  # 1日目は陰線
        day2['open'] < day1['close'] and  # 2日目の始値が1日目の終値より低い
        abs(day2['close'] - day2['open']) < (day1['open'] - day1['close']) * 0.5 and  # 2日目は小陰線または小陽線
        day3['open'] > day2['close'] and  # 3日目の始値が2日目の終値より高い
        day3['close'] > day3['open']):  # 3日目は陽線
        return True
    
    return False


def detect_evening_star(
    prices1,
    prices2,
    prices3
) -> bool:
    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']
    
    # 「宵の明星」パターンの条件をチェック
    if (day1['close'] > day1['open'] and  # 1日目は陽線
        day2['open'] > day1['close'] and  # 2日目の始値が1日目の終値より高い
        abs(day2['close'] - day2['open']) < (day1['close'] - day1['open']) * 0.5 and  # 2日目は小陰線または小陽線
        day3['open'] < day2['close'] and  # 3日目の始値が2日目の終値より低い
        day3['close'] < day3['open']):  # 3日目は陰線
        return True
    
    return False


def detect_bullish_engulfing(
    prices1,
    prices2
) -> bool:
    day1 = prices1
    day2 = prices2
    
    # 「陽の包み線」パターンの条件をチェック
    if (day1['close'] < day1['open'] and  # 1日目は陰線
        day2['open'] < day1['close'] and  # 2日目の始値が1日目の終値より低い
        day2['close'] > day1['open'] and  # 2日目の終値が1日目の始値より高い
        day2['close'] > day2['open']):  # 2日目は陽線
        return True
    
    return False

def detect_bearish_engulfing(
    prices1,
    prices2
) -> bool:
    day1 = prices1
    day2 = prices2
    
    # 「陰の包み線」パターンの条件をチェック
    if (day1['close'] > day1['open'] and  # 1日目は陽線
        day2['open'] > day1['close'] and  # 2日目の始値が1日目の終値より高い
        day2['close'] < day1['open'] and  # 2日目の終値が1日目の始値より低い
        day2['close'] < day2['open']):  # 2日目は陰線
        return True
    
    return False


def detect_bullish_harami(
    prices1,
    prices2
) -> bool:
    day1 = prices1
    day2 = prices2
    
    # 「陽のはらみ線」パターンの条件をチェック
    if (day1['Close'] < day1['Open'] and  # 1日目は陰線
        day2['Open'] > day1['Close'] and  # 2日目の始値が1日目の終値より高い
        day2['Close'] < day1['Open'] and  # 2日目の終値が1日目の始値より低い
        day2['Close'] > day2['Open']):  # 2日目は陽線
        return True
    
    return False


def detect_bearish_harami(
    prices1,
    prices2
) -> bool:
    day1 = prices1
    day2 = prices2
    
    # 「陰のはらみ線」パターンの条件をチェック
    if (day1['Close'] > day1['Open'] and  # 1日目は陽線
        day2['Open'] < day1['Close'] and  # 2日目の始値が1日目の終値より低い
        day2['Close'] > day1['Open'] and  # 2日目の終値が1日目の始値より高い
        day2['Close'] < day2['Open']):  # 2日目は陰線
        return True
    
    return False
