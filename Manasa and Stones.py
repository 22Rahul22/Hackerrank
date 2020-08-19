t = int(input())
for _ in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    arr = []
    z = min(a, b)
    x = (n - 1) * z
    arr.append(x)
    y = abs(a - b)
    if y == 0:
        print(arr[0],end=" ")
    else:
        for i in range(n-1):
            x += y
            arr.append(x)
        for i in range(n):
            print(arr[i], end=" ")
    print()