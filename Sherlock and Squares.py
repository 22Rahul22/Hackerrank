import math
q = int(input())
while q > 0:
    a = int(input())
    b = int(input())
    c = 0
    for i in range(a,b+1):
        if (math.sqrt(i)).is_integer():
            x = math.sqrt(i)
            c += 1
            break
    z = True
    while z:
        x += 1
        if z < x*x <= b:
            c += 1
        else:
            break
    print(c)
    q -= 1