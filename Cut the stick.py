def minimum(a):
    m = a[0]
    for i in range(len(a)):
        if m > a[i] != 0 or m == 0:
            m = a[i]
    return m


n = int(input())
arr = list(map(int, input().split()[:n]))
b = []
for i in range(n):
    c = 0
    b.append(0)
    d = minimum(arr)
    for j in range(n):
        if arr[j] > 0:
            arr[j] -= d
            b[i] += 1
        else:
            c += 1
    if c == n:
        break
b.remove(0)
print(b)