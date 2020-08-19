q = int(input())
for _ in range(q):
    s = input()
    if len(s) % 2 != 0:
        print(-1)
    else:
        a = s[:int(len(s)/2)]
        b = s[int(len(s)/2):]
        c = 0
        for i in a:
            if a.count(i) == b.count(i):
                c += 0
            else:
                c += abs(a.count(i) - b.count(i))
        print(int(c/2))