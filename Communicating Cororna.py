from functools import reduce

t = int(input())
while t > 0:
    n, m = [int(n) for n in input().split()]
    arr = [0]
    while m > 0:
        l, r, p = [int(l) for l in input().split()]
        for i in range(l-1, r):
            arr[i] += p
        m -= 1
    x = 0
    for i in range(len(arr)):
        x = x ^ arr[i]
    print(x)
    t -= 1