s = input()
c = 0
sos = 'SOS'
for i in range(len(s)):
    if s[i] != sos[i%3]:
        c += 1
print(c)