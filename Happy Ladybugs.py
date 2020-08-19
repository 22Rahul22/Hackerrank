g = int(input())
for _ in range(g):
    n = int(input())
    b = input()
    c = []
    under = 0
    flag = 0
    for i in range(n):
        if b[i] not in c:
            c.append(b[i])
    a = [0]*len(c)
    for i in range(n):
        if b[i] == '_':
            under += 1
        else:
            a[c.index(b[i])] += 1
    c = [b[0]]
    if under == 0:
        for i in range(1, n):
            if b[i] != b[i-1]:
                c.append(b[i])
        d = []
        for i in range(len(c)):
            if c[i] in d or a[i] == 1:
                print("NO")
                flag = 1
                break
            else:
                d.append(c[i])
    else:
        for i in a:
            if i == 1:
                print("NO")
                flag = 1
                break
    if flag == 0:
        print("YES")
