n = int(input())
s = input()
num = 0
lc = 0
uc = 0
sc = 0
c = 0
for i in range(n):
    if 33 <= ord(s[i]) <= 47 or 58 <= ord(s[i]) <= 64 or 91 <= ord(s[i]) <= 96 or 123 <= ord(s[i]) <= 126:
        sc += 1
    elif 48 <= ord(s[i]) <= 57:
        num += 1
    elif 65 <= ord(s[i]) <= 90:
        uc += 1
    elif 97 <= ord(s[i]) <= 122:
        lc += 1
if sc == 0:
    c += 1
if lc == 0:
    c += 1
if uc == 0:
    c += 1
if num == 0:
    c += 1
if len(s) < 6:
    if c + len(s) < 6:
        print(6 - len(s))
    else:
        print(c)
else:
    print(c)