n, k = [int(n) for n in input().split()]
arr = list(map(int, input().split()[:n]))
a = [0]
t = 0
for i in range(n):
    x = arr[i] // k
    for j in range(x):
        a.append((j+1) * k)
        t = (j+1) * k
    if t != arr[i]:
        a.append(arr[i]%k+x*k)
s = 1
print(a)

for i in range(2,len(a)):
    if a[i-1] < i <= a[i]:
        s += 1
    elif a[i-1] >= a[i] or a[i-1] < k:
        if 1 < i <= a[i]:
            s += 1
print(s)