t = int(input())
while(t > 0):
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()[:n]))
    c = 0
    for i in a:
        if i <= 0:
            c += 1
    if c >= k:
        print("NO")
    else:
        print("Yes")
    t -= 1
