n = int(input())
p = list(map(int,input().split()[:n]))
a = []
for i in range(1,n+1):
    x = p.index(i)
    y = p.index(x+1)
    a.append(y+1)

print(a)