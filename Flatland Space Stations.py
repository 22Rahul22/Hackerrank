n, m = map(int, input().split())
arr = list(map(int, input().split()[:m]))
if m == 1:
    print(max(arr[0], n - 1 - arr[0]))
else:
    if n == m:
        print(0)
    else:
        arr.sort()
        b = []
        b.append(arr[0])
        for i in range(1,len(arr)):
            b.append(int((arr[i] - arr[i-1])/2))
        b.append(n - 1 - arr[len(arr)-1])
        print(arr)
        print(b)
        x = max(b)
        print(x)
