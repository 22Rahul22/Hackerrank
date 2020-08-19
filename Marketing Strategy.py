s = input()
n = len(s)
c1 = 0
c2 = 0
for i in range(n):
    if i % 2 == 0:
        a = 'S'
        b = 'R'
    else:
        a = 'R'
        b = 'S'
    if a != s[i]:
        c1 += 1
    if b != s[i]:
        c2 += 1
print(min(c1, c2))