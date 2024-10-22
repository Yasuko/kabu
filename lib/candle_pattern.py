

def pattern1(
    candle1: dict,
    candle2: dict,
    candle3: dict,
    trend: str
) -> int:
    score = 10

    if trend == 'sun':
        if candle1['key'] == 'strong_hummer_sun': score -= 3
        if candle2['key'] == 'strong_hummer_sun': score -= 4 
        if candle3['key'] == 'strong_hummer_sun': score -= 5
        
        if candle1['key'] == 'weak_hummer_sun': score -= 2
        if candle2['key'] == 'weak_hummer_sun': score -= 3 
        if candle3['key'] == 'weak_hummer_sun': score -= 4

        if candle1['key'] == 'tower_top': score -= 1
        if candle2['key'] == 'tower_top': score -= 2 
        if candle3['key'] == 'tower_top': score -= 3

        if candle3['key'] == 'upper_shadow_top_sun': score -= 2
    
        return score
    
    if trend == 'shadow':
        if candle1['key'] == 'strong_umbrella_shadow': score -= 3
        if candle2['key'] == 'strong_umbrella_shadow': score -= 4 
        if candle3['key'] == 'strong_umbrella_shadow': score -= 5
        
        if candle1['key'] == 'weak_umbrella_shadow': score -= 2
        if candle2['key'] == 'weak_umbrella_shadow': score -= 3 
        if candle3['key'] == 'weak_umbrella_shadow': score -= 4

        if candle1['key'] == 'dragonfly_shadow': score -= 1
        if candle2['key'] == 'dragonfly_shadow': score -= 2 
        if candle3['key'] == 'dragonfly_shadow': score -= 3

        if candle3['key'] == 'lower_shadow_top_sun': score -= 2
    
        return score

