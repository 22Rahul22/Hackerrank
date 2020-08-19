n, t = [int(n) for n in input().split()]
width = list(map(int, input().split()[:n]))
while t > 0:
    i, j = [int(i) for i in input().split()]
    a = []
    for k in range(i,j+1):
        a.append(width[k])
    print(min(a))
    t -= 1