t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    a = []
    b = True
    if n == 1:
        if arr[0] == 1:
            print("YES")
        else:
            print("NO")
    else:
        for i in range(len(arr)):
            if arr[i] == 1:
                a.append(i)
        for i in range(1, len(a)):
            if a[i] - a[i - 1] < 6:
                b = False
                print("NO")
                break
            else:
                b = True
        if b:
            print("YES")
    t -= 1
