'''
陽の包み線を検出する

上げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 陽の包み線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bullish_engulfing(
    day1,
    day2
) -> bool:
    # 「陽の包み線」パターンの条件をチェック
    if (day1['close'] < day1['open'] and  # 1日目は陰線
        day2['open'] < day1['close'] and  # 2日目の始値が1日目の終値より低い
        day2['close'] > day1['open'] and  # 2日目の終値が1日目の始値より高い
        day2['close'] > day2['open']):  # 2日目は陽線
        return True
    
    return False

'''
陰の包み線を検出する

下げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 陰の包み線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_engulfing(
    day1,
    day2
) -> bool:
    # 「陰の包み線」パターンの条件をチェック
    if (day1['close'] > day1['open'] and  # 1日目は陽線
        day2['open'] > day1['close'] and  # 2日目の始値が1日目の終値より高い
        day2['close'] < day1['open'] and  # 2日目の終値が1日目の始値より低い
        day2['close'] < day2['open']):  # 2日目は陰線
        return True
    
    return False

'''
陽のはらみ線を検出する

上げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 陽のはらみ線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bullish_harami(
    day1,
    day2
) -> bool:
    # 「陽のはらみ線」パターンの条件をチェック
    if (day1['close'] < day1['open'] and  # 1日目は陰線
        day2['open'] > day1['low'] and  # 2日目の始値が1日目の安値より高い
        day2['close'] < day1['open'] and  # 2日目の終値が1日目の始値より低い
        day2['close'] > day2['open']):  # 2日目は陽線
        return True
    
    return False

'''
陰のはらみ線を検出する

前日が陽線で、当日が陰線で尚且つ
前日のローソクの足が、翌日のローソクの足より短く
前日のローソクの足が、翌日のローソクの足の中にある場合

シグナル
    下げ

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 陰のはらみ線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_harami(
    prev_candle,
    candle
) -> bool:
    # 「陰のはらみ線」パターンの条件をチェック
    if (prev_candle['close'] > prev_candle['open'] and  # 1日目は陽線
        candle['open'] < prev_candle['close'] and  # 2日目の始値が1日目の終値より低い
        candle['close'] > prev_candle['open'] and  # 2日目の終値が1日目の始値より高い
        candle['close'] < candle['open']):  # 2日目は陰線
        return True
    
    return False

'''
かぶせ線を検出する

大陽線を付けた翌日に、大陰線を付けて尚且つ
2日目の始値が1日目の終値よりも高く
2日目の終値が1日目の始値と終値の中間値と始値の間にある場合

下げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: かぶせ線パターンが検出された場合はTrue、それ以外はFalse
'''
def is_dark_cloud_cover(
    prev_candle,
    curr_candle
):
    # 1日目が大陽線、2日目が大陰線
    if prev_candle['open'] < prev_candle['close'] and curr_candle['open'] > curr_candle['close']:
            # 2日目の始値が1日目の終値よりも高く
            # 2日目の終値が1日目の始値と終値の中間値と始値の間にある
            if (curr_candle['open'] > prev_candle['close']
                and curr_candle['close'] > (prev_candle['open'] + prev_candle['close']) / 2
                and curr_candle['close'] < prev_candle['open']):
                    return True
    return False

'''
切り込み線を検出する

大陰線を付けた翌日に、大陽線を付けて尚且つ
2日目の終値が1日目の始値と終値の中間値を超えている場合

シグナル
    上昇

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 切り込み線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_piercing_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の終値よりも低く
        # 2日目の終値が1日目の始値と終値の中間値を超えている
        if (curr_candle['open'] < prev_candle['close']
            and curr_candle['close'] > (prev_candle['open'] + prev_candle['close']) / 2):
            return True
    
    return False

'''
差し込み線を検出する

大陰線を付けた翌日に、陽線を付けて尚且つ
2日目のヒゲの部分だけが、1日目の始値と終値の中間値を超えている場合

トレンド
    維持

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 差し込み線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_harami_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の終値、始値と終値の中間値にあり
        # 2日目の最高値が1日目の始値と終値の中心値を超えている
        if (curr_candle['open'] > prev_candle['close']
            and curr_candle['open'] < (prev_candle['close'] + prev_candle['open'] / 2)
            and curr_candle['high'] > (prev_candle['close'] + prev_candle['open'] / 2)):
            return True
    
    return False

'''
入り首線を検出する

大陰線を付けた翌日に、陽線を付けて尚且つ
2日目の開始値が、前日の終値、最低値よりも高く
2日目の最高値が、1日目の始値と終値の中心値まで届かなかった場合

シグナル
    買い弱

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 入り首線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_in_neck_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の終値、最低値よりも高く、2日目の最高値が、1日目の始値と終値の中心値の間にある
        if (curr_candle['open'] > prev_candle['close']
            and curr_candle['open'] > prev_candle['high']
            and curr_candle['open'] < (prev_candle['open'] + prev_candle['close']) / 2
            and curr_candle['high'] < (prev_candle['open'] + prev_candle['close']) / 2):
            return True
    
    return False

'''
あて首線を検出する

大陰線を付けた翌日に、大陽線を付けて尚且つ
2日目の開始値と1日目の開始値が離れて、隙間がある場合

シグナル
    下げ弱

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: あて首線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_on_neck_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の終値よりも1段低い（1%以上）
        if (curr_candle['open'] < prev_candle['close']
            and (prev_candle['close'] > prev_candle['open'] + (prev_candle['open'] * 0.01))):
            return True
    
    return False

'''
出会い線の陽線パターンを検出する

大陽線を付けた翌日に、大陰線を付けて尚且つ
2日目の終値が1日目の終値とほぼ同じ場合

シグナル
    下げ

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 出会い線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_meeting_lines_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陽線、2日目が大陰線
    if (prev_candle['open'] < prev_candle['close']
        and curr_candle['open'] > curr_candle['close']):

        # 2日目の終値が1日目の終値とほぼ同じ（1%以内）
        if (curr_candle['close'] < (prev_candle['close'] + (prev_candle['close'] * 0.01))
            and curr_candle['close'] > (prev_candle['close'] - (prev_candle['close'] * 0.01))):
            return True
    
    return False

'''
出会い線の陰線パターンを検出する

大陰線を付けた翌日に、大陽線を付けて尚且つ
2日目の始値が1日目の終値とほぼ同じ場合

シグナル
    上げ

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 出会い線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_meeting_lines_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陰線、2日目が大陽線
    if (prev_candle['open'] > prev_candle['close']
        and curr_candle['open'] < curr_candle['close']):

        # 2日目の始値が1日目の終値とほぼ同じ（1%以内）
        if (curr_candle['open'] > (prev_candle['close'] - (prev_candle['close'] * 0.01))
            and curr_candle['open'] < (prev_candle['close'] + (prev_candle['close'] * 0.01))):
            return True
    
    return False

'''
振り分け線の陽線パターンを検出する

大陰線を付けた翌日に、大陽線を付けて尚且つ
2日目の始値が1日目の始値とほぼ同じ場合

シグナル
    上げ

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 振り分け線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_separating_lines_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陰線、2日目が大陽線
    if (prev_candle['open'] > prev_candle['close']
        and curr_candle['open'] < curr_candle['close']):

        # 2日目の始値が1日目の終値とほぼ同じ（1%以内）
        if (curr_candle['open'] <= (prev_candle['open'] + (prev_candle['open'] * 0.01))
            and curr_candle['open'] >= (prev_candle['open'] - (prev_candle['open'] * 0.01))):
            return True
    
    return False

'''
振り分け線の陰線パターンを検出する

大陽線を付けた翌日に、大陰線を付けて尚且つ
2日目の始値が1日目の始値とほぼ同じ場合

下げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 振り分け線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_separating_lines_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陽線、2日目が大陰線
    if (prev_candle['open'] < prev_candle['close']
        and curr_candle['open'] > curr_candle['close']):

        # 2日目の始値が1日目の始値とほぼ同じ(1%以内)
        if (curr_candle['open'] >= (prev_candle['open'] - (prev_candle['open'] * 0.01))
            and curr_candle['open'] <= (prev_candle['open'] + (prev_candle['open'] * 0.01))):
            return True
    
    return False


'''
タスキ線の陽線パターンを検出する

上げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: タスキ線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_tasukigap_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の終値よりも低く、2日目の終値が1日目の始値よりも高い
        if curr_candle['open'] < prev_candle['close'] and curr_candle['close'] > prev_candle['open']:
            return True
    
    return False

'''
タスキ線の陰線パターンを検出する

下げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: タスキ線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_tasukigap_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目も陰線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] > curr_candle['close']:
        # 2日目の始値が1日目の終値よりも低く、2日目の終値が1日目の始値よりも低い
        if curr_candle['open'] < prev_candle['close'] and curr_candle['close'] < prev_candle['open']:
            return True
    
    return False

'''
毛抜き天井のパターンを検出する

下げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 毛抜き天井パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_tweezer_top_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陽線、2日目が陰線
    if prev_candle['open'] < prev_candle['close'] and curr_candle['open'] > curr_candle['close']:
        # 1日目と2日目の高値がほぼ同じ
        if prev_candle['high'] == curr_candle['high']:
            return True
    
    return False

'''
毛抜き底のパターンを検出する

上げシグナル

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 毛抜き底パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_tweezer_bottom_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 1日目と2日目の安値がほぼ同じ
        if prev_candle['low'] == curr_candle['low']:
            return True
    
    return False