t = int(input())
while t > 0:
    n, c, m = [int(n) for n in input().split()]
    x = n // c
    bar = x
    y = 100
    while y > 0:
        y = x // m
        x = x % m + y
        bar += y
    print(bar)
    t -= 1
