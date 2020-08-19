n = int(input())
a = list(map(int, input().split()[:n]))
b = []
for i in range(n):
    k = i+1
    for j in range(k,n):
        if a[i] == a[j]:
           b.append(j-i)
if not b:
    print(-1)
else:
    print(min(b))