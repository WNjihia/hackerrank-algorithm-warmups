def staircase(n):
    for i in range(1, n+1):
        space = ''.join([' ' for s in range(n - i)])
        print(space + "#"*i)
