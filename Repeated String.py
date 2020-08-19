s = input()
n = int(input())
x = len(s)
c = 0
d = int(n/x)
for i in s:
    if i == 'a':
        c += 1
t = c*d
r = n%x
for i in range(r):
    if s[i] == 'a':
        t += 1