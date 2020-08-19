t = int(input())
while t > 0:
    n = int(input())
    s = input()
    a = []
    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in s:
        if i not in a:
            a.append(i)
        else:
            b[int(ord(i))-97] += 1
    print(a)
    print(b)
    s = 0
    for i in b:
        if i == 0:
            continue
        else:
            s += int(i*(i+1)/2)
    print(s)
    t -= 1