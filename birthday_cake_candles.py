def birthdayCakeCandles(ar):
    candles = {}
    for value in ar:
        if value in candles:
            candles[value] += 1
        else:
            candles[value] = 1

    return candles[max(candles)]
