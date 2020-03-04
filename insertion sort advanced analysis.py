t = int(input())
while(t > 0):
    n = int(input())
    a = list(map(int, input().split()[:n]))
    b = []
    sum = 0
    for i in range(n):
        if a[i] in b:
            b.append(a[i])
            b.sort()
            for z in range(len(b)):
                if b[z] == a[i]:
                    x = z
            sum += abs(i - x)
        else:
            b.append(a[i])
            b.sort()
            sum += abs(i-b.index(a[i]))
    print(sum)
    t -= 1