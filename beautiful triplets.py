n, d = [int(n) for n in input().split()]
arr = list(map(int, input().split()[:n]))
c = 0
for i in range(n):
    if (arr[i] + d) in arr and (arr[i] + 2*d) in arr:
        print(arr[i])
        c += 1
print(c)