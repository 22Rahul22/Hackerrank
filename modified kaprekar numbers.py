p = int(input())
q =int(input())
t = 0
for i in range(p,q+1):
    temp = i
    temp *= temp
    temp1 = temp
    x = str(i)
    b = 0
    s = 0
    r = 0
    while b < len(x):
        r = temp1%10
        s = pow(10,b)*r + s
        b += 1
        temp1 = int(temp1 / 10)
    if s + temp1 == i:
        t = 1
        print(str(i), end=" ")
if t == 0:
    print("INVALID RANGE")