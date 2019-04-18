def miniMaxSum(arr):
    total = 0
    min = max = arr[0]

    for value in arr:
        total += value

        if value < min:
            min = value

        if value > max:
            max = value

    print(total-max, total-min)

miniMaxSum([1, 2, 3, 4, 5])
