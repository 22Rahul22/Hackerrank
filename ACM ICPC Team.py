n, m = [int(n) for n in input().split()]
arr = []
for i in range(n):
    s = input()
    x = [int(r) for r in str(s)]
    arr.append(x)
t = []
z = 0
for i in range(n - 1):
    k = i + 1
    while k < n:
        j = 0
        t.append(0)
        for j in range(m):
            if arr[i][j] == 1 or arr[k][j] == 1:
                t[z] += 1
        z += 1
        k += 1
a = max(t)
c = 0
for i in t:
    if i == a:
        c += 1
b = [a, c]
print(b)
