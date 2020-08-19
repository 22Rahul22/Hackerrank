n = int(input())
c = list(map(int, input().split()[:n]))
c.append(100)
c.append(100)
t = 0
i = 0
while i < n:
    if c[i+2] == 1 or c[i+2] == 100:
        t += 1
        i += 1
    else:
        t += 1
        i += 2
    print("i = "+str(i))
print(t-1)