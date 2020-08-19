n = int(input())
arr = list(map(int, input().split()[:n]))
t = arr[n-1]
for i in range(n-2, -1, -1):
    if t >= arr[i]:
        print(i)
        f = 1
        break
    else:
        arr[i+1] = arr[i]
        print(i)
        f = 0
        print(*arr, sep=" ")
if f == 1:
    arr[i+1] = t
else:
    arr[i] = t
print(*arr, sep=" ")