x1, v1, x2, v2 = [int(x1) for x1 in input().split()]
a = x1
b = x2
flag = 2
while a < b and flag is not 0:
    if x1 == x2 and v1 == v2:
        flag = 1
    elif x1 is not x2 and v1 == v2:
        flag = 0
    elif x2 > x1 and v2 > v1:
        flag = 0
    elif v1 > v2:
        while a <= b:
            a = a+v1
            b = b+v2
        if a-v1 == b-v2:
            flag = 1

if flag == 1:
    print("YES")
else:
    print("NO")