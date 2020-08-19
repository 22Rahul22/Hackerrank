t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    p = list(map(int, input().split()[:n]))
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(n):
        if a[i] == 0:
            b.append(p[i])
        else:
            c.append(p[i])
    x = min(b)
    y = min(c)
    if x + y < (100 - s):
        print("yes")
    else:
        print("no")
