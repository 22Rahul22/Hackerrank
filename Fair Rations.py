n = int(input())
arr = list(map(int, input().split()[:n]))
c = 0
for i in range(n):
    if arr[i] % 2 != 0 and i != n-1:
        arr[i] += 1
        arr[i+1] += 1
        c += 2
if arr[0] % 2 != 0 or arr[n - 1] % 2 != 0:
    print("NO")
else:
    print(c)
