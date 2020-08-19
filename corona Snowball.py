def split(ki):
    return [char for char in ki]

t = int(input())
for i in range(t):
    ki = input()
    a = split(ki)
    c = 0
    for j in range(len(a)-1):
        z = 0
        if a[j] == 'A' and a[j+1] == 'P':
            a[j+1] = 'A'
            c += 1
        b = 0
        for k in a:
            if k == 'A':
                b += 1
        if b == len(a) or b == 2:

    print(a)
    print(c)