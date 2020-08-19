import math
s = input()
code = s[:]
l = len(s) - s.count(" ")
c = math.ceil(math.sqrt(l))
r = math.floor(math.sqrt(l))
if r*c < l:
    r = c
a = []
for i in range(r):
    a.append(code[:c])
    code = code[c:]
print(a)
enc = ''
for i in range(c):
    for j in range(r):
        if i < len(a[j]):
            enc += a[j][i]
    enc += " "
print(enc)