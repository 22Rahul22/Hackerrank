p, d, m, s = [int(p) for p in input().split()]
c = 0
t = 0
while t <= s:
    t += p
    p -= d
    c += 1
    if p <= m:
        p = m
print(c-1)