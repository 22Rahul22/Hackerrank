t = int(input())
for i in range(t):
    a, b, c, d = [int(a) for a in input().split()]
    x = abs(a - b)
    y = abs(c - d)
    if x == 0:
        print("YES")
    elif (y == 0 and x != 0) or x % y != 0 :
        print("NO")
    else:
        print("YES")