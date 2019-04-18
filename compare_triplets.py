def compareTriplets(a,b):
    c = d = 0
    for index in range(3):
        if a[index] > b[index]:
            c += 1
        if a[index] < b[index]:
            d += 1
    return c,d
