t = int(input())
mod = pow(10, 9) + 7
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    s = 0
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if arr[i] == 0:
            break
        elif arr[i] - i > 0:
            s += arr[i] - i
        else:
            break
    print(s % mod)
    t -= 1