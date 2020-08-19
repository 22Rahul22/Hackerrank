n = int(input())
a = [2000, 500, 100, 50, 10, 1]
b = []
temp = n
i = 0
while temp > 0:
    r = temp // a[i]
    b.append(r)
    temp -= r*a[i]
    i += 1
for i in range(len(b)):
    if b[i] != 0:
        if i != len(b)-1:
            print(str(a[i])+": "+str(b[i]), end=", ")
        else:
            print(str(a[i])+": "+str(b[i]))