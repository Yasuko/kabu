
'''
陽の三兵のパターンを検出する

パラメータ:
    prices1 (dict): 2日前の株価情報
    prices2 (dict): 1日前の株価情報
    prices3 (dict): 当日の株価情報
戻り値:
    bool: 陽の三兵パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_three_soldiers_sun(
    prices1,
    prices2,
    prices3
) -> bool:
    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']
  
    # 陽の三兵の条件
    if (day1['close'] > day1['open'] and
        day2['close'] > day2['open'] and
        day3['close'] > day3['open'] and
        day2['open'] > day1['open'] and
        day2['close'] > day1['close'] and
        day3['open'] > day2['open'] and
        day3['close'] > day2['close']):
        return True
    
    return False

'''
陰の三兵のパターンを検出する

パラメータ:
    prices1 (dict): 2日前の株価情報
    prices2 (dict): 1日前の株価情報
    prices3 (dict): 当日の株価情報
戻り値:
    bool: 陰の三兵パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_three_soldiers_shadow(
    prices1,
    prices2,
    prices3
) -> bool:
    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']

    # 陰の三兵の条件
    if (day1['close'] < day1['open'] and
        day2['close'] < day2['open'] and
        day3['close'] < day3['open'] and
        day2['open'] < day1['open'] and
        day2['close'] < day1['close'] and
        day3['open'] < day2['open'] and
        day3['close'] < day2['close']):
        return True
    
    return False

'''
上昇三空のパターンを検出する

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
    prices3 (dict): 2日前の株価情報
戻り値:
    bool: 上昇三空パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_three_gaps_ups(
    prices1,
    prices2,
    prices3
) -> bool:
    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']
    
    # 上昇三空の条件
    if (day2['low'] > day1['high'] and
        day3['low'] > day2['high']):
        return True
    
    return False

'''
下降三空のパターンを検出する

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
    prices3 (dict): 2日前の株価情報
戻り値:
    bool: 下降三空パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_three_gaps_down(
    prices1,
    prices2,
    prices3
) -> bool:
    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']
    
    # 下降三空の条件
    if (day2['high'] < day1['low'] and
        day3['high'] < day2['low']):
        return True
    
    return False

'''
毛抜き底のパターンを検出する

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 毛抜き底パターンが検出された場合はTrue、それ以外はFalse
'''
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


'''
毛抜き天井を検出する

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 毛抜き天井パターンが検出された場合はTrue、それ以外はFalse
'''
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

'''
明けの明星を検出する

パラメータ:
    prices1 (dict): 2日前の株価情報
    prices2 (dict): 1日前の株価情報
    prices3 (dict): 当日の株価情報
戻り値:
    bool: 明けの明星パターンが検出された場合はTrue、それ以外はFalse
'''
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

'''
宵の明星を検出する

パラメータ:
    prices1 (dict): 2日前の株価情報
    prices2 (dict): 1日前の株価情報
    prices3 (dict): 当日の株価情報
戻り値:
    bool: 宵の明星パターンが検出された場合はTrue、それ以外はFalse
'''
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
