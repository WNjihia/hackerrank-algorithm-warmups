def diagonalDifference(arr):
    length = len(arr)
    total = counterTotal = 0
    diagonal = [arr[i][i] for i in range(length)]
    counterDiagonal = [arr[i][~i] for i in range(length)]

    for value in diagonal:
        total += value

    for value in counterDiagonal:
        counterTotal += value

    return abs(total - counterTotal)
