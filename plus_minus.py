def plusMinus(arr):
    length = len(arr)
    positive = negative = zero = 0
    for value in arr:
        if value > 0:
            positive += 1
        if value < 0:
            negative += 1
        if value == 0:
            zero += 1
    print(positive/length)
    print(negative/length)
    print(zero/length)
