s = input()
c = 1
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        c += 1
print(c)